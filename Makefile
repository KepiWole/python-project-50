build:
	poetry build

publish:
	poetry publish

install:
	poetry install

gendiff:
	poetry run gendiff

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 gendiff

