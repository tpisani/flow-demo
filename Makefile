
install:
	@pip install -r requirements.txt


run:
	@python manage.py runserver


expose:
	@python manage.py runserver 0.0.0.0:8000


new-db:
	@mysql -u root -e "drop database if exists flow_demo; create database flow_demo";


clean:
	@find . -name "*.pyc" | xargs rm
