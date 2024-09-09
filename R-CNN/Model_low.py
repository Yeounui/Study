import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, ReLU, MaxPool2D, Dense, Flatten, Dropout, Softmax

# load_weight = np.load('C:\\Users\\korea\\Downloads\\bvlc_alexnet.npy', allow_pickle=True, encoding='latin1').item()
# for layer in load_weight.keys():
#    print(layer)
#    for weight in load_weight[layer]:
#        print(weight.shape)


class AlexNet(tf.keras.models.Model):
    def __init__(self, seed=None, name=None):
        super().__init__(name=name, inputs=self.input_layer,
                                    outputs=self.out)
        self.input_layer = Input((227,227,3))

        self.conv1 = Conv2D(filters=96, kernel_size=11, strides=(4, 4), padding='valid',
                            input_shape=(None, 227, 227, 3), name="conv1")
        self.conv2 = Conv2D(filters=256, kernel_size=5, padding='same', name="conv2")
        self.conv3 = Conv2D(filters=384, kernel_size=3, padding='same', name="conv3")
        self.conv4 = Conv2D(filters=384, kernel_size=3, padding='same', name="conv4")
        self.conv5 = Conv2D(filters=256, kernel_size=3, padding='same', name="conv5")

        self.fc6 = Dense(4096, use_bias=True, name='fc6')
        self.fc7 = Dense(4096, use_bias=True, name='fc7')
        self.fc8 = Dense(2, use_bias=True, name='fc8',
                         kernel_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=1.0, seed=seed),
                         bias_initializer=tf.keras.initializers.RandomNormal(mean=0.0, stddev=1.0, seed=seed))

        self.maxpol1 = MaxPool2D(pool_size=3, strides=2, padding='valid', name="maxpol1")
        self.maxpol2 = MaxPool2D(pool_size=3, strides=2, padding='valid', name="maxpol2")
        self.maxpol5 = MaxPool2D(pool_size=3, strides=2, padding='valid', name="maxpol3")

        self.relu2 = ReLU(name="relu2")
        self.relu3 = ReLU(name="relu3")
        self.relu4 = ReLU(name="relu4")
        self.relu5 = ReLU(name="relu5")
        self.relu6 = ReLU(name="relu6")
        self.relu7 = ReLU(name="relu7")

        self.flat6 = Flatten(name="flat6")

        self.dropout6 = Dropout(0.5, seed=seed, name='dropout6')
        self.dropout7 = Dropout(0.5, seed=seed, name='dropout7')

        self.softmax8 = Softmax(name="softmax8")

        self.out = self.call(self.input_layer)


    def call(self, inputs, training=False):
        # layer1: conv2d, lrn, maxpool; stride 4, padding
        conv1 = self.conv1(inputs)
        lrn1 = tf.nn.local_response_normalization(input=conv1,
                                                  depth_radius=2,
                                                  alpha=2e-05,
                                                  beta=0.75,
                                                  bias=1.0,
                                                  name="lrn1")
        maxpol1 = self.maxpol1(lrn1)

        # layer2: conv2d, relu, lrn, maxpool; divided into 2.
        conv2 = self.conv2(maxpol1)
        relu2 = self.relu2(conv2)
        lrn2 = tf.nn.local_response_normalization(input=relu2,
                                                  depth_radius=2,
                                                  alpha=2e-05,
                                                  beta=0.75,
                                                  bias=1.0,
                                                  name="lrn2")
        maxpol2 = self.maxpol2(lrn2)

        # layer3: conv2d, relu
        conv3 = self.conv3(maxpol2)
        relu3 = self.relu3(conv3)

        # layer4: conv2d, relu; divided into 2.
        conv4 = self.conv4(relu3)
        relu4 = self.relu4(conv4)

        # layer5: conv2d, relu, maxpool; divided into 2.
        conv5 = self.conv5(relu4)
        relu5 = self.relu5(conv5)
        maxpol5 = self.maxpol5(relu5)

        # layer6: fc, relu
        flat6 = self.flat6(maxpol5)
        if training:
            flat6 = self.dropout6(flat6, training=training)
        fc6 = self.fc6(flat6)
        relu6 = self.relu6(fc6)

        # layer7: fc, relu
        if training:
            relu6 = self.dropout7(relu6, training=training)
        fc7 = self.fc7(relu6)
        relu7 = self.relu7(fc7)

        # layer8: fc, softmax
        fc8 = self.fc8(relu7)
        prob = self.softmax8(fc8)

        return prob

    def feed_pretrained(self, weights):
        conv2_weights = [np.tile(weights['conv2'][0], (1, 1, 2, 1)), weights['conv2'][1]]
        conv4_weights = [np.tile(weights['conv4'][0], (1, 1, 2, 1)), weights['conv4'][1]]
        conv5_weights = [np.tile(weights['conv5'][0], (1, 1, 2, 1)), weights['conv5'][1]]
        self.conv1.build(tf.TensorShape([None, 227, 227, 3]))
        self.conv1.set_weights(weights['conv1'])
        self.conv2.build(tf.TensorShape([None, 55, 55, 96]))
        self.conv2.set_weights(conv2_weights)
        self.conv3.build(tf.TensorShape([None, 27, 27, 256]))
        self.conv3.set_weights(weights['conv3'])
        self.conv4.build(tf.TensorShape([None, 13, 13, 384]))
        self.conv4.set_weights(conv4_weights)
        self.conv5.build(tf.TensorShape([None, 13, 13, 384]))
        self.conv5.set_weights(conv5_weights)
        self.fc6.build(tf.TensorShape([None, 9216]))
        self.fc6.set_weights(weights['fc6'])
        self.fc7.build(tf.TensorShape([None, 4096]))
        self.fc7.set_weights(weights['fc7'])
        print("Finish feeding weights!")


class SVM(tf.keras.models.Model):
    def __init__(self, seed=None, name=None):
        super(SVM, self).__init__(name=name)
        self.weight = tf.Variable(tf.random.normal([4096, 1], mean=0.0, stddev=1.0, dtype=tf.float32, seed=seed),
                                  dtype=tf.float32, name="weight")
        self.bias = tf.Variable(tf.random.normal([1], mean=0.0, stddev=1.0, dtype=tf.float32, seed=seed),
                                  dtype=tf.float32, name="bias")

    def call(self, inputs):
        return tf.add(tf.matmul(inputs, self.weight), self.bias)

class SVMLoss(tf.Module):
    def __init__(self, regularization_parameter = 1., name=None):
        super(SVMLoss, self).__init__(name=name)
        self.coefficient = regularization_parameter
        self.hinge = tf.keras.losses.Hinge(reduction=tf.keras.losses.Reduction.SUM, name='hinge')

    def __call__(self, y_true, y_pred, weight):
        regularization_loss = 0.5 * tf.reduce_sum(tf.square(weight))
        hinge_loss = self.hinge(y_true, y_pred)
        return regularization_loss + self.coefficient * hinge_loss