# {{ cookiecutter.project_name }}

![Unit Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Unit%20Tests/badge.svg)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg?token=EOH4M3PIYL)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }}/)

## Install

```sh
pip install {{ cookiecutter.project_slug }}
```

## Usage

> TODO



## Development

1. Make a python 3.8+ venv
2. `pip install -e .[test]`
3. `black lib --check`
4. `pytest`