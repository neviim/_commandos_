# Instalação de Zabbix 3.2 em CentOS 7

    $ yum -y update
    $ reboot
    $ groupadd zabbix
    $ useradd -g zabbix zabbix
    $ 
    
    # repositorio com zabbix 3.2
    $ yum -y install http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-server-mysql-3.2.11-1.el7.x86_64.rpm
    $ yum -y install http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-get-3.2.11-1.el7.x86_64.rpm 
    $ yum -y install http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-agent-3.2.11-1.el7.x86_64.rpm 
    $ yum -y install http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-proxy-mysql-3.2.11-1.el7.x86_64.rpm
    $ yum -y install http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-sender-3.2.11-1.el7.x86_64.rpm 
    $ yum -y install http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-web-3.2.11-1.el7.noarch.rpm 
    $ yum -y install http://repo.zabbix.com/zabbix/3.2/rhel/7/x86_64/zabbix-web-mysql-3.2.11-1.el7.noarch.rpm 

    # Se for instalar a versao 3.4 - recomendado
    $ yum -y install http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-1.el7.centos.noarch.rpm

    # Mysql server 5.7 com o firewall
    $ yum -y install https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
    $ yum -y install epel-release 
    $ yum -y install mysql-community-server.x86_64 mysql-community-devel.x86_64 firewalld rsync perl-DBI perl-CGI wget perl-Net-OpenSSH perl-IO-Pty-Easy

    # Mysql server 5.7 com zabbix server sem o firewall 
    $ yum -y install mysql-community-server.x86_64 mysql-community-devel.x86_64 rsync perl-DBI perl-CGI wget perl-Net-OpenSSH perl-IO-Pty-Easy
    $ yum -y install zabbix-agent.x86_64 zabbix-get.x86_64 zabbix-sender.x86_64 zabbix-server-mysql.x86_64 zabbix-web-mysql.noarch 
    
    $ /usr/sbin/zabbix_server -V
    zabbix_server (Zabbix) 3.4.10
    Revision 81503 4 June 2018, compilation time: Jun  4 2018 11:45:46

    Copyright (C) 2018 Zabbix SIA
    License GPLv2+: GNU GPL version 2 or later <http://gnu.org/licenses/gpl.html>.
    This is free software: you are free to change and redistribute it according to
    the license. There is NO WARRANTY, to the extent permitted by law.


    # desabilita iptables
    $ iptables -F

    # Ativa o mysql, gerando o ...
    $ systemctl enable mysqld
    $ systemctl start mysqld
    $ systemctl start httpd
    
    # contem a senha default da instalação do mysql server.
    $ grep "A temporary password is generated" /var/log/mysqld.log
    2018-06-18T12:52:21.160739Z 1 [Note] A temporary password is generated for root@localhost: QCE1xEwcM>Vj
    2018-06-20T14:25:37.637339Z 1 [Note] A temporary password is generated for root@localhost: %i2:v0Vjwp:9
    
    # caso queira trocar a senha mysql root
    $ mysqladmin -u root -p password '%i2:v0Vjwp:9'
    $ mysqladmin -u root -p password 'pwdroot'

    # entra no mysql server linha de comando
    $ mysql -u root -p

      mysql> CREATE DATABASE zabbix character set utf8 collate utf8_bin;
      mysql> CREATE USER 'zabbix@localhost' IDENTIFIED BY 'PwdZabbix#18';
      mysql> GRANT ALL PRIVILEGES ON zabbix.* TO 'zabbix@localhost' IDENTIFIED by 'PwdZabbix#18';
      mysql> FLUSH PRIVILEGES;
 
    # cria as tabelas sql no banco zabbix
    $ zcat create.sql.gz| mysql -u root -p zabbix

    # ou
    $ gunzip /usr/share/doc/zabbix-server-mysql-3.4.10/create.sql.gz
    $ mysql -u root -p zabbix < /usr/share/doc/zabbix-server-mysql-3.4.10/create.sql


    ::: Configurando zabbix_server.conf 

        $ nano /etc/zabbix/zabbix_server.conf

            ListenPort=10051
            TmpDir=/tmp
            AllowRoot=0
            LogFileSize=10
            DebugLevel=3

            LogFile=/var/log/zabbix/zabbix_server.log
            PidFile=/run/zabbix/zabbix_server.pid
            FpingLocation=/usr/sbin/fping
            AlertScriptsPath=/etc/zabbix/scripts
            ExternalScripts=/etc/zabbix/scripts

            DBHost=localhost
            DBName=zabbix
            DBUser=zabbix
            DBPassword=PwdZabbix#18
            DBPort=3306


    ::: Configura firewall

        $ systemctl start firewalld

        $ firewall-cmd --zone=public --add-port=3306/tcp --permanent
        $ firewall-cmd --zone=public --add-port=10050/tcp --permanent
        $ firewall-cmd --zone=public --add-port=10051/tcp --permanent
        $ firewall-cmd --zone=public --add-port=80/tcp --permanent
        
        $ systemctl stop firewalld
        $ systemctl start firewalld
        $ systemctl status firewalld
        $ systemctl restart firewalld


    ::: Dar acesso remoto ao mysql server, mysql_permissao_acesso_remoto

        $ mysql -u root -p

        mysql> GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY 'Pwd2018#';
        mysql> GRANT ALL ON *.* TO 'zabbix'@'%' IDENTIFIED BY 'PwdZabbix#18';
        mysql> exit;
        $ 


    ::: Ao usar o SELinux, precisamos permitir que o Apache se comunique com o Zabbix:

        $ setsebool -P httpd_can_connect_zabbix=1


    ::: Configura httpd.conf

        $ nano /etc/httpd/conf/httpd.conf
	        
            Listen 10.0.9.93:80
	        ServerName zabbixsrv.fcn.edu.br:80
	        AddDefaultCharset UTF-8

    ::: Configura zabbix.conf

        $ nano /etc/httpd/conf.d/zabbix.conf

            php_value date.timezone America/Sao_Paulo



    ::: Ativando e startando serviço, httpd, zabbix_server

        $ systemctl enable httpd
        $ systemctl enable mysqld
        $ systemctl enable zabbix-server
        
        $ systemctl start httpd
        $ systemctl start mysqld
        $ systemctl start zabbix-server
        
        $ systemctl status httpd
        $ systemctl status mysqld
        $ systemctl status zabbix-server

        $ systemctl restart httpd
        $ systemctl restart mysqld
        $ systemctl restart zabbix-server


    ::: lista os 3 ultimos logs
    
        $ tail -3 /var/log/zabbix/zabbix_server.log



    ::: Acessando o server

        http://localhost/zabbix/
        http://10.0.9.93/zabbix

        Username: Admin 
        Password: zabbix 




# Instalando o zabbix agente

    ::: instalar agente

        $ yum list installed | grep zabbix
        $ yum install zabbix-agent
        $ yum makecache

        # config agent
        $ nano /etc/zabbix/zabbix_agentd.conf

            Server=192.168.1.40
            ServerActive=192.168.1.40
            Hostname=Hostname_deste_agente

        # start, status, stop
        $ systemctl stop zabbix-agent.service
        $ systemctl start zabbix-agent.service
        $ systemctl restart zabbix-agent.service
        

        # v3.4, Item vfs.dir.size Monitorando tamanho das Pastas Nativamente.
        $ zabbix_agentd -p | grep vfs.dir.size
        vfs.dir.size[/var/log]                        [u|4179289]





# Upgrade zabbix server 3.2 to 3.4

    ::: http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/

        $ yum -y install http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-release-3.4-1.el7.centos.noarch.rpm

        $ yum update http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-server-mysql-3.4.9-1.el7.x86_64.rpm



# comandos basicos monitoramento


    :::
        # tools
        $ netstat -plntu

        # systemctl
        $ systemctl start firewalld
        $ systemctl enable firewalld

        # firewall
        $ firewall-cmd --zone=public --add-port=80/tcp --permanent
        $ firewall-cmd --add-service={http,https} --permanent
        $ firewall-cmd --add-port={10051/tcp,10050/tcp} --permanent

        $ firewall-cmd --reload
        $ firewall-cmd --list-all

        # Iptables configurando
        $ iptables -A INPUT -p tcp --dport 80 -j ACCEPT
        $ iptables -A INPUT -p tcp -s 10.0.9.18 --dport 10050 -m state --state NEW,ESTABLISHED -j ACCEPT


        # mysql
        $ mysql_upgrade -u root -p --force

        $ mysql -u root -p
        
            mysql> show databases;
            mysql> 


        # zabbix_get
        $ zabbix_get -s 127.0.0.1 -p 10050 -k "proc.num[]"
        159

        $ ps -aux | grep zabbix

        # extrair pacote rmp
        $ cd /tmp/test
        $ rpm2cpio zabbix-server-mysql-3.2.11-1.el7.x86_64.rpm | cpio -di

        $ yum install yum-utils -y
        $ repoquery -qi zabbix-server-mysql



        # referencia de uso do comento sed
        [referencia]$ sudo sed -i 's/^max_execution_time.*/max_execution_time=600/' /etc/php.ini
        [referencia]$ sudo sed -i 's/^max_input_time.*/max_input_time=600/' /etc/php.ini
        [referencia]$ sudo sed -i 's/^memory_limit.*/memory_limit=256M/' /etc/php.ini
        [referencia]$ sudo sed -i 's/^post_max_size.*/post_max_size=32M/' /etc/php.ini
        [referencia]$ sudo sed -i 's/^upload_max_filesize.*/upload_max_filesize=16M/' /etc/php.ini
        [referencia]$ sudo sed -i "s/^\;date.timezone.*/date.timezone=\'Europe\/Brussels\'/" /etc/php.i

        [referencia]$ sudo sed -i 's/^# DBPassword=.*/DBPassword=secretpassword/' /etc/zabbix/zabbix_server.conf



# trocar senha root veriticar em:

    ::: mysql_troca-senha-root.py




# ERROS - basicos e frequente nesta instalação.

    ::: Cannot bind socket to "/var/run/zabbix/zabbix_server_alerter.sock": [13] Permission denied.

        -  Pode ser reparado fazendo o download e importando o pacote do módulo selinux fornecido pelo suporte oficial.

            $ getsebool -a | grep zabbix
            httpd_can_connect_zabbix --> off
            zabbix_can_network --> off

            $ setsebool -P httpd_can_connect_zabbix on
            $ setsebool -P zabbix_can_network on

            $ systemctl stop mysqld
            $ systemctl stop zabbix-server
            $ systemctl stop zabbix-agent

            $ yum install -y policycoreutils-python
            $ wget -O zabbix_server_add.te https://support.zabbix.com/secure/attachment/53320/53320_zabbix_server_add.te –no-check-certificate

            $ checkmodule -M -m -o zabbix_server_add.mod zabbix_server_add.te
            $ semodule_package -o zabbix_server_add.pp -m zabbix_server_add.mod
            $ semodule -i zabbix_server_add.pp

            $ systemctl restart zabbix-server
            $ systemctl restart zabbix-agent
            $ systemctl start mysqld
            $ systemctl start zabbix-server
            $ systemctl start zabbix-agent
            
            # resolvido com isso.








# referencias

    # Instalação de Zabbix 3.2 em CentOS 7
    http://nervinformatica.com.br/blog/index.php/2017/06/28/instalacao-de-zabbix-3-2-em-centos-7/

    # Instalação de Zabbix Server 2.4.5 em CentOS 7.1 com MySQL 5.6
    http://nervinformatica.com.br/blog/index.php/2015/08/04/instalacao-de-zabbix-server-2-4-5-em-centos-7-1-com-mysql-5-6/

    #
    http://jensd.be/393/linux/install-zabbix-on-centos-7-or-rhel-7
    http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/

    # referencia em video no youtube (Jorge Pretel)
    https://www.youtube.com/watch?v=RdnAZ1Z-IJg&t=17s

