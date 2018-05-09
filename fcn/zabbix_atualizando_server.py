# Como atualizar o servidor Zabbix de 3.0.12 para 3.4.1

    - Passos 01

        - Parar zabbix server
        - Fazer backup databases

            $ service zabbix-server stop
            $ service zabbix-agent Stop 

            $ mysqldump -u root -p zabbix > zabbix_backup_08052018.sql


    - Passo 02

        - Adiciona source.list com atualizacao do repositorio zabbiz 3.4

            $ nano /etc/apt/source.list.d/zabbix.list

                deb http://repo.zabbix.com/zabbix/3.4/ubuntu trusty main
                deb-src http://repo.zabbix.com/zabbix/3.4/ubuntu trusty main


        - baixe por wget do repositoio o pacote deb

            # zabbix 3.0, utilizando este versão por ser compativel com o sistema atual.


            # zabbix 3.2, instalando no ubuntu server 18.04 (não funcionou com o sistema ubuntu server 18.04)
            $ wget http://repo.zabbix.com/zabbix/3.2/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.2-1+xenial_all.deb
            $ dpkg -i zabbix-release_3.2-1+xenial_all.deb
            $ apt update

            # zabbix 3.4.8 (nesta instalação deu erro ao instalar o zabbix server mysql, ubuntu server 18.04)
            $ wget http://repo.zabbix.com/zabbix/3.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.4-1+trusty_all.deb
            $ dpkg -i zabbix-release_3.4-1+trusty_all.deb
            $ apt update
            $ apt list --upgradable

            $ apt install zabbix-server-mysql 
            $ apt install zabbix-agent 
            $ apt install zabbix-frontend-php


    # verifica status da instalação

        $ systemctl start  zabbix-server.service
        $ systemctl status zabbix-server.service
        $ systemctl start  zabbix-agent.service
        $ systemctl status zabbix-agent.service
