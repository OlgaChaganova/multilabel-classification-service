# cvr-hw1-service

## 1 - Подготовить среду для обучения

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


## 3 - Запустить приложение

1. Выполнить:

```shell
make run_app
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