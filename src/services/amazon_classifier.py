import typing as tp

import numpy as np
import torch

from src.services.preprocess_images import preprocess_image


class AmazonClassifier(object):
    def __init__(self, config: tp.Dict):
        self._model_path = config['model_path']
        self._device = config['device']

        self._model = torch.jit.load(self._model_path, map_location=self._device)
        self._classes: np.array = np.array(self._model.classes)
        self._img_size: tp.Tuple[int, int] = (self._model.img_size, self._model.img_size)
        self._threshold: float = self._model.threshold

    @property
    def classes(self) -> tp.List:
        return self._classes

    def predict(self, image: np.ndarray) -> tp.List[str]:
        probs = self._predict(image)
        return self._postprocess_predict(probs)

    def predict_proba(self, image: np.ndarray) -> tp.Dict[str, float]:
        probs = self._predict(image)
        return self._postprocess_predict_proba(probs)

    def _predict(self, image: np.array) -> np.array:
        batch = preprocess_image(image, self._img_size).to(self._device)
        with torch.no_grad():
            probs = self._model(batch).detach().cpu()[0]
        return probs.numpy()

    def _postprocess_predict(self, probs: np.ndarray) -> tp.List[str]:
        return self._classes[probs > self._threshold].tolist()

    def _postprocess_predict_proba(self, predict: np.ndarray) -> tp.Dict[str, float]:
        sorted_idxs = reversed(predict.argsort())
        return {self._classes[ind]: float(predict[ind]) for ind in sorted_idxs}
