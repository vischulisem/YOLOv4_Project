#This script will use pre-annotated dataset from https://public.roboflow.com/ to train YOLOv4
#Tutorial from https://colab.research.google.com/drive/1mzL6WyY9BRx4xX476eQdhKDnd_eixBlG#scrollTo=KiCILEbs1NII

#First download yolov4 ConvNet weights

cd darknet
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137

#Setting up custom data set
#Upload pre-annotated dataset to Roboflow
#Apply pre-processing and augmentation. At least auto-orient and resize 416x416. Generate dataset
#Export dataset in YOLO Darknet format
#Copy downloaded url

cd darknet
wget -O roboflow.zip https://app.roboflow.com/ds/UjaO58Ucjv?key=KjiQmgvln7
unzip roboflow.zip
rm roboflow.zip


#Set up training file directories for custom dataset
cd darknet/
cp train/_darknet.labels data/obj.names
mkdir data/obj
#copy image and labels
cp train/*.jpg data/obj/
cp valid/*.jpg data/obj/

cp train/*.txt data/obj/

#now run write_files.py as command line script in darknet folder

#run training_config.py as command line script in darknet folder