import os
import sys
import urllib.request
import tarfile

OUTPUT_DIR = "../../../data/01_raw/raw_01/"
DATASET_URL_IMAGES="http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09.tar"
DATASET_URL_CSV_TRAIN="http://web.mit.edu/torralba/www/TrainImages.txt"
DATASET_URL_CSV_TEST="http://web.mit.edu/torralba/www/TestImages.txt"

if os.path.exists(OUTPUT_DIR):
    print("skip download")
    sys.exit(0)
else:
    os.makedirs(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR + "tar")
    os.makedirs(OUTPUT_DIR + "extracted")

    with urllib.request.urlopen(DATASET_URL_IMAGES) as u:
        with open(OUTPUT_DIR + "tar/indoorCVPR_09.tar", 'bw') as o:
            print("start download tar")
            o.write(u.read())
            print("end download tar")

    with urllib.request.urlopen(DATASET_URL_CSV_TRAIN) as u:
        with open(OUTPUT_DIR + "extracted/CSV/TrainImages.txt", 'bw') as o:
            o.write(u.read())

    with urllib.request.urlopen(DATASET_URL_CSV_TEST) as u:
        with open(OUTPUT_DIR + "extracted/CSV/TestImages.txt", 'bw') as o:
            o.write(u.read())

    with tarfile.open(OUTPUT_DIR + "tar/indoorCVPR_09.tar", 'r:*') as tar:
        tar.extractall(OUTPUT_DIR + "extracted/")