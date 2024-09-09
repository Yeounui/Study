import os
import time
import tensorflow as tf
import numpy as np
import Dataflow
import Model_low

Seed = 26
BatchSize = 400

DATA_PATH = "C:\\Pascal VOC 2012\\VOC_train_val2012\\VOCdevkit\\VOC2012"
IMAGE_FOLDER = "JPEGImages"
ANNOTATIONS_FOLDER = "Annotations"
PROPOSAL_FOLDER = "Proposals"
SAVE_FOLDER = "SaveModels\\Classification"
CLASS = "Person"
ObjDetectModel = "SaveModels\\Detection\\20201001_1749"

# Set up Training dataset and Validation set
RawTensor = Dataflow.ObjectClassification([DATA_PATH, ANNOTATIONS_FOLDER, PROPOSAL_FOLDER], Dataflow.numerate(CLASS))
RawDataset = tf.data.Dataset.from_tensor_slices(RawTensor)
RawDataset = RawDataset.shuffle(buffer_size=tf.shape(RawTensor).numpy()[0], seed=Seed).batch(BatchSize)
RawBatchProcess = Dataflow.RawBatchProcessing([DATA_PATH, IMAGE_FOLDER])


# Set up model
ObjDetect = Model_low.AlexNet()
ObjDetect.load_weights(os.path.join(DATA_PATH, ObjDetectModel))
SplitAlexNet = tf.keras.models.Model(ObjDetect.get_layer("conv1").input, ObjDetect.get_layer("relu7").output,
                                     name="SplitAlexNet")
ObjClass = Model_low.SVM(name="SVM")

# Set up optimizer, loss
Learning_rate, Beta_1, Beta_2 = 0.01, 0.9, 0.999
optimizer = tf.keras.optimizers.Adam(learning_rate=Learning_rate, beta_1=Beta_1, beta_2=Beta_2, name='Adam')
Loss = Model_low.SVMLoss(regularization_parameter = 1e-6, name="SVMLoss")

# Set up metrics
train_accuracy = tf.keras.metrics.CategoricalAccuracy(name='train_accuracy')
valid_accuracy = tf.keras.metrics.CategoricalAccuracy(name='valid_accuracy')
current_time = time.strftime("%Y%m%d-%H%M%S")
train_log_dir = 'logs/gradient_tape/' + current_time + '/train'
test_log_dir = 'logs/gradient_tape/' + current_time + '/test'
train_summary_writer = tf.summary.create_file_writer(train_log_dir)
test_summary_writer = tf.summary.create_file_writer(test_log_dir)


@tf.function
def train_step(train_x, train_y):
    FeatVec = SplitAlexNet(train_x, training=False)
    with tf.GradientTape() as tape:
        pred_y = ObjClass(FeatVec)
        loss_value = Loss(train_y, pred_y, ObjClass.trainable_variables[0])
    grads = tape.gradient(loss_value, ObjClass.trainable_variables)
    optimizer.apply_gradients(zip(grads, ObjClass.trainable_variables))
    train_accuracy.update_state(train_y, pred_y)
    return loss_value

@tf.function
def valid_step(valid_x, valid_y):
    FeatVec = SplitAlexNet(valid_x, training=False)
    pred_y = ObjClass(FeatVec)
    loss_value = Loss(valid_y, pred_y, ObjClass.trainable_variables[0])
    valid_accuracy.update_state(valid_y, pred_y)
    return loss_value

start_time = time.time()
for step, RawBatch in RawDataset.enumerate():
    if step == 0:
        valid_x, valid_y = RawBatchProcess(RawBatch)
        print("The number of positive data in a validation set is %d" % (tf.reduce_sum(valid_y[:, 1]).numpy()))
    else:
        batch_x, batch_y = RawBatchProcess(RawBatch)
        loss_result = train_step(batch_x, batch_y)
        accuracy_result = train_accuracy.result()
        with train_summary_writer.as_default():
            tf.summary.scalar("PosNum", tf.reduce_sum(batch_y[:, 1]), step=step)
            tf.summary.scalar("Loss", loss_result, step=step)
            tf.summary.scalar("Accuracy", accuracy_result, step=step)

        if step % 30 == 0:
            print("At step %d, (for one batch)" % (step))
            print("Training acc & los: %.6f, %.6f" % (float(accuracy_result), float(loss_result)))
            valid_los = valid_step(valid_x, valid_y)
            print("Validation acc & los: %.6f, %.6f" % (float(valid_accuracy.result()), float(valid_los)))
            print("Seen so far: %d %s samples within %d samples in %.4f"
                  % (step * BatchSize, CLASS, RawTensor.get_shape()[0] - BatchSize, time.time() - start_time))
            with test_summary_writer.as_default():
                tf.summary.scalar("Accuracy", train_accuracy.result(), step=step)
            train_accuracy.reset_states()
            valid_accuracy.reset_states()
        if step % 500 == 0:
            ObjClass.save_weights(os.path.join(DATA_PATH, SAVE_FOLDER, CLASS, time.strftime("%Y%m%d_%H%M")))


valid_los = valid_step(valid_x, valid_y)
print("Validation acc & los: %.6f, %.6f" % (float(valid_accuracy.result()), float(valid_los)))
ObjClass.save_weights(os.path.join(DATA_PATH, SAVE_FOLDER, CLASS, time.strftime("%Y%m%d_%H%M")))