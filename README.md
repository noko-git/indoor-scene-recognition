# indoor-scene-reckognition

## Getting Started for Developer
```
# build container
$ docker build ./ -t indoor_scene_reckognition

# run container
$ sh run.sh docker

# set credentials
conf/base/credentials/XXX.json

# exec scripts
$ python3 scraping_indoor_scene_reckognition.py
$ python3 label_indoor_scene_reckognition.py
$ python3 upload_label_indoor_scene_reckognition_to_gcs.py

# reference
* [GCPのAutoMLVisionを試してみた](https://qiita.com/noko_qii/items/7a5af519274240123b0d)

```

## Description
* OS version
```
$ cat /etc/issue
Ubuntu 18.04.5 LTS
```

* Python version
```
$ python3 -V
Python 3.6.9
```