# zabbix get

    ::: 

        $ zabbix_get -s zabbixsrv.fcn.edu.br -k 'agent.version'
        3.4.10

        $ zabbix_get -s zabbixsrv.fcn.edu.br -k 'agent.ping'
        1

        $ zabbix_get -s pdlab01.fcn.edu.br -p 10050 -k "system.cpu.load[all,avg1]" --version

        # retorna a versão do agent instalado
        $ zabbix_get -s 10.0.9.18 -k agent.version


#fre%4lk10*