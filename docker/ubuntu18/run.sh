#!/bin/bash

# usage
SCRIPT_FILE=`basename $0`
function usage()
{
  echo "usage: ${SCRIPT_FILE} docker/nvidia-docker" 1>&2
}

# arguments
if [ $# -ne 1 ]; then
  usage
  exit 1
fi
DOCKER_CMD=$1

# constant
CONTAINER_NAME=indoor_scene_reckognition
CONTAINER_IMAGE=indoor_scene_reckognition
HOST_PORT_IPYNB=18888
CONTAINER_PORT_IPYNB=8888
HOST_PORT_KV=14141
CONTAINER_PORT_KV=4141
HOST_PORT_MLFLOW=15000
CONTAINER_PORT_MLFLOW=5000

# main
${DOCKER_CMD} run --name ${CONTAINER_NAME} \
  --privileged \
  --entrypoint bash \
  -v $(pwd)/../../:/opt/indoor_scene_reckognition/ \
  -p ${HOST_PORT_IPYNB}:${CONTAINER_PORT_IPYNB} \
  -p ${HOST_PORT_KV}:${CONTAINER_PORT_KV} \
  -p ${HOST_PORT_MLFLOW}:${CONTAINER_PORT_MLFLOW} \
  -it ${CONTAINER_IMAGE}
