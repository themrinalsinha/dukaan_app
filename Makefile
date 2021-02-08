run:
	@docker-compose up --build
cli:
	@docker-compose exec web_service /bin/bash
shell:
	@docker-compose exec web_service python manage.py shell_plus
syncdb:
	@docker-compose exec web_service python manage.py makemigrations
	@docker-compose exec web_service python manage.py migrate
