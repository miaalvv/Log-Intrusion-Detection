up:
	docker-compose build

demo:
	del /Q artifacts\release\results.csv 2>nul
	del /Q artifacts\release\summary.json 2>nul
	docker-compose up --build --abort-on-container-exit

down:
	docker-compose down