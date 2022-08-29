import typing as tp

import cv2
import numpy as np
import torch

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)
MAX_UINT8 = 255


def preprocess_image(
    image: np.array,
    target_image_size: tp.Tuple[int, int],
) -> torch.tensor:

    image = image.astype(np.float32)
    image = cv2.resize(image, target_image_size) / MAX_UINT8
    image = np.transpose(image, (2, 0, 1))
    image -= np.array(IMAGENET_MEAN)[:, None, None]
    image /= np.array(IMAGENET_STD)[:, None, None]
    return torch.from_numpy(image)[None]
