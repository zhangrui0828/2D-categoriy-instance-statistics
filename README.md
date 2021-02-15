## 语义分割常用数据集信息统计

本项目介绍了常用的语义分割数据集：SIFT-flow(2009)，PASCAL VOC2012(2012)，PASCAL-Part(2014) ，MS COCO(2014)，Cityscapes(2015)的统计信息。

### 数据集

数据集官方下载地址：

- SIFT-flow(2009) ：http://www.cs.unc.edu/~jtighe/Papers/ECCV10/

- PASCAL VOC2012(2012) ：http://host.robots.ox.ac.uk/pascal/VOC/voc2012/
- PASCAL-Part(2014)：http://roozbehm.info/pascal-parts/pascal-parts.html
- PASCAL-Context(2010)： https://cs.stanford.edu/~roozbeh/pascal-context/
- MS COCO(2014)：https://cocodataset.org/
- Cityscapes(2015)：https://www.cityscapes-dataset.com/

###  代码使用

#### 需要的库

- pyhon
- json
- tqdm
- scipy
- xml
- numpy
- matplotlib

#### 统计代码

统计数据集信息用到的代码存储在文件[StatisticalCode](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-code)中,要使用此代码，您只需更改代码中对应的文件路径。

- SIFT-flow.py

  简单更改root路径为SIFI-flow数据集中分割标签（semanticlabels）在您的电脑中的路径即可。

- VOC2012.py

  简单更改main函数中root和file_path为您自己的路径。

- PASCAL-Part.py

  由于此数据集的注释信息存储在mat文件中，您需要先调用PASCAL-Part.m文件生成含有每张图片实例信息的instances.txt文件，并把这个文件输入到python程序中去。

- PASCAL-Context.py

  简单更改root路径为PASCAL-Context数据集在您的电脑中的路径即可。

- MS COCO.py

  由于COCO数据集中训练集（train）和验证集（val）在不同的文件中，您需要分别将这两个文件(instances_train2014.json, instances_val2014.json)输入到程序中去，并把两次得到的结果自己相加。由于数据集比较大，程序可能会花费较长的时间。

- Cityscapes.py

  因为存储有标注信息的json文件分别存放在Cityscapes数据集gtFine/中不同的文件夹下， 您需要自己将他们提取到一个文件夹中，把程序中file_dir更改为这个文件夹路径。您可以在main函数中的labels列表中设置您感兴趣的类进行统计。

#### 绘图代码

绘图用到的代码存储在文件[DrawingCode](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/draw-code)中,要使用此代码，您需要为每一个python脚本配置数据文件，这些数据以CSV格式存储在[DrawingData](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-data)文件中。

- Images per category.py

- Instances per category.py

- images per category of cityscapes.py

- instance per category of cityscapes.py

- Images per category of  SIFT-flow.py

- Images per category of PASCAL-Context.py

- Number of categories vs Number of instances.py

- Categories per image.py

- Instances per image.py

  由于每个统计图样式和输入数据不一样，所以每一个代码对应一张统计图，要使用此代码，您需要将统计出来的数据整理后存放在[DrawingData](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-data)文件下对应的CSV文件中，并简单更改此代码中root为您自己的路径。

### 统计图

利用统计信息绘出的图存放在[Pictures](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/pictures)文件夹中，一共八张图片，包含每个数据集每一类实例数和每一类图片数的柱状图，类数与实例数的散点图，以及每一张图片包含的类数和实例数的折线图。其中由于SIFI-flow数据集没有实例信息，其没有与实例信息相关的图。

### 关于作者

作者：

如果您有任何问题，欢迎在讨论区讨论。
