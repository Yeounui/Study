import os
import xml.etree.ElementTree as ET
import numpy as np
import tensorflow as tf


def BoxDetection(path_list):
    print("Initiate Box data extraction.")
    Preset = tf.TensorArray(tf.int32, size=0, dynamic_size=True, infer_shape=False)
    prp_path, _, prp_files = next(iter(os.walk(os.path.join(path_list[0], path_list[2]))))
    for IMGCount, prp_file in enumerate(prp_files):
        GroundTruthArray = tf.TensorArray(tf.int32, size=0, dynamic_size=True)

        filename = prp_file.split(".")[0]
        tree = ET.parse(open(os.path.join(path_list[0], path_list[1], filename + ".xml"), "r"))
        root = tree.getroot()

        for i, _obj in enumerate(root.findall("object")):
            bndbox = _obj.find("bndbox")
            GroundTruthArray.write(i, tf.constant([int(bndbox.find("ymin").text), int(bndbox.find("xmin").text),
                                                   int(bndbox.find("ymax").text),
                                                   int(bndbox.find("xmax").text)])).mark_used()
        GroundTruth = GroundTruthArray.stack()
        GroundTruthArray.close()
        Proposal = tf.constant(np.load(os.path.join(prp_path, prp_file)))
        Label = tf.math.greater_equal(tf.reduce_max(_IOU(Proposal, GroundTruth), axis=1, keepdims=True),
                                      tf.constant(0.5))
        ImageNum = tf.fill([Proposal.get_shape()[0], 1], IMGCount)
        Preset.write(IMGCount, tf.concat([ImageNum, Proposal, tf.cast(Label, tf.int32)], axis=1)).mark_used()
        if (IMGCount + 1) % 2000 == 0:
            print("{} data are mounted.".format(IMGCount + 1))
    Preset = Preset.concat()
    print(Preset)
    print("Finish dataset preparation.")
    return Preset

@tf.function(experimental_relax_shapes=True)
def _IOU(Proposal, GroundTruth, epsilon=1e-7):
    Proposal = tf.cast(tf.reshape(Proposal, [-1, 4]), dtype=tf.float32)
    GroundTruth = tf.cast(tf.reshape(GroundTruth, [-1, 4]), dtype=tf.float32)

    pr_ymin, pr_xmin, pr_ymax, pr_xmax = tf.split(Proposal, 4, axis=1)
    gt_ymin, gt_xmin, gt_ymax, gt_xmax = tf.split(GroundTruth, 4, axis=1)

    intersect_ymin = tf.math.maximum(pr_ymin, tf.reshape(gt_ymin, [1, -1]))
    intersect_xmin = tf.math.maximum(pr_xmin, tf.reshape(gt_xmin, [1, -1]))
    intersect_ymax = tf.math.minimum(pr_ymax, tf.reshape(gt_ymax, [1, -1]))
    intersect_xmax = tf.math.minimum(pr_xmax, tf.reshape(gt_xmax, [1, -1]))

    width = intersect_xmax - intersect_xmin
    height = intersect_ymax - intersect_ymin

    width = tf.where(tf.math.less(width, tf.constant(0.0)), tf.constant(0.0), width)
    height = tf.where(tf.math.less(height, tf.constant(0.0)), tf.constant(0.0), height)

    interArea = width * height

    box_pr = (pr_ymax - pr_ymin) * (pr_xmax - pr_xmin)
    box_gt = (gt_ymax - gt_ymin) * (gt_xmax - gt_xmin)

    return tf.math.divide(interArea,
                          tf.math.add(tf.math.subtract(tf.math.add(box_pr,
                                                                   tf.reshape(box_gt, [1, -1])),
                                                       interArea),
                                      epsilon))


def _BoxNormalization(boxes, img_size):
    return tf.math.divide(boxes, tf.cast(tf.tile(img_size[1:3], [2]), tf.float32))


class RawBatchProcessing:
    def __init__(self, path_list):
        """
        convert image root and file list to tensor in advance.
        :param path_list: List of two elements: Parent path and Image folder
        """
        IMGRoot, _, IMGFiles = next(os.walk(os.path.join(*path_list)))
        self.IMGRoot = tf.convert_to_tensor(IMGRoot, tf.string)
        self.IMGFiles = tf.convert_to_tensor(IMGFiles, tf.string)

    def __call__(self, Batch):
        """
        convert raw batch to image batch and one hot label.
        :param Batches:
        :return: image batch train_x and its label train_y
        """
        ImageNum = Batch[:, 0]
        Boxes = tf.cast(Batch[:, 1:-1], dtype=tf.float32)
        Label = Batch[:, -1]

        batch_x = tf.zeros(ImageNum.get_shape() + [227, 227, 3])
        Selected_image, BoxLoci = tf.unique(ImageNum)

        @tf.function
        def __processing(batch_x, IMGRoot, IMGFile):
            IMGPath = tf.strings.join([IMGRoot, IMGFile], separator=os.sep)
            IMGTensor = tf.io.decode_jpeg(tf.io.read_file(IMGPath))[None, ...]
            BoxLociBoolean = tf.math.equal(ImageNum, IMG_dealt)
            NormalizedSelectedBoxes = _BoxNormalization(tf.boolean_mask(Boxes, BoxLociBoolean, axis=0),
                                                        tf.shape(IMGTensor))
            CroppedIMGs = tf.image.crop_and_resize(image=IMGTensor, boxes=NormalizedSelectedBoxes,
                                                   box_indices=tf.zeros(tf.shape(NormalizedSelectedBoxes)[0],
                                                                        dtype=tf.int32),
                                                   crop_size=(227, 227), method='bilinear')
            UpdateLoci = tf.where(BoxLociBoolean)
            batch_x = tf.tensor_scatter_nd_add(batch_x, UpdateLoci, CroppedIMGs)
            return batch_x

        for IMG_dealt in Selected_image:
           batch_x = __processing(batch_x, self.IMGRoot, self.IMGFiles[IMG_dealt])

        batch_x = tf.image.per_image_standardization(batch_x)
        batch_y = tf.one_hot(Label, 2, dtype=tf.float32)

        return batch_x, batch_y


def ValidationSplit(DataTensor, seed):
    PosShuffle = tf.random.shuffle(
                        tf.boolean_mask(DataTensor,
                                        tf.math.equal(DataTensor[:, -1], 1),
                                        axis=0),
                        seed=seed)
    NegShuffle = tf.random.shuffle(
                        tf.boolean_mask(DataTensor,
                                        tf.math.equal(DataTensor[:, -1], 0),
                                        axis=0),
                        seed=seed)
    PosVal, PosTrain = PosShuffle[:32, ...], PosShuffle[32: , :]
    NegVal, NegTrain = NegShuffle[:100, ...], NegShuffle[100: , :]
    return PosTrain, NegTrain, PosVal, NegVal

@tf.function
def ObjectClassification(path_list, training_class):
    def Dir(path_list):
        DATA_PATH, ANN_Folder = path_list[0].numpy(), path_list[1].numpy()
        ANNRoot, _, ANNFiles = next(iter(os.walk(os.path.join(DATA_PATH, ANN_Folder))))
        IMGAmount = tf.constant(len(ANNFiles))
        ANNRoot = tf.convert_to_tensor(ANNRoot, tf.string)
        ANNFiles = tf.convert_to_tensor(ANNFiles, tf.string)
        path_list = tf.convert_to_tensor(path_list, tf.string)
        return ANNRoot, ANNFiles, IMGAmount, path_list

    ANNRoot, ANNFiles, IMGAmount, path_list = tf.py_function(Dir, [path_list,], [tf.string, tf.string, tf.int32, tf.string])

    Preset = tf.TensorArray(tf.int32, size=0, dynamic_size=True,
                            infer_shape=False, element_shape= [None, 6])
    PresetCount = 0
    for IMGCount in tf.range(IMGAmount):
        ANNFile = ANNFiles[IMGCount]
        ANNPath = tf.strings.join([ANNRoot, ANNFile], separator=os.sep)

        def ANNExtraction(ANNPath, ANNFile, path_list):
            tree = ET.parse(open(ANNPath.numpy(), "r"))
            root = tree.getroot()
            GroundTruth = []
            for _obj in root.findall("object"):
                if numerate(_obj.find("name").text) == training_class:
                    bndbox = _obj.find("bndbox")
                    GroundTruth.append(tf.constant([int(bndbox.find("ymin").text), int(bndbox.find("xmin").text),
                                                    int(bndbox.find("ymax").text), int(bndbox.find("xmax").text),
                                                    1]))

            Proposal_path = tf.strings.join([path_list[0], path_list[2],
                                             tf.strings.join([tf.strings.split(ANNFile, sep='.')[0],
                                                              tf.constant(".npy")])],
                                            separator=os.sep)
            Proposal = np.load(Proposal_path.numpy().decode('utf-8'))

            if len(GroundTruth) != 0:
                return Proposal, tf.reshape(tf.concat(GroundTruth, axis=0), tf.constant([-1, 5]))
            else:
                return Proposal, tf.constant([[-1, ], ])

        Proposal, GroundTruth = tf.py_function(ANNExtraction, [ANNPath, ANNFile, path_list], [tf.int32, tf.int32])
        if tf.shape(GroundTruth)[1] == 5:
            NegBoolean = tf.math.reduce_all(tf.math.less(_IOU(Proposal, GroundTruth[:, :4]), tf.constant(0.3)), axis=1)
            NegProposal = tf.boolean_mask(Proposal, NegBoolean, axis=0)
            NegLabel = tf.fill([tf.shape(NegProposal)[0]], 0)[:, None]
            NegBoxLabel = tf.concat([NegProposal, NegLabel], axis=1)
            AllBoxLabel = tf.concat([NegBoxLabel, GroundTruth], axis=0)
            ImageNum = tf.fill([tf.shape(AllBoxLabel)[0]], IMGCount)[:, None]
            IBL = tf.concat([ImageNum, AllBoxLabel], axis=1)
            Preset = Preset.write(PresetCount, IBL)
            PresetCount += 1
        if (IMGCount + 1) % 2000 == 0:
            tf.print(IMGCount+1, " data are mounted.")
    result = Preset.concat()
    tf.print(result)
    tf.print("Finish dataset preparation.")
    return result


def numerate(literal_class):
    return ['person', 'bird', 'cat', 'cow', 'dog', 'horse', 'sheep', 'aeroplane',
            'bicycle', 'boat', 'bus', 'car', 'motorbike', 'train', 'bottle', 'chair',
            'diningtable', 'pottedplant', 'sofa', 'tvmonitor'].index(literal_class.lower()) + 1