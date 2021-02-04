run:
	docker-compose up

start:
	docker-compose up -d

logs:
	docker-compose logs -f

migrate:
	docker-compose exec web python hello_project/manage.py migrate

test:
	docker-compose exec web python hello_project/manage.py test hello_world