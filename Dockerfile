FROM python:slim

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

RUN make install

WORKDIR /amazon_service

COPY . /amazon_service/

CMD make run_app
