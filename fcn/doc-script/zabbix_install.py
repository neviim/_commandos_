# Instalar zabbix server:

    :: removendo zabbix

        $ apt search zabbix | grep zabbix

        $ apt remove zabbix-server-mysql
        $ apt remove zabbix-frontend-php
        $ apt remove zabbix-agent


# instalar pacote do repositorio ubunto server 18.04

    :: instalar

        $ apt install zabbix-server-mysql
        $ apt install zabbix-frontend-php
        $ apt install zabbix-agent

        $ service zabbix-server status


    :: Criar banco de dados mysql do zabbix:

        $ mysql -uroot -p<password>
          mysql> create database zabbix character set utf8 collate utf8_bin;
          mysql> grant all privileges on zabbix.* to zabbix@localhost identified by '<password>';
          mysql> quit;

        :: Versão 3.0

            $ zcat /usr/share/zabbix-server-mysql/{schema,images,data}.sql.gz | mysql -uzabbix -p zabbix
            Enter password: zabbix

        :: Versão 3.4

            $ zcat /usr/share/doc/zabbix-server-mysql/create.sql.gz | mysql -uzabbix -p zabbix
            Enter password: zabbix

    # Alterar a variavel DBPassword do conf zabbix, para senha que foi criada para o banco zabbix.

        - referencias para o acesso:

            Database type       MySQL
            Database server     localhost
            Database port       default
            Database name       zabbix
            Database user       zabbix
            Database password   zabbix

            Zabbix server       localhost
            Zabbix server port  10051


        :: configurando zabbix server

            $ sudo nano /etc/zabbix/zabbix_server.conf

                # pode zerar o arquivo conf e adicionar estas variaveis:
                Server=0.0.0.0
                Hostname=zabbix
                DBName=zabbix
                DBUser=zabbix
                DBPassword=zabbix


            :: uma referencia das variaveis que podem conter no arquivo acima:

                ListenPort=10051
                LogFile=/var/log/zabbix/zabbix_server.log
                PidFile=/var/log/zabbix/zabbix_server.pid
                LogFileSize=100
                DebugLevel=3
                DBHost=127.0.0.1
                DBName=zabbix
                DBUser=zabbix
                DBPassword=senha
                DBSocket=/var/lib/mysql/mysql.sock
                DBPort=3306
                StartPollers=50
                StartPollersUnreachable=15
                StartTrappers=20
                StartPingers=15
                StartDiscoverers=15
                StartHTTPPollers=5
                StartTimers=5
                HousekeepingFrequency=1
                MaxHousekeeperDelete=1000
                SenderFrequency=120
                CacheSize=16M
                CacheUpdateFrequency=25
                StartDBSyncers=8
                HistoryCacheSize=16M
                TrendCacheSize=5M
                HistoryTextCacheSize=16M
                ValueCacheSize=8M
                Timeout=15
                UnreachablePeriod=45
                UnavailableDelay=60
                UnreachableDelay=15
                FpingLocation=/usr/sbin/fping
                LogSlowQueries=2
                StartProxyPollers=20
                ProxyConfigFrequency=240
                ProxyDataFrequency=60
                StartIPMIPollers=0
                StartJavaPollers=0
                StartVMwareCollectors=0
                VMwareFrequency=3600
                StartSNMPTrapper=0


        :: restart, stop, start

            $ systemctl restart zabbix-server zabbix-agent apache2

            $ systemctl start zabbix-server.service
            $ systemctl start zabbix-agent.service

            $ systemctl status zabbix-server.service
            $ systemctl atatus zabbix-agent.service

            # restarta os server:
            $ service zabbix-server restart
            $ service zabbix-agent restart
            $ service apache2 restart
        
            # verifica status de funcionamento:
            $ service zabbix-server status
            $ service zabbix-agent status
            $ service apache2 status    


# Configura PHP

    :: php.ini

        $ php -i | grep php.ini
        Configuration File (php.ini) Path => /etc/php/7.2/cli

        $ nano /etc/php/7.2/cli/php.ini

            post_max_size = 16M
            max_execution_time = 300
            max_input_time = 300
            always_populate_raw_post_data = -1
            date.timezone = UTC 
    

    # copiando o arquivo de conf do exemplo do zabbix php

        $ cp /usr/share/doc/zabbix-frontend-php/examples/zabbix.conf.php.example /etc/zabbix/zabbix.conf.php

            <?php
            // Zabbix GUI configuration file.
            global $DB;

            $DB['TYPE']                     = 'MYSQL';
            $DB['SERVER']                   = 'localhost';
            $DB['PORT']                     = '0';
            $DB['DATABASE']                 = 'zabbix';
            $DB['USER']                     = 'zabbix';
            $DB['PASSWORD']                 = 'zabbix';

            // Schema name. Used for IBM DB2 and PostgreSQL.
            $DB['SCHEMA']                   = '';
            $ZBX_SERVER                     = 'localhost';
            $ZBX_SERVER_PORT                = '10051';
            $ZBX_SERVER_NAME                = '';

            $IMAGE_FORMAT_DEFAULT           = IMAGE_FORMAT_PNG;


        $ cp /usr/share/doc/zabbix-frontend-php/examples/apache.conf /etc/apache2/conf-available/zabbix.conf

            # apos fazer isso e o servidr zabix não subir, realize este procedimento...

                $ cat /etc/apache2/conf-available/zabbix.conf
                $ cd /etc/apache2/conf-enabled

                $ ln -s ../conf-available/zabbix.conf
                $ ls -ls /usr/share/zabbix

                $ service apache2 status

                # no browse

                    http://10.0.9.41/zabbix/
                    localhost/zabbix/

                    # ok, abrindo a tela de login

                        Usuario.: Admin
                        Password: zabbix

    
    # Instalando o Agente zabbix no proprio servidor dele...

        $ cd /etc/zabbix
        $ nano zabbix_agentd.conf

            Server=127.0.0.1
            ListenPort=10050
            ServerActive=127.0.0.1
            Hostname=Zabbix-server

        $ service zabbix-agent restart

    
    # local do download dos agentes do zabbix

        https://www.zabbix.com/download_agents



# caso nao funcione os agentes, precisa liberar o zabbix server ou agente ou as portas:

    $ ufw allow 10050/tcp
    $ ufw allow 10051/tcp
    $ ufw reload



# referencia
    # Grafico de parametro de mysql
    http://www.foreverlakers.com/page/4/?s=https