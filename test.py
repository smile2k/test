# Step 1. Mount drive 
from google.colab import drive
drive.mount('/content/gdrive')
//////////////////////////
# Step 2. Tai ma nguon YOLO ve drive
!rm -rf darknet
%cd /content/gdrive/My\ Drive
!git clone https://github.com/AlexeyAB/darknet
%cd /content/gdrive/My\ Drive/darknet
!rm -rf data
!mkdir data
///////////////////////////////
# Step 4. Giải nén file data
%cd /content/gdrive/My\ Drive/darknet/data
!unzip data.zip
//////////////////////////////
# Step 5. Tạo file yolo.names
%cd /content/gdrive/My\ Drive/darknet
!echo "no_mask" > yolo.names
!echo "mask" >> yolo.names
!echo "sai" >> yolo.names
/////////////////////////
# Step 6. Tạo file train.txt và val.txt
%cd /content/gdrive/My\ Drive/darknet

import glob2
import math  
import os
import numpy as np

files = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image_files = glob2.glob(os.path.join("data/data/", ext))
  files += image_files

nb_val = math.floor(len(files)*0.2)
rand_idx = np.random.randint(0, len(files), nb_val)

# Tạo file train.txt
with open("train.txt", "w") as f:
  for idx in np.arange(len(files)):
    if (os.path.exists(files[idx][:-3] + "txt")):
      f.write(files[idx]+'\n')

# Tạo file vali.txt
with open("val.txt", "w") as f:
  for idx in np.arange(len(files)):
    if (idx in rand_idx) and (os.path.exists(files[idx][:-3] + "txt")):
      f.write(files[idx]+'\n')
   ///////////////////////////////
# Step 7. Tạo file yolo.data
%cd /content/gdrive/My\ Drive/darknet
!mkdir backup
!echo classes=3 > yolo.data
!echo train=train.txt >> yolo.data
!echo valid=val.txt >> yolo.data
!echo names=yolo.names >> yolo.data
!echo backup=backup >> yolo.data
////////////////////////////////////
# Step 8. Make darknet
%cd /content/gdrive/My\ Drive/darknet
!make clean
!make
///////////////////////////////
# Step 9. Download pretrain weight
%cd /content/gdrive/My\ Drive/darknet
!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137
  //////////////////////////////////////////////
  # Step 10. Train
# %cd /content/gdrive/My\ Drive/darknet
# !./darknet detector train yolo.data cfg/yolov4-custom.cfg yolov4.conv.137 -dont_show 
%cd /content/gdrive/My\ Drive/darknet
!./darknet detector train yolo.data cfg/yolov4-custom.cfg backup/yolov4-custom_last.weights -dont_show 
