import os
import glob
from google.cloud import storage

CREDENTIAL_PATH="../../../conf/base/credentials/indoor-scene-recognition.json"
LOCAL_PATH="../../../data/03_primary/primary_01"
BUCKET_FOLDER_DIR="data/03_primary/primary_01"

# Explicitly use service account credentials by specifying the private key file
storage_client = storage.Client.from_service_account_json(
    CREDENTIAL_PATH)

# Make an authenticated API request

bucket = storage_client.get_bucket("indoor_scene_reckognition_bucket")

# upload file from local to gcs
def upload_local_directory_to_gcs(local_path, bucket, gcs_path):
    assert os.path.isdir(local_path)
    for local_file in glob.glob(local_path + '/**'):
        if not os.path.isfile(local_file):
           upload_local_directory_to_gcs(local_file, bucket, gcs_path + "/" + os.path.basename(local_file))
        else:
           remote_path = os.path.join(gcs_path, local_file[1 + len(local_path):])
           blob = bucket.blob(remote_path)
           blob.upload_from_filename(local_file)

upload_local_directory_to_gcs(LOCAL_PATH, bucket, BUCKET_FOLDER_DIR)