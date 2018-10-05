# instalando redmine no docker

	::: http://blog.aeciopires.com/redmine-docker/

	::: Crie o diretório de dados do MySQL.

		$ mkdir -p /opt/docker/mysql/data

	::: Crie o diretório de dados, plugins e temas do Redmine.

		$ mkdir -p /opt/docker/redmine/data
		$ mkdir -p /opt/docker/redmine/plugins
		$ mkdir -p /opt/docker/redmine/themes
		$ chmod -R 775 /opt/docker/redmine		

	::: Baixe a última versão da imagem docker do MySQL e Redmine.

		$ docker pull mysql:5.7
		$ docker pull redmine

	::: Inicie o conteiner docker do MySQL com o banco de dados para o Redmine.

		$ docker run -d --name mysql-redmine \
		  -p 3306:3306 \
		  -v /opt/docker/mysql/data:/var/lib/mysql \
		  -e MYSQL_ROOT_PASSWORD=redmine \
		  -e MYSQL_DATABASE=redmine \
		  mysql:5.7

	::: Inicie o conteiner docker do Redmine acessando o banco de dados criado no MySQL.

		$ docker run -d --name redmine \
 -p 3001:3000 \
 -v /opt/docker/redmine/data:/usr/src/redmine/files \
 -v /opt/docker/redmine/plugins:/usr/src/redmine/plugins \
 -v /opt/docker/redmine/themes:/usr/src/redmine/themes \
 --link mysql-redmine:mysql \
 redmine

 ERROS:

 	::: Error response from daemon: Cannot link to a non running container: /mysql-redmine AS /redmine/mysql.

		d4590738225cf8675aafadea0165507fb1746454846c504c6dba271eaae07b6c
		/usr/bin/docker-current: Error response from daemon: Cannot link to a non running container: 
		/mysql-redmine AS /redmine/mysql.