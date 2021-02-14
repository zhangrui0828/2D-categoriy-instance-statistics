#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : VOC2012.py
# @description  ：This code statistics information about PASCAL VOC2012 datasets

import os
import xml.etree.ElementTree as ET
from tqdm import tqdm


def get_flpth(filename):
    file_list = open(filename, "r")
    file_list = [id_.rstrip() for id_ in file_list]
    return file_list


def main():
    root = r"\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\Annotations"   # modify to your own path
    filename = r"\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\ImageSets\Main\trainval.txt"

    labels = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
              "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

    file_list = get_flpth(filename)

    images_perclass = [0 for i in range(21)]
    object_perclass = [0 for i in range(21)]

    classes_per = [0 for i in range(60)]
    instance_per = [0 for i in range(60)]

    num_instance = 0

    for flname in tqdm(file_list):
        flname = flname + ".xml"
        filpth = os.path.join(root, flname)
        tree = ET.parse(filpth)
        roots = tree.getroot()

        instance_list = []

        for inflection_name in roots.iter('object'):
            target = inflection_name.find('name').text
            index = labels.index(target)

            instance_list.append(index)
        instance_len = len(instance_list)
        num_instance = num_instance + instance_len

        classes_set = set(instance_list)
        classes_list = list(classes_set)
        classes_len = len(classes_list)

        for ind in classes_list:
            images_perclass[ind] = images_perclass[ind] + 1
        for ind in instance_list:
            object_perclass[ind] = object_perclass[ind] + 1

        classes_per[classes_len] = classes_per[classes_len] + 1
        instance_per[instance_len] = instance_per[instance_len] + 1

    print()
    print("Number of categories per image:", num_instance)

    print("Number of images per category(index is classID, value is number of images):")
    print(sum(images_perclass), images_perclass)
    print("Number of instances per category(index is classID, value is number of instances):")
    print(sum(object_perclass), object_perclass)

    print("Number of categories per image(index is number of categories in an image, value is number of images):")
    print(sum(classes_per), classes_per)
    print("Number of instances per image(index is number of instances in an image, value is number of images):")
    print(sum(instance_per), instance_per)


if __name__ == '__main__':
    main()

