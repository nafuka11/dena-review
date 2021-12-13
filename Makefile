game:
	python main.py

lint:
	black --check .
	flake8 .
	mypy .
	isort --diff .

format:
	black .
	isort .
