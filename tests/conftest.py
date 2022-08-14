import os.path

import cv2
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from omegaconf import OmegaConf

from app import set_routers
from src.containers.containers import AppContainer

TESTS_DIR = os.path.dirname(__file__)


@pytest.fixture(scope='session')
def sample_image_bytes():
    f = open(os.path.join(TESTS_DIR, 'supplementary', 'images', 'train_4.jpg'), 'rb')  # -- noqa: WPS515
    try:
        yield f.read()
    finally:
        f.close()


@pytest.fixture
def sample_image_np():
    img = cv2.imread(os.path.join(TESTS_DIR, 'supplementary', 'images', 'train_4.jpg'))
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


@pytest.fixture(scope='session')
def app_config():
    return OmegaConf.load(os.path.join(TESTS_DIR, 'supplementary', 'test_config.yml'))


@pytest.fixture
def app_container(app_config):
    container = AppContainer()
    container.config.from_dict(app_config)
    return container


@pytest.fixture(scope='session')
def test_app():
    app = FastAPI()
    set_routers(app)
    return app


@pytest.fixture(scope='session')
def client(test_app):
    return TestClient(test_app)
