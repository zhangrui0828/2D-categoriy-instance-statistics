#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : Number of categories vs Number of instances.py
# @description ：A scatter plot is used to represent  the number of classes and the number of instances

import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    root = '\DataStatistics'  # your own path
    file_path = os.path.join(root, r'DrawingData\Number of categories vs Number of instances.csv')
    save_path = os.path.join(root, r'Pictures\Number of categories vs Number of instances.jpg')

    x1, y1, x2, y2, x3, y3, x4, y4 = np.loadtxt(file_path, encoding='utf-8-sig', delimiter=',', skiprows=2,
                                                usecols=(0, 1, 2, 3, 4, 5, 6, 7), unpack=True)

    fontdict = {'family': 'Times New Roman', 'size': 12}

    plt.figure('Scatter Chart', figsize=(15, 9), facecolor='None')
    plt.title('Number of categories vs Number of instances', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.grid(linestyle='-.', axis='y')

    plt.xlabel('Number of categories', fontdict=fontdict)
    plt.ylabel('Number of instances', fontdict=fontdict)

    area = np.pi * 9 ** 2

    plt.xlim((0, 110))
    plt.ylim((10, 10000000))
    my_x_ticks = np.arange(0, 111, 10)
    plt.yscale('log')
    plt.xticks(my_x_ticks, fontproperties='Times New Roman', fontsize=12)
    plt.yticks(fontproperties='Times New Roman', fontsize=12)

    plt.scatter(x1, y1, s=area, c='red', marker='s', alpha=0.6, label='MS COCO')
    plt.scatter(x3, y3, s=area, c='blue', marker='^', alpha=0.6, label='Cityscapes')
    plt.scatter(x4, y4, s=area, c='orange', marker='*', alpha=0.6, label='PASCAL-Part')
    plt.scatter(x2, y2, s=area, c='green', marker='o', alpha=0.6, label='PASCAL VOC2012')

    plt.legend(prop=fontdict)
    plt.tight_layout()
    plt.savefig(save_path, dpi=600)
    plt.show()


if __name__ == '__main__':
    main()
