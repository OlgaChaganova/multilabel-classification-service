FROM ubuntu:20.04


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    python3-pip \
    make \
    wget \
    ffmpeg \
    libsm6 \
    libxext6

WORKDIR /amazon_service

COPY . /amazon_service/

RUN make install && make init_dvc && make download_weights_dvc

CMD make run_app
