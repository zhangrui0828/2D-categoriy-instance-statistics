#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : Categories per image.py
# @description    ：Use a line graph to represent the number of classes per image

import os
import numpy as np
import matplotlib.pyplot as plt


# Calculate the average number of classes per image
def aver(data):
    num_sum = 0
    for i in range(len(data)):
        num_sum = num_sum + data[i] * (i + 1)
    avera = round((num_sum / sum(data)), 1)
    return avera


def main():

    root = '\DataStatistics'  # your own path
    file_path = os.path.join(root, r'DrawingData\Categories per image.csv')
    save_path = os.path.join(root, r'Pictures\Categories per image.jpg')

    x1, y1, y2, y3, y4, y5, y6 = np.loadtxt(file_path, encoding='utf-8-sig',
                                        delimiter=',', skiprows=2, usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True)
    y1_aver = aver(y1)
    y2_aver = aver(y2)
    y3_aver = aver(y3)
    y4_aver = aver(y4)
    y5_aver = aver(y5)
    y6_aver = aver(y6)

    y1 = y1/sum(y1)
    y2 = y2/sum(y2)
    y3 = y3/sum(y3)
    y4 = y4/sum(y4)
    y5 = y5/sum(y5)
    y6 = y6/sum(y6)

    fontdict = {'family': 'Times New Roman', 'size': 12}
    plt.figure('line chart', figsize=(15, 9), facecolor='None')

    plt.title('Categories per image', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.grid(linestyle='-.', axis='y')

    plt.xlabel('Number of categories', fontdict=fontdict)
    plt.ylabel('Percentage of images', fontdict=fontdict)

    area = np.pi * 6 ** 2

    plt.xlim((0, 31))
    plt.ylim((0, 0.7))

    my_x_ticks = np.arange(0, 31, 1)
    my_y_ticks = np.arange(0, 0.8, 0.1)
    y_name = ['0', '10%', '20%', '30%', '40%', '50%', '60%', '70%']
    plt.xticks(my_x_ticks, rotation=0, fontproperties='Times New Roman', fontsize=12)
    plt.yticks(my_y_ticks, y_name, fontproperties='Times New Roman', fontsize=12)

    plt.scatter(x1, y5, s=area, c='purple', marker='p', alpha=0.6, label='SIFT-flow({})'.format(y5_aver))
    plt.scatter(x1, y1, s=area, c='red', marker='s', alpha=0.6, label='MS COCO({})'.format(y1_aver))
    plt.scatter(x1, y3, s=area, c='blue', marker='^', alpha=0.6, label='Cityscapes({})'.format(y3_aver))
    plt.scatter(x1, y4, s=area, c='orange', marker='*', alpha=0.6, label='PASCAL-Part({})'.format(y4_aver))
    plt.scatter(x1, y2, s=area, c='green', marker='o', alpha=0.6, label='PASCAL VOC2012({})'.format(y2_aver))
    plt.scatter(x1, y6, s=area, c='cornflowerblue', marker='+', alpha=0.6, label='PASCAL-Context({})'.format(y6_aver))

    plt.plot(x1, y1, '-', c='red', marker='s', ms=10)
    plt.plot(x1, y2, '-', c='green', marker='o', ms=10)
    plt.plot(x1, y3, '-', c='blue', marker='^', ms=10)
    plt.plot(x1, y4, '-', color='orange', marker='*', ms=10)
    plt.plot(x1, y5, '-', color='purple', marker='p', ms=10)
    plt.plot(x1, y6, '-', color='cornflowerblue', marker='+', ms=10)

    plt.legend(prop=fontdict)
    plt.tight_layout()
    plt.savefig(save_path, dpi=600)
    plt.show()


if __name__ == '__main__':
    main()
