from dependency_injector import containers, providers

from src.services.amazon_classifier import AmazonClassifier
from src.services.amazon_classifier_service import AmazonClassifierService


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    amazon_classifier = providers.Singleton(
        AmazonClassifier,
        config=config.services.amazon_classifier,
    )

    amazon_classifier_service = providers.Singleton(
        AmazonClassifierService,
        classifier=amazon_classifier,
    )
