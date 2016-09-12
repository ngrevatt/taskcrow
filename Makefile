upcompose:
	docker-compose up --build

rmcompose:
	docker-compose rm

modelsshell:
	docker exec -it taskcrow_models_1 /bin/bash

dbshell:
	docker run -it --name mysql-cmdline --rm --link taskcrow_db_1:db mysql:5.7.14 /bin/bash

