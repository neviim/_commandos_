# docker install mariadb

	::: Buscar ou atualizar a imagem do MariaDB e verificar

		$ docker pull mariadb:latest
		$ docker images

		# Verifique se a pasta de dados ainda não existe. Caso contrário, a parte de inicialização a seguir não faz sentido.

		$ app=mariadbprod
		$ mkdir /data/$app
		$ ls -alhF /data/$app/
		$ #sudo rm -rf /data/$app/

		# Lançar um volume de mapeamento de contêiner /data/mariadbprod/ para /var/lib/mysql/ and check.

		$ app=mrdbredmine
		$ docker ps -a | grep $app

		$ docker run --name mrdbredmine -e MYSQL_ROOT_PASSWORD=redmine -d mariadb -h mrdbredmine -p 3306:3306 -v /data/$app:/var/lib/mysql 

		$ docker ps -a | grep $app
		$ docker logs $app

		c4edcdd44899a5713c5efb583cdc78799965b18b8f79ca628339117aa7ebc348
		$ iptables -w2 -t filter -A DOCKER ! -i docker0 -o docker0 -p tcp -d 10.0.9.18 --dport 3306 -j ACCEPT

		# aqui: http://doc.nethence.com/docker/mariadb

		$ docker exec -ti mrdbredmine mysql -u root -p redmine
		$ docker exec -ti $app        mysql -u root -p root

		create database somedb;
		grant all privileges on somdb.* to somedbuser identified by 'USERPASS_HERE';
		flush privileges;


		# --- teste

		$ docker run --name mrdbredmine -e MYSQL_ROOT_PASSWORD=redmine -d mariadb -h mrdbredmine -p 3306:3306 -v /data/$app:/var/lib/mysql 
		$ docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=test    -d mariadb
		$ docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=test    -d mariadb:5.7

		# Opcionalmente, após o nome da imagem, podemos especificar algumas opções para o mysqld. Por exemplo:

		$ docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=test -d mariadb --log-bin --binlog-format=MIXED
		$ docker ps

		# executando comando dentro do conteiner

		$ docker exec -ti mariadbtest mysql -u root -p
		MariaDB [(none)]> quit

		# O Docker nos permite reiniciar um contêiner com um único comando:

		$ docker restart mariadbtest
		$ docker stop mariadbtest
		$ docker start mariadbtest

		$ docker stop --time=30 mariadbtest
		$ docker kill mariadbtest

		# Caso desejemos destruir um contêiner, talvez porque a imagem não atenda às nossas necessidades, podemos pará-lo e executar:

		$ docker rm mariadbtest
		$ docker rm -v mariadbtest
		
		# Se o contêiner não iniciar ou não estiver funcionando corretamente, podemos investigar com o seguinte comando:

		$ docker logs mariadbtest

		# --- Fim teste

		# --- Docker ps

			$ docker ps --filter "name=mariadbtest"
			$ docker ps --filter "label=color"


		# --- Docker remover imagens

			$ docker images --digests
			$
			REPOSITORY             TAG                 DIGEST                                                                    IMAGE ID            CREATED             SIZE
			docker.io/redmine      latest              sha256:deedc4ec97c280fe9474166e948c1b259cc81999114ceac1b8e58e66c14ce349   a4e46890e900        2 days ago          688 MB
			jadsid/ubuntu-master   1.1                 <none>                                                                    2da3f0e13fe2        3 days ago          224 MB
			jadsid/ubuntu-master   1.0                 <none>                                                                    e4c93922e180        3 days ago          130 MB
			docker.io/mariadb      latest              sha256:0d4bad4ea58ec976f3de2b5e16f4ed9513da58f21a2bb0df9fdd8422526dd5e5   54514d54a4a5        3 days ago          364 MB
			docker.io/redmine      <none>              sha256:30937a84c313b206497ade3aa6f35659896f8579166480b8842ffa8e77c27228   7b11bff991fe        6 days ago          687 MB
			docker.io/ubuntu       latest              sha256:de774a3145f7ca4f0bd144c7d4ffb2931e06634f11529653b23eba85aef8e378   cd6d8154f1e1        4 weeks ago         84.1 MB
			docker.io/mysql        5.7                 sha256:1d8f471c7e2929ee1e2bfbc1d16fc8afccd2e070afed24805487e726ce601a6d   563a026a1511        4 weeks ago         372 MB
			docker.io/mysql        latest              sha256:038f5f6ea8c8f63cfce1bce9c057ab3691cad867e18da8ad4ba6c90874d0537a   6a834f03bd02        4 weeks ago         484 MB
			docker.io/centos       latest              sha256:6f6d986d425aeabdc3a02cb61c02abb2e78e57357e92417d6d58332856024faf   5182e96772bf        2 months ago        200 MB

			$ docker rmi 2da3f0e13fe2
			$ 

			$ docker rmi docker.io/redmine@sha256:30937a84c313b206497ade3aa6f35659896f8579166480b8842ffa8e77c27228
			$ docker kill my_container

			$ 

			