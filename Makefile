build:
	docker-compose build --pull

stack-up:
	docker-compose up -d

stack-purge:
	docker-compose stop
	docker-compose kill
	docker-compose rm

stack-full-refresh:
	docker-compose build --no-cache --pull

build:
	docker-compose build gym_scheduler --pull

run:
	docker-compose run --rm gym_scheduler python3 /home/gym_scheduler/scripts/gym_scheduler.py 

bash:
	docker-compose run --rm --entrypoint "/bin/bash -c" gym_scheduler bash 

launch:
	docker-compose -f docker-compose.yaml up 
