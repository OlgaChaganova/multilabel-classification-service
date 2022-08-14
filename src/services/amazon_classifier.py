import typing as tp

import torch

class AmazonClassifier:
    def __init__(self, config: tp.Dict):
        self._model_path = config['model_path']
        self._map_location = config['map_location']

        self.model = torch.jit.load(self._model_path, map_location=self._map_location)


        