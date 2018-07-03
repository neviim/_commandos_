# estudar como interagir com estes serviços via zabbix grafana

    ::: 
        $ zabbix_agentd -p > /tmp/agent.txt 


    ::: Utilizando zabbix_get para ter acesso as informaçoes de um cliente e seus estatus:

        # funcionando
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k agent.ping
        1 Up
            State:
                0   - Down, não respondendo
                1   - Up, respondendo

        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'system.hostname'
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'system.uptime'

        # service.info
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'service.info[EventLog, state]'
        0 running
            state:
                0   - running,
                1   - paused,
                2   - start pending,
                3   - pause pending,
                4   - continue pending,
                5   - stop pending,
                6   - stopped,
                7   - unknown,
                255 - no such service

        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'service.info[EventLog, startup]'
        0 automatic
            startup:
                0 - automatic,
                1 - automatic delayed,
                2 - manual,
                3 - disabled,
                4 - unknown,
                5 - automatic trigger start,
                6 - automatic delayed trigger start,
                7 - manual trigger start

        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'service.info[Spooler]'
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'service.info[EventLog, displayname]'
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'service.info[EventLog, startup]'
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'service.info[EventLog[Application]]'

        # outras opçoes.
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 

        # testando, não funciona.
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'system.cpu.load[all,avg1]'
        $ zabbix_get -s fac034378n1.fcn.edu.br -p 10050 -k 'vfs.fs.size[/,free]'
        $ zabbix_get -s fac034378n1.fcn.edu.br -k 'system.proc.num[,,,]'


        # teste config no server.
        $ zabbix_get -s fac034378n1.fcn.edu.br -k modbus_read_registers["/dev/ttyS1 9600 N",9,0x1518,3,l,1,0]
          http://www.ads.it/wp-content/uploads/2017/09/Using-Zabbix-in-an-IoT-Architecture_F.Fantoni.pdf



        ::: Windows service discovery: State of service "UserManager" (Gerenciador de Usuários)
        ::: Windows service discovery: State of service "DiagTrack" (Experiências e Telemetria de Usuário Conectado)
        ::: Windows service discovery: State of service "SENS" (Serviço de Notificação de Eventos do Sistema)
        :::	Windows service discovery: State of service "RasMan" (Gerenciador de conexão de acesso remoto)
        ::: Windows service discovery: State of service "ProfSvc" (Serviço de Perfil de Usuário)
        ::: Windows service discovery: State of service "Dnscache" (Cliente DNS)