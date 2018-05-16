# Instalar zabbix server:

    - referencias para o acesso:
        Database type       MySQL
        Database server     localhost
        Database port       default
        Database name       zabbix
        Database user       zabbix
        Database password   zabbix

        Zabbix server       localhost
        Zabbix server port      10051

# instalar pacote do repositorio ubunto server 18
#  
    $ apt install zabbix-server-mysql
    $ apt install zabbix-frontend-php
    $ apt install zabbix-agent
    $ service zabbix-server status
    $ zcat /usr/share/zabbix-server-mysql/{schema,images,data}.sql.gz | mysql -uzabbix -pzabbix zabbix

    # Alterar a variavel DBPassword do conf zabbix, para senha que foi criada para o banco zabbix.

        $ sudo nano /etc/zabbix/zabbix_server.conf

            DBPassword=password

  
        # podebdo zerar o arquivo conf e adicionar estas variaveis:

            Server=<IP of your zabbix server>
            Hostname=<Name of your proxy>
            DBName=<Name of your proxy database>
            DBUser=<Name of your proxy user>
            DBPassword=<Password of your proxy user>    


    # restarta os server:
        $ service zabbix-server restart
        $ service zabbix-agent restart
        $ service apache2 restart
    
        # verifica status de funcionamento:
        $ service zabbix-server status
        $ service zabbix-agent status
        $ service apache2 status    


# caso nao os agentes nao link, precisa liberar as portas:

    [$server] # sudo ufw allow 10050/tcp
    [$server] # sudo ufw allow 10051/tcp
    [$server] # sudo ufw reload


# Configura PHP

    post_max_size = 16M
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

        $ cp /usr/share/doc/zabbix-frontend-php/examples/apache.conf /etc/apache2/sites-available/zabbix.conf

            # abilitar o modo de aria


            # apos fazer isso e o servidr zabix não subir, realize este procedimento...

                $ cd /etc/apache2/sites-available
                $ mv zabbix.conf /etc/apache2/conf-available
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


        

                        