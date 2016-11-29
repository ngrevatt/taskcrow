mysql:
	rm -rf db
	mkdir db
	docker run --name mysql -d -e MYSQL\_ROOT\_PASSWORD='$$3cureUS' -v "${PWD}/db":/var/lib/mysql mysql:5.7.14

# This won't work for a few seconds after making the mysql target.
initmysql:
	docker run -it --rm --link mysql:db mysql:5.7.14 mysql -uroot -p"\$$3cureUS" -h db -v -e \
		"CREATE USER 'www'@'%' IDENTIFIED BY '\$$3cureUS';\
		CREATE DATABASE cs4501 CHARACTER SET utf8;\
		GRANT ALL PRIVILEGES ON *.* TO 'www'@'%';"

stopmysql:
	docker stop mysql
	docker rm mysql

upcompose:
	docker-compose up --build

rmcompose:
	docker-compose rm

modelsshell:
	docker exec -it taskcrow_models_1 /bin/bash

expshell:
	docker exec -it taskcrow_exp_1 /bin/bash

webshell:
	docker exec -it taskcrow_web_1 /bin/bash

dbshell:
	docker run -it --name mysql-cmdline --rm --link mysql:db mysql:5.7.14 /bin/bash

batchshell:
	docker exec -it batch /bin/bash

kafkashell:
	docker exec -it kafka /bin/bash

test:
	docker exec -it taskcrow_models_1 python /app/manage.py test
	docker exec -it taskcrow_batch_1 python -m unittest tests
	docker build -t taskcrow/webtest webtest
	docker run --rm --link taskcrow_selenium_1:selenium -v "$(PWD)/webtest:/app" -it taskcrow/webtest python -m unittest tests

travis_test:
	docker exec -it taskcrow_models_run_1 python /app/manage.py test

agnes:
	rm -rf ../cs4501/db
	mkdir ../cs4501/db
	docker run --name mysql -d -e MYSQL\_ROOT\_PASWORD='$$3cureUS' -v "${PWD}/../cs4501/db":/var/lib/mysql mysql:5.7.14
