# Instala mysql

# Verifica se esta instalado

    $ netstat -anp tcp | findstr 3306
    TCP 0.0.0.0:3306 0.0.0.0:0 LISTENING


# Criar um acesso para um usuario com password utilizando um ip remoto: 

mysql> GRANT ALL ON database.* TO user@'203.0.113.2' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;


# Criar um access para todos databases:

mysql> GRANT ALL PRIVILEGES ON *.* TO 'user'@'203.0.113.2' IDENTIFIED BY 'password' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
FLUSH PRIVILEGES;


# Acessando:

    $ mysql -u root;

    mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'root';
    mysql> exit
    Bye

    $ mysql -u someuser -p "password" -h example.com
    $ mysql> 


