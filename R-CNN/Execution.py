import os
import tensorflow as tf

import Model_low
from SelectiveSearch import SelectiveSearch


#Subject
img =

#trained model directory
model =

#SVM directories.
SVM_dir = {'person': "",
           'bird': "",
           'cat': "",
           'cow': "",
           'dog': "",
           'horse': "",
           'sheep': "",
           'aeroplane': "",
           'bicycle': "",
           'boat': "",
           'bus': "",
           'car': "",
           'motorbike': "",
           'train': "",
           'bottle': "",
           'chair': "",
           'diningtable': "",
           'pottedplant': "",
           'sofa': "",
           'tvmonitor': ""}

#Generating sequences.
ProposalGather= SelectiveSearch(min_area=9)

ObjectDetection = Model_low.AlexNet()
ObjectDetection.load_weights(model)

for class_name in SVM_dir.keys():
    Model_low.SVM(name=class_name).load_weights(SVM_dir[class_name])

#Execution
proposals= ProposalGather.execute(img, 2000)
probs = ObjectDetection(proposals)

detected = tf.boolean_mask(proposals, tf.greater_equal(probs, tf.constant([0.5])))




