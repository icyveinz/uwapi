.ONESHELL:
up:
	clear || cls
	docker-compose up --build
	docker-compose exec django_web python manage.py migrate
cleaned:
	clear || cls
	docker-compose down -v
	docker system prune -a -f
	docker-compose up --build
	docker-compose exec django_web python manage.py migrate