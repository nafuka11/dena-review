game:
	python main.py

test:
	poetry run python -m pytest

lint:
	poetry run black --check .
	poetry run flake8 .
	poetry run mypy .
	poetry run isort --diff .

format:
	poetry run black .
	poetry run isort .
