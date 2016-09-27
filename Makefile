mysql:
	docker run --name mysql -d -e MYSQL\_ROOT\_PASSWORD='$$3cureUS' -v "${PWD}/db":/var/lib/mysql mysql:5.7.14

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
	docker run -it --name mysql-cmdline --rm --link taskcrow_db_1:db mysql:5.7.14 /bin/bash

