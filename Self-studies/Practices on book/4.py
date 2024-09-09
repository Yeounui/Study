import numpy as np
import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

housing = fetch_california_housing()
m, n = housing.data.shape

"""
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing.data] # adding bias on housing data

X= tf.constant(housing_data_plus_bias, dtype=tf.float32, name = 'X')
y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name = "y")
XT = tf.transpose(X)
theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)

with tf.Session() as sess:
    theta_value = theta.eval()
print(theta_value)
"""

n_epochs = 1000
learning_rate = 0.01

scaler = StandardScaler()
scaled_housing_data = scaler.fit_transform(housing.data)
scaled_housing_data_plus_bias = np.c_[np.ones((m, 1)), scaled_housing_data]

X = tf.constant(scaled_housing_data_plus_bias, dtype=tf.float32, name='X')
y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name='y')
theta = tf.Variable(tf.random_uniform([n + 1, 1], -1.0, 1.0), name='theta')
y_pred = tf.matmul(X, theta, name='predictions')
error = y_pred - y
mse = tf.reduce_mean(tf.square(error), name="mse")
optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)
#gradients = tf.gradients(mse, [theta])[0]
#gradients = 2/m * tf.matmul(tf.transpose(X), error)
training_op = optimizer.minimize(mse)
#training_op = tf.assign(theta, theta - learning_rate * gradients)
# Meaning "theta = theta - learning_rate * gradient", however Tensorflow are computed by pointer, so that assign command
# is needed.

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(n_epochs):
        if epoch % 100 == 0:
            print("Epoch", epoch, "MSE =", mse.eval())
        sess.run(training_op)

    best_theta = theta.eval()
print(best_theta)