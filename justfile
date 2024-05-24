#!/usr/bin/env just --justfile

# Dependencies installation
install:
  poetry install

# Installation without dev dependencies
install-no-dev:
  poetry install --no-dev

# Run pre-commit lint
lint:
  @pre-commit run --all-files


# Run tests
test:
  poetry run pytest

# Running tests with coverage
test-with-coverage:
  poetry run pytest --cov=yandex_geocoder

# Uploading coverage report
upload-coverage:
  poetry run coveralls
