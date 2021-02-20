## Semantic segmentation dataset information statistics

This repository introduces the statistics of commonly used semantic segmentation datasets: SIFT-flow(2009), PASCAL VOC2012(2012), PASCAL-Part(2014), PASCAL-Context(2010), MS COCO(2014), Cityscapes(2015).

### Dataset

Dataset download：

- SIFT-flow(2009) ：http://www.cs.unc.edu/~jtighe/Papers/ECCV10/
- PASCAL VOC2012(2012) ：http://host.robots.ox.ac.uk/pascal/VOC/voc2012/
- PASCAL-Part(2014)：http://roozbehm.info/pascal-parts/pascal-parts.html
- PASCAL-Context(2010)： https://cs.stanford.edu/~roozbeh/pascal-context/
- MS COCO(2014)：https://cocodataset.org/
- Cityscapes(2015)：https://www.cityscapes-dataset.com/

###  Usage

#### Requirements

- pyhon
- json
- tqdm
- scipy
- xml
- numpy
- matplotlib

#### Statistics-code

The code used for the statistical dataset information is stored in [statistics-code](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-code). You only need to change the corresponding file path in the code to use it.

- SIFT-flow.py

  Simply set the root path to the path of Semanticlabels in the SIFI-FLOW dataset on your computer.
  
- VOC2012.py

  Simply change the root and file_path in the main function to your own path.

- PASCAL-Part.py

  Since the annotation information for this data set is stored in the mat file, you need to first call the pascal-part.m file to generate the instances.txt file with the instance information for each image and input this file into the Python program.

- PASCAL-Context.py

  Simply change the root path to the path of the PASCAL-Context dataset on your computer.
  
- MS COCO.py

  由于COCO数据集中训练集（train）和验证集（val）在不同的文件中，您需要分别将这两个文件(instances_train2014.json, instances_val2014.json)输入到程序中去，并把两次得到的结果自己相加。由于数据集比较大，程序可能会花费较长的时间。

- Cityscapes.py

  因为存储有标注信息的json文件分别存放在Cityscapes数据集gtFine/中不同的文件夹下， 您需要自己将他们提取到一个文件夹中，把程序中file_dir更改为这个文件夹路径。您可以在main函数中的labels列表中设置您感兴趣的类进行统计。

#### Draw-code

绘图用到的代码存储在文件[draw-code](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/draw-code)中,要使用此代码，您需要为每一个python脚本配置数据文件，这些数据以CSV格式存储在[statistics-data](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-data)文件中。

- Images per category.py

- Instances per category.py

- images per category of cityscapes.py

- instance per category of cityscapes.py

- Images per category of  SIFT-flow.py

- Images per category of PASCAL-Context.py

- Number of categories vs Number of instances.py

- Categories per image.py

- Instances per image.py

  由于每个统计图样式和输入数据不一样，所以每一个代码对应一张统计图，要使用此代码，您需要将统计出来的数据整理后存放在[statistics-data](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-data)文件下对应的CSV文件中，并简单更改此代码中root为您自己的路径。

### Statistical-chart

利用统计信息绘出的图存放在[statistical-chart](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/pictures)文件夹中，一共九张图片，包含每个数据集每一类实例数和每一类图片数的柱状图，类数与实例数的散点图，以及每一张图片包含的类数和实例数的折线图。其中由于SIFI-flow数据集和PASCAL-Context数据集没有实例信息，其没有与实例信息相关的图。

### About

If you have any questions, please feel free to discuss in the issues.
