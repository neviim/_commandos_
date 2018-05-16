# Servidor zabbix, teste de aplicações (VM) 

    :: serviços instalados nele:

        - apache2
        - mysql
        - zabbix
        - grafana
        - netdata
        - glances
        - fluentd

        - php 7.2
        - python 3.4

        - http://10.0.9.41/phpinfo.php
        - http://10.0.9.41/wordpress
        - http://10.0.9.41/zabbix
        - http://10.0.9.41:3000                     # grafana
        - http://10.0.9.41:8888                     # fluentd



        # recursos:

            - curl -X POST -d 'json={"json":"message"}' http://localhost:8888/debug.test


    :: procedimento de verificação para os serviços que esta estartado nele.

        - subir zabbix-server
            $ systemctl start zabbix-server.service
            $ systemctl status zabbix-server.service



# alguns comandos basicos para verificar integridade 

    $ systemctl list-unit-files                     # listas todos os serviços ativos.
    $ service --status-all                          # listas todos resumidamente.

    $ mysql -u root -p
      mysql> SELECT User, Host FROM mysql.user;

    $ tail -f zabbix-server/zabbix_server.log

    $ netstat -tupln 