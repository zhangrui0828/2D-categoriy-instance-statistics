#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : MS COCO.py
# @description  ：This code statistics information about MS COCO(2017) datasets

import json
from tqdm import tqdm

def main():
    json_file = r"\annotations_trainval2014\annotations\instances_val2014.json"  # modify to your own path

    data = json.load(open(json_file, 'r'))

    data_2={}
    data_2['info'] = data['info']
    data_2['licenses'] = data['licenses']

    data_2['images'] = [data['images'][i] for i in range(len(data['images']))]
    data_2['categories'] = data['categories']

    images_per = [0 for i in range(100)]
    instances_per = [0 for i in range(100)]

    classes_perimage = [0 for i in range(200)]
    instance_perimage = [0 for i in range(200)]
    num_instances = 0

    # Find all of its objects through the imgID
    for i in tqdm(range(len(data_2['images']))):
        annotation = []
        instance_list = []


        imgID=data_2['images'][i]['id']
        for ann in data['annotations']:
            if ann['image_id'] == imgID:
                annotation.append(ann)
                instance_list.append(ann['category_id'])

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

    print("The class name and its ID:")
    print(data_2['categories'])


if __name__ == '__main__':
    main()

