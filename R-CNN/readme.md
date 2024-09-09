# R-CNN

Implementation of **R-CNN** model from the paper below,

>   Girshick, R., Donahue, J., Darrell, T., & Malik, J. (2014). Rich feature hierarchies for accurate object detection and semantic segmentation. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 580-587).


The model is a classic model for object detection and sementatic segmentation. Since the source code is gone, the code is based on description as the paper explained.

The model is divided into three segments: Selective Search, AlexNet, and Support Vector Machine(SVM).

1. Selective search proposes category-independent regions via offering coordinates of bounding boxes. 2000 images in each bounding boxes are fed into AlexNet.

>   Uijlings, J.R.R., van de Sande, K.E.A., Gevers, T. et al. Selective Search for Object Recognition. Int J Comput Vis 104, 154–171 (2013). https://doi.org/10.1007/s11263-013-0620-5

2. According to the suggestion of Selective search, bound images are warped to 227 X 227 size. This images are passed to the pretrained AlexNet, which is pruned at 8th softmax layer.

>   Krizhevsky, A., Sutskever, I., & Hinton, G.E. (2012). ImageNet classification with deep convolutional neural networks. Communications of the ACM, 60, 84 - 90.

Weights earned [here](https://github.com/yiling-chen/view-finding-network/blob/master/alexnet.npy).

3. The output features are connected to a set of SVMs. Each SVMs corresponds to each category of an object to classify whether the bound image is in the category or not.

> M. A. Hearst, S. T. Dumais, E. Osuna, J. Platt and B. Scholkopf, "Support vector machines," in IEEE Intelligent Systems and their Applications, vol. 13, no. 4, pp. 18-28, July-Aug. 1998, doi: 10.1109/5254.708428.


## What is it?

+ Dependencies: Numpy, Matlibplot, OpenCV, Tensorflow 2.x
### Files

+ **SelectiveSearch.py** : Selective search of OpenCV is used.
+ **Train_1.py** : Extracts coordinates of bounding boxes and stores as numpy files in local directories.
___
+ **Dataflow.py** : A set of functions to process images.   

>   _BoxDectection_ : Labels bound images based on IoU score comparing ground truth and outputs from Selective search.   

>   _RawBatchProcessing_ : Crops and resizes images to 227 X 227 according to extracted coordinates.   

>   _ValidationSplit_: Aligns subset of data for validation during training.

>   _ObjectClassification_: Generates collected dataset which is a set of warped image tensors and labels.
___
+ **Model_low.py** : AlexNet and SVM are implemented, pretrained weights from npy file can be adjusted via _feed_pretrained_.
+ **Train_3.py** : Actual training step.
___
+ **Execution.py** : To use trained model.
+ **TrueDetectionDisplay.py** : Shows a cropped image from ground truths. 
___
### Leftovers

+ **Train_2.py** : Trials to introduce weights of AlexNet from npy file.

+ **XMLsort.py, XML.parsing, XMLtoTFRecord.py** : Trials to mount data.