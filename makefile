# Variables
SRC_DIR := ./src
LINE_LENGTH := 120
PYTHONPATH := $(shell pwd)


run:
	gunicorn "src.app:app" -c "./src/gunicorn.py"

run_dev:
	export PYTHONPATH=$(shell pwd) && export FLASK_APP=src/app.py && export FLASK_ENV=development && flask run

format:
	black $(SRC_DIR)/* --line-length=$(LINE_LENGTH) --skip-string-normalization
	isort $(SRC_DIR)/* --line-length=$(LINE_LENGTH) --multi-line=0
	flake8 $(SRC_DIR)/* --max-line-length=$(LINE_LENGTH)

# Create a new release
# Usage: make release
release:
	@echo "Input version[$(shell git describe --abbrev=0 --tags --always)]:"
	@read INPUT_VERSION; [[ ! -z $$INPUT_VERSION ]] \
		|| INPUT_VERSION=`git describe --abbrev=0 --tags --always` \
		&& echo "__version__ = '$$INPUT_VERSION'" > `pwd`/src/__init__.py \
		&& echo "Creating a new release version: $$INPUT_VERSION" \
		&& git add `pwd`/src/__init__.py \
		&& git commit -m "new version $$INPUT_VERSION" \
		&& git tag "$$INPUT_VERSION" \
		&& git push origin "$$INPUT_VERSION" \
		&& git push origin -u "$(shell git rev-parse --abbrev-ref HEAD)"

revision:
	@PYTHONPATH="${PYTHONPATH}" alembic revision --autogenerate

upgrade:
	@PYTHONPATH="${PYTHONPATH}" alembic upgrade head

downgrade:
	@PYTHONPATH="${PYTHONPATH}" alembic downgrade -1


clean-pyc:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +
	find . -name '*~' -exec rm -rf {} +
