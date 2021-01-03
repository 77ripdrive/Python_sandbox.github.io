## An example of initializing a Python project from scratch

### Dependency management with [Poetry-Python](https://python-poetry.org/docs/)

```sh
pip3 install --user poetry
```

####  for Windows with Powershell

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
