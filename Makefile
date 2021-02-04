build:
	docker-compose build

start:
	docker-compose up

run:
	docker-compose up -d

logs:
	docker-compose logs -f

test:
	docker-compose run web python hello_project/manage.py test hello_world

fixtures:
	docker-compose exec web python hello_project/manage.py loaddata hello_world

migrate:
	docker-compose exec web python hello_project/manage.py migrate

