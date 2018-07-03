# Instalando docker com elasticsearch

    ::: Imagens do Docker podem ser recuperadas com os seguintes comandos

        $ su
        $ yum install docker
        
        $ systemctl start docker
        $ systemctl status docker
        $ docker run hello-world

        # Add user em docker group
        $ sudo usermod -aG docker $USER
        $ groupadd docker
        $ usermod -aG docker $(whoami)
        $ systemctl restart docker

        $ ls -l /var/run/docker.sock
        $ chown *your-username* /var/run/docker.sock 
        $ docker info

        # Instalar docker e Kibana
        $ docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.0
        $ docker pull docker.elastic.co/kibana/kibana:6.3.0


    ::: Rodando Elasticsearch a partir da linha de comando (Basic Auth Elasticsearch(user: 'elastic', pw 'elastic') daemon)

        # A listagem a seguir cria dois contêineres no modo daemon. Eles são automaticamente excluídos/removidos na parada através do parâmetro --rm
        $ docker run -d --rm -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "transport.host=0.0.0.0" -e ELASTIC_PASSWORD=elastic --name elastic docker.elastic.co/elasticsearch/elasticsearch:6.3.0 && sleep 20

        # execute o daemon do Kibana no modo de remoção automática # start leva 20+ segundos
        $ docker run -d --rm --link elastic:elastic-url -e "ELASTICSEARCH_URL=http://10.0.9.39:9200" -e ELASTICSEARCH_PASSWORD="elastic"  -p 5601:5601 --name kibana docker.elastic.co/kibana/kibana:6.3.0 && sleep 20

        # check connection to Elasticsearch (JSON é retornado) [curl "http://localhost:9200/_count" -u 'elastic:secret']
        $ curl "http://localhost:9200/_count" -u 'elastic:elastic'

        # check connection to Kibana (o HTML é retornado)
        $ curl http://localhost:5601 --location

        # Pare os contêineres Elasticsearch e Kibana
        $ systemctl stop elastic kibana


    ::: Docker composer





    ::: Observaçoes relevantes.

        - Você não deve usar o usuário elástico para conectar o Kibana ao Elasticsearch. É para isso que o usuário thekibana é. 
          O usuário elástico tem privilégios de superusuário e não é uma boa idéia executar o Kibana com esses privilégios. 
        
        - Kibana será o padrão para usar o usuário kibana, então você só precisa configurar o elasticsearch.password para 
          corresponder à senha do usuário do Kibana.

          Em kibana.yml o usuário de configuração-senhas elasitc e passe

            elasticsearch.username: "xxx"
            elasticsearch.password: "xxx"


        ::: Em alguns ambientes, pode fazer mais sentido preparar uma imagem personalizada contendo sua configuração. Um Dockerfile para conseguir isso pode ser tão simples quanto:

            - As imagens do Docker fornecem vários métodos para configurar o Kibana. A abordagem convencional é fornecer um arquivo kibana.yml, conforme descrito em Configurando o 
              Kibana, mas também é possível usar variáveis ​​de ambiente para definir configurações.

              Uma maneira de configurar o Kibana no Docker é fornecer o kibana.yml via bind-mounting. Com o docker-compose, o bind-mount pode ser especificado assim:










# referencias
    # instalar elasticsearch e kibana
    https://docs.swiftybeaver.com/article/33-install-elasticsearch-kibana-via-docker

    # config kibana
    https://www.elastic.co/guide/en/kibana/6.3/settings.html

    # Running an Elasticsearch cluster with Docker
    https://stefanprodan.com/2016/elasticsearch-cluster-with-docker/