import typing as tp

import numpy as np

from src.services.amazon_classifier import AmazonClassifier


class AmazonClassifierService(object):
    def __init__(
        self,
        classifier: AmazonClassifier,
    ):
        self._classifier = classifier

    @property
    def land_types(self):
        return self._classifier.classes

    def predict(self, image: np.array) -> tp.List[str]:
        return self._classifier.predict(image)

    def predict_proba(self, image: np.array):
        return self._classifier.predict_proba(image)
