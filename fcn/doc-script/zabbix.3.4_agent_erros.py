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

        
        # configuração atual de zabbix_agentd.conf
        $ nano /etc/zabbix/zabbix_agentd.conf

            PidFile=/var/run/zabbix/zabbix_agentd.pid
            LogFile=/var/log/zabbix/zabbix_agentd.log

            LogFileSize=0
            Server=10.0.9.18
            ListenPort=10050
            Hostname=zabbixsrv
            Include=/etc/zabbix/zabbix_agentd.d/*.conf

        