import typing as tp

import torch
from sklearn.preprocessing import LabelEncoder


class AmazonClassifierService:
    def __init__(
            self,
            classifier: tp.Any,
            label_encoder: LabelEncoder,
            threshold: float,
    ):
        self._classifier = classifier
        self._label_encoder = label_encoder
        self._threshold = threshold

    def _get_probs(self, img: torch.tensor):
        probs = self._classifier(img)
        return probs

    def _get_labels(self, probs: torch.tensor) -> tp.List[str]:
        tags = 1 * (probs > self._threshold)
        labels = self._label_encoder.inverse_transform(tags)
        return labels

    def classify(self, img: torch.tensor) -> tp.List[str]:
        probs = self._get_probs(img)
        labels = self._get_labels(probs)
        return labels

