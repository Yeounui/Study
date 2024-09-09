import os
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as Et
from Dataflow import _IOU

from PIL import Image
from PIL import ImageDraw

def show_ground_truth(dataset_path, specific=None):

  IMAGE_FOLDER = "JPEGImages"
  ANNOTATIONS_FOLDER = "Annotations"

  if specific == None or []:
    ann_root, _, ann_files = next(os.walk(os.path.join(dataset_path, ANNOTATIONS_FOLDER)))
  else:
    ann_root = os.path.join(dataset_path, ANNOTATIONS_FOLDER)
    ann_files = [_img + '.xml' for _img in specific]

  for xml_file in ann_files:
    # XML파일와 이미지파일은 이름이 같으므로, 확장자만 맞춰서 찾습니다.
    img_name = os.path.join(xml_file.split(".")[0]+".jpg")
    img_file = os.path.join(dataset_path, IMAGE_FOLDER, img_name)
    image = Image.open(img_file).convert("RGB")
    draw = ImageDraw.Draw(image)

    xml = open(os.path.join(ann_root, xml_file), "r")
    tree = Et.parse(xml)
    root = tree.getroot()

    objects = root.findall("object")

    for _object in objects:
        name = _object.find("name").text
        bndbox = _object.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        ymin = int(bndbox.find("ymin").text)
        xmax = int(bndbox.find("xmax").text)
        ymax = int(bndbox.find("ymax").text)

        draw.rectangle(((xmin, ymin), (xmax, ymax)), outline="red")
        draw.text((xmin, ymin), name)

    plt.figure(figsize=(25,20))
    plt.imshow(image)
    plt.show()
    plt.close()

def show_proposal_rects(dataset_path, specific=None):
    IMAGE_FOLDER = "JPEGImages"
    ANNOTATIONS_FOLDER = "Annotations"
    PROPOSAL_FOLDER = "Proposals"

    if specific == None or []:
        ann_root, _, ann_files = next(os.walk(os.path.join(dataset_path, ANNOTATIONS_FOLDER)))
    else:
        ann_root = os.path.join(dataset_path, ANNOTATIONS_FOLDER)
        ann_files = [_img + '.xml' for _img in specific]

    for xml_file in ann_files:
        # XML파일와 이미지파일은 이름이 같으므로, 확장자만 맞춰서 찾습니다.
        img_name = os.path.join(xml_file.split(".")[0] + ".jpg")
        img_file = os.path.join(dataset_path, IMAGE_FOLDER, img_name)
        image = Image.open(img_file).convert("RGB")
        draw = ImageDraw.Draw(image)

        xml = open(os.path.join(ann_root, xml_file), "r")
        tree = Et.parse(xml)
        root = tree.getroot()

        objects = root.findall("object")

        Ground_Truth = []
        for _object in objects:
            name = _object.find("name").text
            bndbox = _object.find("bndbox")
            xmin = int(bndbox.find("xmin").text)
            ymin = int(bndbox.find("ymin").text)
            xmax = int(bndbox.find("xmax").text)
            ymax = int(bndbox.find("ymax").text)
            Ground_Truth.append([ymin, xmin, ymax, xmax])

            draw.rectangle(((xmin, ymin), (xmax, ymax)), outline="red")
            draw.text((xmin, ymin), name)
        Ground_Truth = np.concatenate(Ground_Truth, axis=0).reshape([-1, 4])

        npy_name = os.path.join(xml_file.split(".")[0] + ".npy")
        npy_file = os.path.join(dataset_path, PROPOSAL_FOLDER, npy_name)
        npy = np.load(npy_file)

        blues = npy[np.argmax(_IOU(npy, Ground_Truth), axis=0).reshape([npy.shape[0], 1]) >= 0.5]
        yellows = npy[np.argmax(_IOU(npy, Ground_Truth), axis=0) < 0.5]
        print(blues.shape, yellows.shape)
        for blue in blues:
            draw.rectangle(((blue[1], blue[0]),
                            (blue[3], blue[2])), outline="blue")
        for yellow in yellows:
            draw.rectangle(((yellow[1], yellow[0]),
                            (yellow[3], yellow[2])), outline="green")

        plt.figure(figsize=(25, 20))
        plt.imshow(image)
        plt.show()
        plt.close()

print(show_proposal_rects(dataset_path='C:\\Pascal VOC 2012\\VOC_train_val2012\\VOCdevkit\\VOC2012',
                        specific=['2011_003353', '2011_006777']))
#45.70000076293945, 281.70000076293945