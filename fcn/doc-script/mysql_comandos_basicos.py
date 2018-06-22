# comandos basicos mysql

        # Comando 
        # 
            ::: Por padrão, o nível de segurança da senha vem como médio:

                $ show global variables like 'validate_password%';

                +--------------------------------------+--------+
                | Variable_name                        | Value  |
                +--------------------------------------+--------+
                | validate_password_check_user_name    | OFF    |
                | validate_password_dictionary_file    |        |
                | validate_password_length             | 8      |
                | validate_password_mixed_case_count   | 1      |
                | validate_password_number_count       | 1      |
                | validate_password_policy             | MEDIUM |
                | validate_password_special_char_count | 1      |
                +--------------------------------------+--------+

            ::: Logado com o usuário, a alteração de senha pode ser efetuada da seguinte forma:

                $ set password = password('novaPassword');

            ::: mysql -u root -p nome_do_banco_de_dados

                $ show global variables like 'default_password_lifetime';
                $ show databases;
                $ show tables;
                $ describe table_name;

                $ mysqldump -u root -p database_name --no-data > database_name.sql;
                $ mysql -u root -p database_name < database_name.sql;
                $ mysqldump -u user -p --all-databases > full_path_to\file.sql

                ::: Parâmetro: database_name
                    Substitua pelo nome do banco de dados ao qual deseja realizar a cópia.

                ::: Parâmetro: –no-data
                    Indica que desejamos criar uma cópia do bando de dados sem as informações contidas nas tabelas.
                
                ::: Parâmetro: –all-databases
                    Indica que desejamos exportar todas as bases de dados disponíveis no MySQL.


                $ drop table nome_da_tabela;
                $ drop database nome_do_banco_de_dados;


            
        # Lock/Unlok - Bloqueia e desbloqueira Usuarios
        #
            ::: 
            
                mysql> alter user 'ze2'@'localhost' ACCOUNT LOCK;
                mysql> alter user 'ze2'@'localhost' ACCOUNT UNLOCK;
                mysql> ALTER USER 'ze2'@'localhost' PASSWORD EXPIRE NEVER

                mysql> CREATE USER 'jeffrey'@'localhost' PASSWORD EXPIRE INTERVAL 90 DAY;
                mysql> ALTER USER  'jeffrey'@'localhost' PASSWORD EXPIRE INTERVAL 90 DAY;
