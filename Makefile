up:
	docker-compose build

demo:
	rm -f artifacts/release/results.csv artifacts/release/summary.json
	docker-compose up --build --abort-on-container-exit

down:
	docker-compose down