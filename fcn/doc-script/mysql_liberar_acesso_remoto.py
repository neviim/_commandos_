# liberar o acesso remoto no banco 

    - abra um terminal e digite
        $ sudo vi /etc/mysql/my.cnf

        - comente as linhas
            bind-address = 127.0.0.1
            skip-external-locking

        - reinicie o servidor com o comando
            /etc/init.d/mysql restart
            sudo service mysql restart

        - entre no prompt do mysql com o comando:
            mysql –u root –p

        - Será solicitado a senha do usuário root para servidor MySQL, no prompt do MySQL digite:

            mysql> GRANT ALL PRIVILEGES ON zabbixdb.* TO zabbix@'%' IDENTIFIED By 'PwdZabbix#18';

            mysql> GRANT ALL ON *.* TO root@'%' IDENTIFIED By 'senhadoroot';
            mysql> GRANT ALL ON *.* TO zabbix@'%' IDENTIFIED By 'PwdZabbix#18';
            mysql> FLUSH PRIVILEGES;


# comandos basico mysql:

    mysql> SHOW GRANTS FOR ´root´
    mysql> SHOW GRANTS FOR 'root'@'localhost';

    mysql> SELECT User FROM mysql.user;
    mysql> SHOW DATABASES;

