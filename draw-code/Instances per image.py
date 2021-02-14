#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : Instances per image.py
# @description    ：Use a line graph to represent the number of instances per image

import os
import numpy as np
import matplotlib.pyplot as plt

def main():

    root = '\DataStatistics'  # your own path
    file_path = os.path.join(root, r'DrawingData\Instances per image.csv')
    save_path = os.path.join(root, r'Pictures\Instances per image.jpg')

    x1, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8 = np.loadtxt(file_path, encoding='utf-8-sig',
                                                            delimiter=',', skiprows=2, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8), unpack=True)
    co_aver = round((y_2[1]/y_2[0]), 1)
    voc_aver = round((y_4[1]/y_4[0]), 1)
    city_aver = round((y_6[1]/y_6[0]), 1)
    part_aver = round((y_8[1]/y_8[0]), 1)

    y3 = y_1/y_2[0]
    y2 = y_3/y_4[0]
    y1 = y_5/y_6[0]
    y4 = y_7/y_8[0]

    fontdict = {'family': 'Times New Roman', 'size': 12}
    plt.figure('折线图', figsize=(15, 9), facecolor='None')
    plt.title('Instances per image', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.grid(linestyle='-.', axis='y')
    plt.xlabel('Number of instances', fontdict=fontdict)
    plt.ylabel('Percentage of images', fontdict=fontdict)

    area = np.pi * 6 ** 2

    plt.xlim((0, 36))
    plt.ylim((0, 0.5))

    my_x_ticks = np.arange(0, 36, 1)
    my_y_ticks = np.arange(0, 0.51, 0.1)
    x_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19',  '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35']
    y_name = ['0', '10%', '20%', '30%', '40%', '50%']
    plt.xticks(my_x_ticks, x_name, rotation=0, fontproperties='Times New Roman', fontsize=12)
    plt.yticks(my_y_ticks, y_name, fontproperties='Times New Roman', fontsize=12)

    plt.scatter(x1, y3, s=area, c='red', marker='s', alpha=0.6, label='MS COCO({})'.format(co_aver))
    plt.scatter(x1, y1, s=area, c='blue', marker='^', alpha=0.6, label='Cityscapes({})'.format(city_aver))
    plt.scatter(x1, y4, s=area, c='orange', marker='*', alpha=0.6, label='PASCAL-Part({})'.format(part_aver))
    plt.scatter(x1, y2, s=area, c='green', marker='o', alpha=0.6, label='PASCAL VOC2012({})'.format(voc_aver))

    plt.plot(x1, y1, '-', c='blue', marker='^', ms=10)
    plt.plot(x1, y2, '-', c='green', marker='o', ms=10)
    plt.plot(x1, y3, '-', c='red', marker='s', ms=10)
    plt.plot(x1, y4, '-', c='orange', marker='*', ms=10)

    plt.legend(prop=fontdict)
    plt.tight_layout()
    plt.savefig(save_path, dpi=600)
    plt.show()


if __name__ == '__main__':
    main()
