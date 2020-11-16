#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : Cityscapes.py
# @description  ：This code statistics information about Cityscapes datasets

import os
import json
from tqdm import tqdm


def get_files(file_dir):
    files = []
    for file in os.listdir(file_dir):
        files.append(os.path.join(file_dir, file))
    return files


def main():
    file_dir = r"\cityscapesjson"  # The path that stores the Cityscapes JSON file

    labels = ['static', 'dynamic', 'ground', 'road', 'sidewalk', 'parking', 'rail track', 'building', 'wall',
              'fence', 'guard rail', 'bridge', 'tunnel', 'pole', 'polegroup', 'traffic light', 'traffic sign',
              'vegetation', 'terrain','sky', 'person', 'rider', 'car', 'truck', 'bus', 'caravan', 'trailer',
              'train', 'motorcycle', 'bicycle']

    files = get_files(file_dir)

    images_per = [0 for i in range(30)]
    instances_per = [0 for i in range(30)]

    classes_perimage = [0 for i in range(300)]
    instance_perimage = [0 for i in range(300)]
    num_instances = 0

    for file in tqdm(files):
        data = json.load(open(file, 'r'))
        object_list = data["objects"]

        instance_list = []

        for label in object_list:
            obj = label['label']
            if obj in labels:
                index = labels.index(obj)
                instance_list.append(index)

        classes_set = set(instance_list)
        classes_list = list(classes_set)

        for index in instance_list:
            instances_per[index] = instances_per[index] + 1
        for index in classes_list:
            images_per[index] = images_per[index] + 1

        clas_len = len(classes_list)
        inst_len = len(instance_list)

        classes_perimage[clas_len] = classes_perimage[clas_len] + 1
        instance_perimage[inst_len] = instance_perimage[inst_len] + 1
        num_instances = num_instances + inst_len

    print()
    print("Total number of instances:", num_instances)

    print("Number of images per category(index is classID, value is number of images):")
    print(sum(images_per), images_per)
    print("Number of instances per category(index is classID, value is number of instances):")
    print(sum(instances_per), instances_per)

    print("Number of categories per image(index is number of categories in an image, value is number of images):")
    print(sum(classes_perimage), classes_perimage)
    print("Number of instances per image(index is number of instances in an image, value is number of images):")
    print(sum(instance_perimage), instance_perimage)


if __name__ == '__main__':
    main()
