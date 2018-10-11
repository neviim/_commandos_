# docker com redmine (http://doc.nethence.com/docker/redmine)

	::: Criando um container [6db52f29ff1cfd5fd60ba5498ec3652f5965c33863d73f6b2fdfd0a42d30e029]

		$ docker pull redmine
		$
		$ docker run --name mariadbprod -e MYSQL_ROOT_PASSWORD=root -d mariadb:latest
		6db52f29ff1cfd5fd60ba5498ec3652f5965c33863d73f6b2fdfd0a42d30e029

		docker ps -a
		CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
		6db52f29ff1c        mariadb:latest      "docker-entrypoint..."   5 hours ago         Up 5 hours          3306/tcp            mariadbprod


	::: Crie um banco de dados MariaDB e usuário para Redmine

		# Container: mariadbprod
		# Imagem...: mariadb:latest
		# Nome.....: mariadbprod
		# ----------------------
		# Database.: redmine
		# User.....: redmine
		# Pwd......: redmine

		$ docker exec -ti mariadbprod mysql -u root -p root

		MariaDB [(none)]> CREATE DATABASE redmine CHARACTER SET utf8;
		MariaDB [(none)]> CREATE USER 'redmine' IDENTIFIED BY 'redmine';
		MariaDB [(none)]> GRANT ALL PRIVILEGES ON redmine.* TO 'redmine';

		ctr+d 

	:::  

		$ app=redmineprod
		$ docker run -d --name $app -h $app -p 3000:3000 --link mariadbprod:mariadb docker.io/redmine

		$ docker exec -ti $app bash
		
		$ cd ~/
		$ ln -s /usr/src/redmine/config .
		$ ln -s /usr/src/redmine .

		# Verifique se você pode acessar o mariadb dentro do container.

		$ apt update
		$ apt install netcat
		$ apt -y install mysql-client

		$ gem install mysql2

		$ nc -v -z mariadb 3306
		mariadb [172.17.0.2] 3306 (?) open

		$ mysql -u root    -p root    -h mariadb
		$ mysql -u redmine -p redmine -h mariadb
		$
		Welcome to the MariaDB monitor.  Commands end with ; or \g.
		Your MariaDB connection id is 10
		Server version: 10.3.10-MariaDB-1:10.3.10+maria~bionic mariadb.org binary distribution
		Copyright (c) 2000, 2017, Oracle, MariaDB Corporation Ab and others.
		Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

		MariaDB [redmine]>
		MariaDB [redmine]>
		MariaDB [redmine]> quit

		$ cd ~/config
		$ cp configuration.yml.example configuration.yml

		$ 


	::: setup Rails_env

		$ cd ~/config/environments/
		$ cp production.rb production.rb.dist

		$ vim production.rb
		  # Disable delivery errors
		  #config.action_mailer.raise_delivery_errors = false
		  config.action_mailer.raise_delivery_errors = true
		  config.action_mailer.perform_deliveries = true
		  config.action_mailer.default_options = {from: 'redmine@example.com'}

	::: DB credencial

		$ cd ~/config/
		$ cp database.yml.example database.yml

		$ vim database.yml

			production:
			  adapter: "mysql2"
			  database: "redmine"
			  host: "mariadb"
			  username: "redmine"
			  password: "redmine"
			  encoding: "utf8"


	::: Configurar sendmail

		$ apt install sendmail
		
		$ vim /etc/hosts
			#
			127.0.0.1  localhost tilab

		$ sendmailconfig


	::: Popular banco

		# Popula o banco de dados.
		$ cd ~/redmine/
		$ RAILS_ENV=production bundle exec rake db:migrate
		$ RAILS_ENV=production bundle exec rake redmine:load_default_data
		$ RAILS_ENV=production REDMINE_LANG=en bundle exec rake redmine:load_default_data









# referencia:
	http://doc.nethence.com/docker/redmine
	# config database
	https://github.com/cloud66/rails4-mysql-sample/blob/master/config/database.yml
	https://github.com/cloud66/rails4-mysql-sample/blob/master/config/environments/production.rb
	# config postfix
	http://doc.nethence.com/server/email-settings