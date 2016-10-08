mysql:
	docker run --name mysql -d -e MYSQL\_ROOT\_PASSWORD='$$3cureUS' -v "${PWD}/db":/var/lib/mysql mysql:5.7.14 \
            mysql -uroot -p'$$3cureUS' -h db \
            create user 'www'@'%' identified by '$$3cureUS'; \
            create database cs4501 character set utf8; \
            grant all on cs4501.* to 'www'@'i%'; 
        
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

