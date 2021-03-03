FROM ubuntu:18.04

ENV GIT_SSL_NO_VERIFY=1

# apt install
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
         curl \
         git \
         python3-pip \
         python3-setuptools \
         unzip \
         vim \
         wget \
         gcc \
         python-dev \
         python-setuptools \
         libffi-dev

# pip install
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# cd
WORKDIR /opt/indoor_scene_reckognition

# expose port for jupyter notebook
EXPOSE 8888

# expose port for kedro viz
EXPOSE 4141

# expose port for mlflow ui
EXPOSE 5000

# exec CMD
CMD kedro run