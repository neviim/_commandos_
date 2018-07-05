# IMPORTANTE: Configure os agentes do Zabbix para o modo ativo, reconfigure os itens para serem verificações ativas. 

    ::: inicializando o cliente agente zabbix:

        λ cd c:\zabbix\bin\win64
        λ  .\zabbix_agentd.exe -i -c C:\ProgramData\zabbix\zabbix_agentd.win.conf
        zabbix_agentd.exe [1332]: service [Zabbix Agent] installed successfully
        zabbix_agentd.exe [1332]: event source [Zabbix Agent] installed successfully

        # na versao 3.4
        λ cd c:\zabbix\bin\win64
        λ  .\zabbix_agentd.exe -d -c C:\ProgramData\zabbix\zabbix_agentd.win.conf
        zabbix_agentd.exe [18344]: service [Zabbix Agent] uninstalled successfully
        zabbix_agentd.exe [18344]: event source [Zabbix Agent] uninstalled successfully

        - 'só instalar novamente'

        λ .\zabbix_agentd.exe -V
        zabbix_agentd Win64 (service) (Zabbix) 3.4.6
        Revision 76819 15 January 2018, compilation time: Jan 15 2018 10:43:42


    ::: Novidades

        # v3.4, Item vfs.dir.size Monitorando tamanho das Pastas Nativamente.
        $ zabbix_agentd -p | grep vfs.dir.size
        vfs.dir.size[/var/log]     [u|4179289]


        $ zabbix_get -s 192.168.0.131 -k system.hostname

        $ zabbix_get -s 192.168.0.131 -k vfs.dir.size[C:/youtube]
        $ zabbix_get -s 192.168.0.131 -k vfs.dir.size[C:/youtube, txt]



C:\ProgramData\zabbix\
