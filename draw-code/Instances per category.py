#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : Instances per category.py
# @description    ：Use bar charts to represent the number of instances per category

import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    root = '\DataStatistics'  # your own path
    file_path = os.path.join(root, r'DrawingData\Instances per category.csv')
    save_path = os.path.join(root, r'Pictures\Instances per category.jpg')

    x1, y1, y2, y3 = np.loadtxt(file_path, delimiter=',', skiprows=2, usecols=(0, 1, 3, 5), unpack=True, dtype='U20,f8,f8,f8')

    fontdict = {'family': 'Times New Roman', 'size': 12}
    plt.figure('Bar Chart', figsize=(15, 9), facecolor='None')
    plt.title('Instances per category ', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.grid(linestyle='-.', axis='y')
    plt.xlabel('Per category', fontdict={'family': 'Times New Roman', 'size': 12})
    plt.ylabel('Instances per category', fontdict={'family': 'Times New Roman', 'size': 12})
    x = np.arange(x1.size)

    plt.bar(x, y1, 0.8, bottom=y2+y3, label='MS COCO', color='red')
    plt.bar(x, y3, 0.8, label='PASCAL-Part', color='orange')
    plt.bar(x, y2, 0.8, bottom=y3,  label='PASCAL VOC2012', color='green')

    plt.xticks(x, x1, rotation=90, fontproperties='Times New Roman', fontsize=12)
    plt.yticks(fontproperties='Times New Roman', fontsize=12)
    plt.ylim((100, 1000000))
    plt.yscale('log')
    plt.legend(prop=fontdict)
    plt.tight_layout()
    plt.savefig(save_path, dpi=600)
    plt.show()


if __name__ == '__main__':
    main()
