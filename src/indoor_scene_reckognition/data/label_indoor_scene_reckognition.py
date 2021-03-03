import os
import sys
import shutil
import pandas as pd

RAW_DIR = "../../../data/01_raw/raw_01/"
PRIMARY_DIR = "../../../data/03_primary/primary_01/"
TARGET_LABELS = ["gym", "library", "winecellar"]
BUCKET_PATH = "gs://indoor_scene_reckognition_bucketXX/data/03_primary/primary_01/"

# copy images from raw to primary
if os.path.exists(PRIMARY_DIR):
    print("skip copy Images")
else:
    os.makedirs(PRIMARY_DIR)
    os.makedirs(PRIMARY_DIR + "CSV")
    for i in range(len(TARGET_LABELS)):
        shutil.copytree(RAW_DIR + "extracted/Images/" + TARGET_LABELS[i], PRIMARY_DIR + "Images/" + TARGET_LABELS[i])

# make label csv file
df_raw_train_selected = pd.DataFrame(index=[], columns=["path", "label"])
df_raw_train = pd.read_csv(RAW_DIR + "extracted/CSV/TrainImages.txt", names=["path"])
for i in range(len(TARGET_LABELS)):
    df_raw_train_selected = pd.concat([df_raw_train_selected, df_raw_train[df_raw_train["path"].str.contains(TARGET_LABELS[i])]])

df_primary_train = pd.DataFrame(index=[], columns=["path", "label"])
for idx,item in df_raw_train_selected.iterrows():
    path_gcs = BUCKET_PATH + "Images/" + item.path
    label = item.path.split("/")[0]
    df_line = pd.DataFrame([path_gcs, label], index=["path", "label"]).T
    df_primary_train = pd.concat([df_primary_train, df_line])
df_primary_train.to_csv(PRIMARY_DIR + "CSV/label_train.csv", sep=",", header=False, index=False)