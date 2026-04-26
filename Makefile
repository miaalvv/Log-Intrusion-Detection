up:
	docker-compose up --build

bootstrap:
	echo "Setting up project"
	pip install -r requirements.txt || true

run:
	python src/main.py

demo:
	docker-compose up --build --abort-on-container-exit

test:
	echo "Running tests"
	python -m pytest tests/