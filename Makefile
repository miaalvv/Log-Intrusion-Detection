bootstrap:
	echo "Setting up project"
	pip install -r requirements.txt || true

run:
	python src/log_reader.py

test:
	echo "Running tests"
