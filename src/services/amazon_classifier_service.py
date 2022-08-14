import typing as tp

import numpy as np

from src.services.amazon_classifier import AmazonClassifier


class AmazonClassifierService(object):
    def __init__(
        self,
        classifier: AmazonClassifier,
    ):
        """
        Create a service to classify Amazon lands.

        Parameters
        ----------
        classifier : AmazonClassifier
            An AmazonClassifier object which performs all classification logic.
        """
        self._classifier = classifier

    @property
    def land_types(self):
        """
        Land types that can be recognised on the images.

        Returns
        -------
        List with available land types.
        """
        return list(self._classifier.classes)

    def predict(self, image: np.array) -> tp.List[str]:
        """
        Predict classes of an input image.

        Parameters
        ----------
        image : np.ndarray
            Input image

        Returns
        -------
        List with classes of the input image.
        """
        return self._classifier.predict(image)

    def predict_proba(self, image: np.array):
        """
        Predict probabilities of each class of an input image.

        Parameters
        ----------
        image : np.ndarray
            Input image

        Returns
        -------
        Dictionary with probabilities of each model class.
        """
        return self._classifier.predict_proba(image)
