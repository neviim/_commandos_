Cannot display item queue.

::: Ao analisar constatei que tinham algumas linhas duplicadas no arquivo zabbix_server.conf que em minha 
    distribuição fica localizado em: usr/local/etc/zabbix_server.conf

    - Por exemplo: 

        Tinha uma linha no começo e outra no meio do arquivo com o seguinte conteúdo:
        LogFile=/tmp/zabbix_server.log
        LogFileSize=2

        Isso ocorreu no copiar e colar de um tutorial que utilizei como referência.

        Após comentar as linhas duplicadas, o serviço iniciou de forma correta.




::: Details (Adminidtration - Queue)

    # opção de mensagens de erro
    Connection to Zabbix server "localhost" refused. Possible reasons:
    1. Incorrect server IP/DNS in the "zabbix.conf.php";
    2. Security environment (for example, SELinux) is blocking the connection;
    3. Zabbix server daemon not running;
    4. Firewall is blocking TCP connection.
    Connection refused

    # opção de mensagem de erro
    Empty response received from Zabbix server "localhost".


    ::: Verificar...

        $ iptables -L 
        $ iptables -F
        $ iptables -X
        $ iptables -Z 
        $ iptables -S 

        # no arquivo de configuração
        firewall_stop(){
            iptables -F
            iptables -X
            iptables -P INPUT ACCEPT
            iptables -P FORWARD ACCEPT
            iptables -P OUTPUT ACCEPT
        }


        $ nano /etc/zabbix/web/zabbix.conf.php
        $ systemctl status mysqld.service
        $ mysql -u zabbix -p

        $ ps -aux | grep zabbix_server
        $ find /usr |grep zabbix_server
        $ find /etc |grep zabbix_server

        $ sed -e '/^#/d' -e '/^$/d' /etc/zabbix/zabbix_server.conf
        $ sed -e '/^#/d' -e '/^$/d' /etc/zabbix/zabbix_agentd.conf


    ::: zabbix_server.conf 

        



        # Arquivo de configuração do Zabbix Server para alta performance e coletas intensas em grande escala.

        SocketDir=/var/run/zabbix
        LogFile=/tmp/zabbix_server.log
        PidFile=/var/run/zabbix/zabbix_server.pid
        SNMPTrapperFile=/tmp/snmptrap.log
        AlertScriptsPath=/usr/lib/zabbix/alertscripts

        #
        DBName=zabbix
        DBUser=zabbix
        DBPassword=PwdZabbix#18

        #
        Timeout=5
        LogFileSize=0
        StartPollers=60
        StartPollersUnreachable=30
        StartPingers=30
        ListenIP=0.0.0.0
        LogSlowQueries=3000


    ::: zabbix_agentd.conf

        PidFile=/var/run/zabbix/zabbix_agentd.pid
        LogFile=/var/log/zabbix/zabbix_agentd.log
        LogFileSize=0
        Server=10.0.9.18
        ListenPort=10050
        Hostname=zabbixsrv
        Include=/etc/zabbix/zabbix_agentd.d/*.conf  


    ::: restart o serviço 

        $ systemctl stop zabbix-server.service
        $ zabbix systemctl start zabbix-server.service
        $ zabbix systemctl status zabbix-server.service

        $ cat /tmp/zabbix_server.log

            29377:20180724:120131.496 Zabbix Server stopped.  Zabbix 3.4.11 (revision 82160).
            29597:20180724:120141.776 Starting Zabbix Server. Zabbix 3.4.11 (revision 82160).
            29597:20180724:120141.777 ****** Enabled features ******
            29597:20180724:120141.777 SNMP monitoring:           YES
            29597:20180724:120141.777 IPMI monitoring:           YES
            29597:20180724:120141.777 Web monitoring:            YES
            29597:20180724:120141.777 VMware monitoring:         YES
            29597:20180724:120141.777 SMTP authentication:       YES
            29597:20180724:120141.777 Jabber notifications:      YES
            29597:20180724:120141.777 Ez Texting notifications:  YES
            29597:20180724:120141.777 ODBC:                      YES
            29597:20180724:120141.777 SSH2 support:              YES
            29597:20180724:120141.777 IPv6 support:              YES
            29597:20180724:120141.778 TLS support:               YES
            29597:20180724:120141.778 ******************************
            29597:20180724:120141.778 using configuration file: /etc/zabbix/zabbix_server.conf
            29597:20180724:120141.780 current database version (mandatory/optional): 03040000/03040007
            29597:20180724:120141.780 required mandatory version: 03040000
            29597:20180724:120141.991 server #0 started [main process]
            29599:20180724:120141.991 server #1 started [configuration syncer #1]


        # Esta ok...
        $ telnet 10.0.9.18 10051
        Trying 10.0.9.18...
        Connected to 10.0.9.18.
        Escape character is '^]'.
        Connection closed by foreign host.

        # Com problema...
        $ telnet 10.0.9.18 10051
        Trying 10.0.9.18...
        telnet: connect to address 10.0.9.18: Connection refused


        $ netstat --tcp --numeric
        $ netstat --tcp -l
        $ netstat -na | grep tcp

        $ netstat -ntlp
        Conexões Internet Ativas (sem os servidores)
        Proto Recv-Q Send-Q Endereço Local          Endereço Remoto         Estado      PID/Program name
        tcp        0      0 127.0.0.1:8125          0.0.0.0:*               OUÇA       2963/netdata
        tcp        0      0 0.0.0.0:19999           0.0.0.0:*               OUÇA       2963/netdata
        tcp        0      0 0.0.0.0:10050           0.0.0.0:*               OUÇA       1060/zabbix_agentd
        tcp        0      0 0.0.0.0:10051           0.0.0.0:*               OUÇA       7391/zabbix_server
        tcp        0      0 127.0.0.1:199           0.0.0.0:*               OUÇA       1046/snmpd
        tcp        0      0 0.0.0.0:22              0.0.0.0:*               OUÇA       1049/sshd
        tcp        0      0 127.0.0.1:25            0.0.0.0:*               OUÇA       1566/master
        tcp6       0      0 ::1:8125                :::*                    OUÇA       2963/netdata
        tcp6       0      0 :::19999                :::*                    OUÇA       2963/netdata
        tcp6       0      0 :::10050                :::*                    OUÇA       1060/zabbix_agentd
        tcp6       0      0 :::3306                 :::*                    OUÇA       2623/mysqld
        tcp6       0      0 :::80                   :::*                    OUÇA       337/httpd
        tcp6       0      0 :::22                   :::*                    OUÇA       1049/sshd
        tcp6       0      0 ::1:25                  :::*                    OUÇA       1566/master


    ::: firewalld

        $ cat /etc/firewalld/firewalld.conf

            #########################
            # Variaveis do firewall #
            #########################

            CAIXA1="200.201.174.207"
            CAIXA2="200.201.173.68"
            LAN="eth0"
            WAN="eth1"
            DIR="/etc/firewall"
            CAT="/bin/cat"
            ECHO="/bin/echo"

            BLOCKALL="ips_block_all"
            ALLOWALL="ips_allow_all"

            ########################
            ## REGRA ACESSO TOTAL ##
            ########################

            for n in `$CAT $DIR/$ALLOWALL`
            do
            iptables -A FORWARD -s $n -m state --state NEW -j ACCEPT
            iptables -A FORWARD -d $n -m state --state NEW -j ACCEPT
            done
