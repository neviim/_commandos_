# instalar docker compose

    ::: 
        $ yum install epel-release
        $ yum install -y python-pip
        
        $ pip install docker-compose
        $ yum upgrade python*



    ::: testando docker composer

        $ mkdir hello-world
        $ cd hello-world

        $ nano docker-compose.yml

            my-test:
            image: hello-world

        $ docker-compose up
        $ docker-compose ps

        # como um processo em segundo plano com o seguinte comando:
        $ docker-compose up -d
        $ docker-compose stop
        $ docker-compose rm 


        $ docker exec -it e90e12f70418 /bin/bash
        root@e90e12f70418:/#







# referencia
    # conceitos básicos do Docker Compose e como instalá-lo e executá-lo
    https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-centos-7

    # Running an Elasticsearch cluster with Docker
    https://stefanprodan.com/2016/elasticsearch-cluster-with-docker/