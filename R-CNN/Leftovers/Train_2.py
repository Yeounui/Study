import os
import time
import tensorflow as tf
import numpy as np

import Dataflow
import Model_low

Seed = 1
Epochs = 200

DATA_PATH = "C:\\Pascal VOC 2012\\VOC_train_val2012\\VOCdevkit\\VOC2012"
IMAGE_FOLDER = "JPEGImages"
ANNOTATIONS_FOLDER = "Annotations"
PROPOSAL_FOLDER = "Proposals"
SAVE_FOLDER = "SaveModels\\Detection"


# Set up Training dataset and Validation set
DataTensor = Dataflow.BoxDetection([DATA_PATH, ANNOTATIONS_FOLDER, PROPOSAL_FOLDER])
PosRawTensor, NegRawTensor, PosVal, NegVal = Dataflow.ValidationSplit(DataTensor, seed=Seed)
RawBatchProcess = Dataflow.RawBatchProcessing([DATA_PATH, IMAGE_FOLDER])
valid_x, valid_y = RawBatchProcess([PosVal, NegVal])
PosRawDataset = tf.data.Dataset.from_tensor_slices(PosRawTensor)
PosRawDataset = PosRawDataset.shuffle(buffer_size=tf.shape(PosRawTensor).numpy()[0], seed=Seed).batch(32)
NegRawDataset = tf.data.Dataset.from_tensor_slices(NegRawTensor)
NegRawDataset = NegRawDataset.shuffle(buffer_size=tf.shape(NegRawTensor).numpy()[0], seed=Seed).batch(96)

# Set up model
load_weight = np.load(os.path.join(DATA_PATH, "bvlc_alexnet.npy"), allow_pickle=True, encoding="latin1").item()
Model = Model_low.AlexNet(Seed)
Model.feed_pretrained(load_weight)
print(Model.summary())

# Set up optimizer & loss
Learning_rate, Beta_1, Beta_2 = 0.001, 0.9, 0.999
optimizer = tf.keras.optimizers.Adam(learning_rate=Learning_rate, beta_1=Beta_1, beta_2=Beta_2, name='Adam')
loss = tf.keras.losses.BinaryCrossentropy()

# Set up metrics
train_accuracy = tf.keras.metrics.CategoricalAccuracy(name='train_accuracy')
valid_accuracy = tf.keras.metrics.CategoricalAccuracy(name='valid_accuracy')

@tf.function
def train_step(train_x, train_y):
    with tf.GradientTape() as tape:
        pred_y = Model(train_x, training=True)
        loss_value = loss(train_y, pred_y)
    grads = tape.gradient(loss_value, Model.trainable_variables)
    optimizer.apply_gradients(zip(grads, Model.trainable_variables))
    train_accuracy.update_state(train_y, pred_y)
    return loss_value

@tf.function
def Validate_step(valid_x, valid_y):
    pred_y = Model(valid_x)
    valid_accuracy.update_state(valid_y, pred_y)


for epoch in range(Epochs):
    print("\nStart of epoch %d" % (epoch,))
    start_time = time.time()
    iterNegRaw = iter(NegRawDataset)
    for step, PosRawBatch in PosRawDataset.enumerate():

        Batch = tf.concat([PosRawBatch, iterNegRaw.get_next()], axis=0)
        train_x, train_y = RawBatchProcess(Batch)

        loss_value = train_step(train_x, train_y)

        if (step+1) % 100 == 0:
            print("Training loss (for one batch) at step %d: %.8f" % (step+1, float(loss_value)))
            print("Seen so far: Positive %d samples within %d samples in %.4f"
                  % ((step + 1) * 32, DataTensor.get_shape()[0], time.time() - start_time))
        if (step+1) % 1000 == 0:
            Model.save_weights(os.path.join(DATA_PATH, SAVE_FOLDER, time.strftime("%Y%m%d_%H%M")))
            Validate_step(valid_x, valid_y)
            valid_acc_value = valid_accuracy.result()
            valid_accuracy.reset_states()
            print("Validation acc: %.4f" % (float(valid_acc_value),))
            print("Time taken: %.2fs" % (time.time() - start_time))

    train_acc = train_accuracy.result()
    print("Training acc over epoch: %.8f" % (float(train_acc),))

    # Reset training metrics at the end of each epoch
    train_accuracy.reset_states()

    Validate_step(valid_x, valid_y)

    valid_acc_value = valid_accuracy.result()
    valid_accuracy.reset_states()
    print("Validation acc: %.4f" % (float(valid_acc_value),))
    print("Time taken: %.2fs" % (time.time() - start_time))

    Model.save_weights(os.path.join(DATA_PATH, SAVE_FOLDER, time.strftime("%Y%m%d_%H%M")))