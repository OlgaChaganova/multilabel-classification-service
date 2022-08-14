import typing as tp

import torch
from torchvision.transforms import functional as ttf

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]


def preprocess_image(
    img: torch.tensor,
    img_size: tp.List[int],
):
    img = ttf.resize(img, size=img_size)
    img = ttf.to_tensor(img)
    img = ttf.normalize(img, mean=IMAGENET_MEAN, std=IMAGENET_STD)
    return img
