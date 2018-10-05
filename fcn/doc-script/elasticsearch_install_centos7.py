# instalar java

    ::: Instalando java para centos7 [https://tecadmin.net/install-java-8-on-centos-rhel-and-fedora/]
        $ wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz"
        $ tar -zxvf jdk-8u*-linux-x64.tar.gz
        $ mv jdk1.8.*/ /usr/


        $ alternatives --install /usr/bin/java java /usr/jdk1.8.*/bin/java 2
        $ alternatives --config java


        $ java –version


        ::: 
            $ export JAVA_HOME=/usr/jdk1.8.0_*
            $ export JRE_HOME=/usr/jdk1.8.0_*/jre/
            $ export PATH=$JAVA_HOME/bin:$PATH


        :::

            ### Debian 9 / Ubuntu 16.04 & Linux Mint 18 ###

            $ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

            ### RHEL 7 / CentOS 7 ###

            # rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch


            ### Debian 9 / Ubuntu 16.04 & Linux Mint 18 ###

            $ echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elk.list

                ### RHEL 7 / CentOS 7 ###

                $ cat <<EOF >> /etc/yum.repos.d/elasticsearch.repo
                [elasticsearch-5.x]
                name=Elasticsearch repository for 5.x packages
                baseurl=https://artifacts.elastic.co/packages/5.x/yum
                gpgcheck=1
                gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
                enabled=1
                autorefresh=1
                type=rpm-md
                EOF


    ::: Instalar elasticsearch

        ### Debian 9 / Ubuntu 16.04 & Linux Mint 18 ###

            $ sudo apt-get update 
            $ sudo apt-get install -y elasticsearch

        ### RHEL 7 / CentOS 7 ###

            $ yum -y install elasticsearch


        ### Debian 9 / Ubuntu 16.04 & Linux Mint 18 ###

            $ systemctl enable elasticsearch
            $ systemctl start elasticsearch

        ### RHEL 7 / CentOS 7 ###

            $ systemctl daemon-reload
            $ systemctl enable elasticsearch
            $ systemctl start elasticsearch


    ::: 

        $ nano /etc/elasticsearch/elasticsearch.yml

            ### IPv4 - acesso publico, ip do host onde esta instalado. ###

            network.bind_host: 192.168.0.1

            ### Usando da forma abaixo desabilita o acesso publico, passando a operar localmente ###

            network.bind_host: 127.0.0.1


    ::: 

        $ service elasticsearch restart
        $ curl -X GET 'http://localhost:9200'
        {
            "name" : "FkJ2rt9",
            "cluster_name" : "elasticsearch",
            "cluster_uuid" : "N5kIJNh7TS-5t_eynxyFaQ",
            "version" : {
                "number" : "5.6.10",
                "build_hash" : "b727a60",
                "build_date" : "2018-06-06T15:48:34.860Z",
                "build_snapshot" : false,
                "lucene_version" : "6.6.1"
            },
            "tagline" : "You Know, for Search"
       }

# testando o elastic

    ::: Testando Adiciona um documento

        $ curl -X POST 'http://10.0.9.39:9200/itzgeek/howtos/1' -d '{
        "Title" : "Installing Elasticsearch",
        "Date" :  "March 2015",
        "Tag" :   "Ubuntu, CentOS, LinuxMint"
        }'

        # saida
        {"_index":"itzgeek","_type":"howtos","_id":"1","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"created":true}

    ::: Pesquisa

        # consultar os dados no Elasticsearch.
        $ curl -X GET 'http://10.0.9.39:9200/itzgeek/howtos/1'

        # Anexar? Pretty = true para obter uma saída formatada.
        $ curl -X GET 'http://10.0.9.39:9200/itzgeek/howtos/1?pretty=true'

    ::: Update 

        $ curl -X POST 'http://10.0.9.39:9200/itzgeek/howtos/1' -d '{
        "Title" : "Installing Elasticsearch por neviim",
        "Date" :  "March 2017",
        "Tag" :   "Ubuntu 18, CentOS 7, LinuxMint 18"
        }'

    ::: Remover

        $ curl -X DELETE 'http://10.0.9.39:9200/itzgeek/howtos/1'

