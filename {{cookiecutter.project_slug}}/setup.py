#!/usr/bin/env python
"""Setup."""

from pathlib import Path

from setuptools import find_packages, setup

THIS_DIRECTORY = Path(__file__).resolve().parent
INSTALL_REQUIRES = []
DEV_REQUIREMENTS = [
    "black-22.6.0",
    "pytest==7.1.2",
    "coverage==6.4.1",
    "pytest-cov==3.0.0",
    "codecov==2.1.12",
]
# use readme as long description
LONG_DESCRIPTION = (THIS_DIRECTORY / "readme.md").read_text()
VERSION = (
    (THIS_DIRECTORY / "src" / "{{ cookiecutter.project_slug }}" / "version")
    .read_text()
    .strip()
)

setup(
    author_email="{{ cookiecutter.email }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    extras_require=dict(test=DEV_REQUIREMENTS),
    install_requires=INSTALL_REQUIRES,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    name="{{ cookiecutter.project_slug }}",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.8",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    version=VERSION,
)
