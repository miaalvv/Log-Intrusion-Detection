clean:
	python -c "import os; [os.remove(f) for f in ['artifacts/release/results.csv','artifacts/release/summary.json'] if os.path.exists(f)]"

up:
	docker-compose build

demo:
	docker-compose up --build --abort-on-container-exit

down:
	docker-compose down
