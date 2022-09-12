# cvr-hw1-service

## 1 - Подготовить среду

1. Создать виртуальное окружение (можно любым удобным способом, но нужен python 3.10)

```shell
conda create --name <venv_name> python=3.10
conda activate <venv_name>
```

Могут возникнуть проблемы с активацией окружения -- тогда выполнить:

```shell
source /opt/conda/etc/profile.d/conda.sh
```

2. Установить необходимые зависимости: 

```shell
make install
```

## 2 - Скачать веса моделей

1. Из репозитория с моделлингом (к нему должен быть настроен доступ по ssh):

```shell
make download_weights_shh
```

2. Используя dvc-файлы из папки `weights`:

```shell
make download_weights_dvc
```


## 3 - Развернуть сервис

1. При помощи **питона**:

- Создать виртуальное окружение;
- Установить зависимости;
- Скачать веса моделей;
- Выполнить `make run_app`


2. С **докером**:

- Выполнить (предварительно должны быть скачаны веса моделей)
```
make build
```
- Или спуллить готовый образ с DockerHub: 
```shell
docker push olgachaganova/oliyyaa_amazon_service:latest
```

- Запустить контейнер на порту LOCAL_PORT:

```shell
docker run -p $(LOCAL_PORT):2202 -d oliyyaa_amazon_service:latest
```

## 4 - Тесты

1. Unit-тесты:

```shell
make run_unit_tests
```

2. Интеграционные тесты:

```shell
make run_integration_tests
```

3. Все тесты:

```shell
make run_tests
```

## 5 - Описание API

- `amazon/land_types` -- получить список всех типов земель, которые могут быть классифицированы на изображении


- `amazon/predict` -- получить предсказание типов земель на изображении


- `amazon/predict_proba` -- получить вероятность присутствия каждого возможного типа земель на изображении
