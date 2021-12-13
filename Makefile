game:
	python main.py

test:
	python -m pytest

lint:
	black --check .
	flake8 .
	mypy .
	isort --diff .

format:
	black .
	isort .
