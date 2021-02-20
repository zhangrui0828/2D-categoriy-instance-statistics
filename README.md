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

  Since the training set  and validation set in the COCO dataset are in separate files, you need to input the two files (instances_train2014.json, instances_val2014.json) into the program separately and add the results. Due to the large dataset, the program may take a long time.

- Cityscapes.py

  Because the JSON files that store the annotation information are stored in different folders in the Cityscapes dataset gtFine/, you need to extract them into a folder yourself and change the file_dir in the program to this folder path. You can set the class you are interested in to count on the labels list in the main function.

#### Draw-code

Drawing code stored in [draw-code](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/draw-code), you need for each python script configurine data file.The data is stored in CSV format in [statistics-data](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-data).

- Images per category.py

- Instances per category.py

- images per category of cityscapes.py

- instance per category of cityscapes.py

- Images per category of  SIFT-flow.py

- Images per category of PASCAL-Context.py

- Number of categories vs Number of instances.py

- Categories per image.py

- Instances per image.py

  Since the style of each statistic chart and input data is different, each code corresponds to a statistic graph. To use this code, you need to organize the statistical data and store them in [statistics-data](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/statistics-data), and simply change the root in this code to your own path.

#### Statistical-chart

  Graphs drawn using statistical information are stored in [statistical-chart](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/tree/main/pictures). There are nine chart, contain bar charts about the number of instances and images of each class in each dataset, scatter charts about the number of classes and instances, and line charts about the number of classes and instances contained in each image. Since there is no instance information in the SIFI-flow dataset and PASCAL-Context dataset, there is no graph related to instance information.For examples:
  
 ![Categories per image.jpg](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/blob/main/statistical-chart/Categories%20per%20image.jpg)
 
 ![Images per category.jpg](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/blob/main/statistical-chart/Images%20per%20category.jpg)
 
 ![Number of categories vs Number of instances.jpg](https://github.com/zhangrui0828/2D-categoriy-instance-statistics/blob/main/statistical-chart/Number%20of%20categories%20vs%20Number%20of%20instances.jpg)

### About

If you have any questions, please feel free to discuss in the issues.
