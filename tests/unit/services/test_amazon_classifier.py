from copy import deepcopy

import cv2
import numpy as np
import pytest

from src.containers.containers import AppContainer


def test_predicts_not_fail(app_container: AppContainer, sample_image_np: np.ndarray):
    amazon_classifier = app_container.amazon_classifier()
    amazon_classifier.predict(sample_image_np)
    amazon_classifier.predict_proba(sample_image_np)


def test_prob_less_or_equal_to_one(app_container: AppContainer, sample_image_np: np.ndarray):
    amazon_classifier = app_container.amazon_classifier()
    probas = amazon_classifier.predict_proba(sample_image_np)
    for prob in probas.values():
        assert prob <= 1
        assert prob >= 0


def test_predict_dont_mutate_initial_image(app_container: AppContainer, sample_image_np: np.ndarray):
    initial_image = deepcopy(sample_image_np)
    amazon_classifier = app_container.amazon_classifier()
    amazon_classifier.predict(sample_image_np)
    assert np.allclose(initial_image, sample_image_np)


@pytest.mark.parametrize(
    'image_filename, y_true', [
        ('tests/supplementary/images/train_4.jpg', ('agriculture', 'clear', 'habitation', 'primary', 'road')),
        ('tests/supplementary/images/train_10.jpg', ('agriculture', 'clear', 'primary', 'slash_burn', 'water')),
    ],

)
def test_quality_on_train_images(app_container: AppContainer, image_filename: str, y_true: list):
    img = cv2.imread(image_filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    amazon_classifier = app_container.amazon_classifier()
    y_pred = set(amazon_classifier.predict(img))
    assert y_pred.issubset(y_true)
