import cv2
import numpy as np
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, File

from src.containers.containers import AppContainer
from src.routers.routers import router
from src.services.amazon_classifier_service import AmazonClassifierService


@router.get('/land_types')
@inject
def land_types(service: AmazonClassifierService = Depends(Provide[AppContainer.amazon_classifier_service])):
    return {'land_types': service.land_types}


@router.post('/predict')
@inject
def predict(
    image: bytes = File(),
    service: AmazonClassifierService = Depends(Provide[AppContainer.amazon_classifier_service]),
):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    predicted_land_types = service.predict(img)
    return {'land_types': predicted_land_types}


@router.post('/predict_proba')
@inject
def predict_proba(
    image: bytes = File(),
    service: AmazonClassifierService = Depends(Provide[AppContainer.amazon_classifier_service]),
):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    return service.predict_proba(img)


@router.get('/health_check')
def health_check():
    return 'OK'
