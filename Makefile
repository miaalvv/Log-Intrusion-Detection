up:
	echo "Simulating docker up"

bootstrap:
	echo "Setting up project"
	pip install -r requirements.txt || true

run:
	python src/main.py

demo:
	make run

test:
	echo "Running tests"
	python -m pytest tests/