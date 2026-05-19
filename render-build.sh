#!/usr/bin/env bash

apt-get update && apt-get install -y \
    cmake \
    build-essential \
    python3-dev \
    libopenblas-dev \
    liblapack-dev \
    zlib1g-dev \
    libjpeg-dev

pip install -r requirements.txt
