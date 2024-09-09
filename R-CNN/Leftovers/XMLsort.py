import os
import xml.etree.ElementTree as Et

def _numerate(literal_class):
    """
    Convert literal classes into certain numbers.
    :param literal_class: given numpy array which contains literal object classes
    :return: numpy array with int value
    """
    return ['person','bird', 'cat', 'cow', 'dog', 'horse', 'sheep', 'aeroplane',
            'bicycle', 'boat', 'bus', 'car', 'motorbike', 'train', 'bottle', 'chair',
            'diningtable', 'pottedplant','sofa', 'tvmonitor'].index(literal_class) + 1

def extract_dataset(dataset_path):
    """
    extract information from annotation dataset.
    :param dataset_path:
    :return:
    """
    IMAGE_FOLDER = "JPEGImages"
    ANNOTATIONS_FOLDER = "Annotations"

    ann_root, ann_dir, ann_files = next(os.walk(os.path.join(dataset_path, ANNOTATIONS_FOLDER)))
    img_root, img_dir, img_files = next(os.walk(os.path.join(dataset_path, IMAGE_FOLDER)))

    dataset_info = {}
    for xml_file in ann_files:
        assert os.path.join(xml_file.split(".")[0]+".jpg") in img_files,\
            "There isn't any image corresponding to the annotation, {}.".format(xml_file)

        xml = open(os.path.join(ann_root, xml_file), "r")
        tree = Et.parse(xml)
        root = tree.getroot()

        _objs_in_image = []
        for _obj in root.findall("object"):
            bndbox = _obj.find("bndbox")
            _objs_in_image.append([[int(bndbox.find("xmin").text), int(bndbox.find("ymin").text),
                                    int(bndbox.find("xmax").text), int(bndbox.find("ymax").text)],
                                   _numerate(_obj.find("name").text)])
        dataset_info[os.path.join(img_root, xml_file.split(".")[0]+".jpg")] = _objs_in_image
    return dataset_info

data_array = extract_dataset('C:\\Pascal VOC 2012\\VOC_train_val2012\\VOCdevkit\\VOC2012')

for i in data_array.keys():
    print(i)
    print(data_array[i])