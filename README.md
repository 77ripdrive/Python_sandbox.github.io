![.github/workflows/poetry.yml](https://github.com/77ripdrive/Python_sandbox/workflows/.github/workflows/poetry.yml/badge.svg)
[![PYTEST](https://img.shields.io/badge/pytest-v%200.1-green)](https://img.shields.io/badge/pytest-v%200.1-green)

## An example of initializing a Python project from scratch

### Dependency management with [Poetry-Python](https://python-poetry.org/docs/)

```sh
pip3 install --user poetry
```

#### for Windows with Powershell

```sh
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

### Poetry init

```sh
poetry init
poetry add pre-commit black
```

> на вопросы `Would you like to define ...` ответить `no`

### Pre-commit

#### for Windows

```sh
poetry pre-commit sample-config > .pre-commit-config.yaml
poetry pre-commit install
```

or

```sh
pre-commit sample-config > .pre-commit-config.yaml
pre-commit run -a
```

#### To run tests, clone the project and run

```sh
poetry install
poetry run pytest
```

#### To run marked tests with tag @api_service

```sh
poetry run python -m pytest -k "api_service"

```
