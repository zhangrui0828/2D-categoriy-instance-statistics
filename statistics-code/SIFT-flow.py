#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : SIFT-flow.py
# @description  ：This code statistics information about SIFT-flow datasets

import os
from scipy.io import loadmat
from tqdm import tqdm


def get_files(file_dir):
    files = []
    for file in os.listdir(file_dir):
        files.append(os.path.join(file_dir, file))
    return files


def main():
    root = r"\SiftFlowDataset\SemanticLabels\spatial_envelope_256x256_static_8outdoorcategories"  # modify to your own path

    image_list = get_files(root)

    images_perclass = [0 for i in range(35)]
    classes_per = [0 for i in range(35)]

    for image in tqdm(image_list):
        m = loadmat(image)
        m_list = m['S'].flatten()

        classes_set = set(m_list)
        classes_list = list(classes_set)

        if 0 in classes_list:
            classes_list.remove(0)

        classes_len = len(classes_list)
        if classes_len == 0:
            print(image)

        for ind in classes_list:
            images_perclass[ind] = images_perclass[ind] + 1

        classes_per[classes_len] = classes_per[classes_len] + 1

    print()
    print("Number of images per category(index is classID, value is number of images):")
    print(sum(images_perclass), images_perclass)

    print("Number of categories per image(index is number of categories in an image, value is number of images):")
    print(sum(classes_per), classes_per)


if __name__ == '__main__':
    main()
