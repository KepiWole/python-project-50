
build:
	poetry build

install:
	poetry install

gendiff:
	poetry run gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff
