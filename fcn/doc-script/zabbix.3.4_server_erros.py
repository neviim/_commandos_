# Alguns erros ocorrido no zabbix server

    ::: Ago 13 09:25:21 zabbixsrv systemd[1]: Starting Zabbix Server...
    ::: Ago 13 09:25:21 zabbixsrv systemd[1]: PID file /run/zabbix/zabbix_server.pid not readable (yet?) after start.

        $ zabbix_server -V
        $ ls -la /tmp/zabbix_server.pid
        -rw-rw-r--. 1 zabbix zabbix 5 Ago 13 09:25 /tmp/zabbix_server.pid

        # O arquivo pid está sendo criado, mas não parece que o Zabbix Server tente usá-lo quando um stop / restart for chamado.
        $ stat /usr/sbin/zabbix_agentd
        File: “/usr/sbin/zabbix_agentd”
        Size: 577248          Blocks: 1128       IO Block: 4096   arquivo comum
        Device: fd00h/64768d    Inode: 33572644    Links: 1
        Access: (0755/-rwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
        Context: system_u:object_r:zabbix_agent_exec_t:s0
        Access: 2018-08-13 08:14:58.528959397 -0300
        Modify: 2018-07-30 08:46:53.000000000 -0300
        Change: 2018-08-08 08:01:05.505507797 -0300

        $ stat /usr/sbin/zabbix_server
        File: “/usr/sbin/zabbix_server” -> “/etc/alternatives/zabbix-server”
        Size: 31              Blocks: 0          IO Block: 4096   ligação simbólica
        Device: fd00h/64768d    Inode: 33619862    Links: 1
        Access: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
        Context: unconfined_u:object_r:bin_t:s0
        Access: 2018-08-13 08:14:58.523959360 -0300
        Modify: 2018-08-08 08:01:04.789502174 -0300
        Change: 2018-08-08 08:01:04.789502174 -0300
        Birth: -

        $ stat /etc/alternatives/zabbix-server
        File: “/etc/alternatives/zabbix-server” -> “/usr/sbin/zabbix_server_mysql”
        Size: 29              Blocks: 0          IO Block: 4096   ligação simbólica
        Device: fd00h/64768d    Inode: 67276121    Links: 1
        Access: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
        Context: unconfined_u:object_r:etc_t:s0
        Access: 2018-08-13 08:14:58.523959360 -0300
        Modify: 2018-08-08 08:01:04.789502174 -0300
        Change: 2018-08-08 08:01:04.789502174 -0300
        Birth: -

        Obs: 'O agente do Zabbix pode iniciar/parar/reiniciar sem problemas, com a linha do arquivo pid comentada no arquivo conf ou com um caminho customizado.'
             'Última versão do CentOS Linux 7.2.1511 (Core) e Zabbix REPO, o server tem um problema que precisa ser colocado o arquivo Pid em /tmp'

        #
        # Solucionando...
        #
        
        # altere o PidFile para...
        $ nano /etc/zabbix/zabbix_server.conf

            PidFile=/tmp/zabbix_server.pid
            #PidFile=/var/run/zabbix/zabbix_server.pid

        $ nano /usr/lib/systemd/system/zabbix-server.service

            [Service]
            Environment="CONFFILE=/etc/zabbix/zabbix_server.conf"
            EnvironmentFile=-/etc/sysconfig/zabbix-server
            Type=forking
            Restart=on-failure
            PIDFile=/tmp/zabbix_server.pid
            #PIDFile=/run/zabbix/zabbix_server.pid
            KillMode=control-group
            ExecStart=/usr/sbin/zabbix_server -c $CONFFILE
            ExecStop=/bin/kill -SIGTERM $MAINPID
            RestartSec=10s

        $ systemctl start zabbix-server.service
        $ systemctl status zabbix-server.service

            ● zabbix-server.service - Zabbix Server
            Loaded: loaded (/usr/lib/systemd/system/zabbix-server.service; enabled; vendor preset: disabled)
            Active: active (running) since Seg 2018-08-13 10:20:25 -03; 9s ago
            Process: 25432 ExecStart=/usr/sbin/zabbix_server -c $CONFFILE (code=exited, status=0/SUCCESS)
            Main PID: 25434 (zabbix_server)
            CGroup: /system.slice/zabbix-server.service
                    ├─25434 /usr/sbin/zabbix_server -c /etc/zabbix/zabbix_server.conf
                    ├─25439 /usr/sbin/zabbix_server: configuration syncer [waiting 25 sec for processes]
                    ├─25440 /usr/sbin/zabbix_server: alerter #1 started