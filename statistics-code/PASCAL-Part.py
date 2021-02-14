#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : PASCAL-Person-Part.py
# @description  ：This code statistics information about PASCAL-Person-Part datasets

from tqdm import tqdm

def main():
    pth = r"\instances.txt"   # modify to your own path

    f = open(pth, "r")

    images_perclass = [0 for i in range(30)]
    object_perclass = [0 for i in range(30)]

    classes_per = [0 for i in range(60)]
    instance_per = [0 for i in range(60)]

    num_instance = 0

    for line in tqdm(f.readlines()):

        instance_list = [int(id) for id in line.split('*')[:-1]]

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
