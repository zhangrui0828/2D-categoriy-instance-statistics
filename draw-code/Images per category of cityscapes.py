#!/usr/bin/env python
# -*- coding:  utf-8 -*-
# @Time   : 2020/11/12
# @Author :
# @File   : Images per category of cityscapes.py
# @description    ：Use bar charts to represent the number of images per category of Cityscapes

import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    root = '\DataStatistics'  # your own path
    file_path = os.path.join(root, r'DrawingData\Images per category of cityscapes.csv')
    save_path = os.path.join(root, r'Pictures\Images per category of Cityscapes.jpg')

    x1, y1 = np.loadtxt(file_path, delimiter=',', skiprows=2, usecols=(0, 1), unpack=True, dtype='U20,f8')

    fontdict = {'family': 'Times New Roman', 'size': 12}
    plt.figure('Bar Chart', figsize=(15, 9), facecolor='None')
    plt.title('Images per category ', fontdict={'family': 'Times New Roman', 'size': 16})
    plt.grid(linestyle='-.', axis='y')
    plt.xlabel('Per category', fontdict=fontdict)
    plt.ylabel('Images per category', fontdict=fontdict)
    x = np.arange(x1.size)

    plt.bar(x, y1, 0.8,   label='Cityscapes', color='blue')

    plt.xticks(x, x1, rotation=90, fontproperties='Times New Roman', fontsize=12)
    plt.yticks(fontproperties='Times New Roman', fontsize=12)
    plt.ylim((1, 1000000))
    plt.yscale('log')

    plt.legend(prop=fontdict)
    plt.tight_layout()
    plt.savefig(save_path, dpi=600)
    plt.show()


if __name__ == '__main__':
    main()
