# docker com redmine 

	::: 

		$ docker run -d --name some-mysql -e MYSQL_ROOT_PASSWORD=redmine -e MYSQL_DATABASE=redmine mysql


	::: Via docker stack deploy ou docker-compose

		Example stack.yml for redmine:

		version: '3.1'

		services:

		  redmine:
		    image: redmine
		    restart: always
		    ports:
		      - 8080:3000
		    environment:
		      REDMINE_DB_MYSQL: redmine
		      REDMINE_DB_PASSWORD: redmine

		  db:
		    image: mysql:5.7
		    restart: always
		    environment:
		      MYSQL_ROOT_PASSWORD: root
		      MYSQL_DATABASE: redmine

	::: 

		# Run docker stack deploy -c stack.yml redmine (or docker-compose -f stack.yml up), wait for it to initialize completely, 
		# and visit http://swarm-ip:8080, http://localhost:8080, or http://host-ip:8080 (as appropriate).


	::: 