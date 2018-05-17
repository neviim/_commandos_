# Lista serviços:

    :: comandos basicos:

        $ systemctl start application.service
        $ systemctl restart application.service
        $ systemctl stop application.service


    :: lista serviços ativos: 

        $ systemctl list-unit-files | grep enabled
        $ systemctl list-unit-files | grep zabbix


        :: caso presice verificar de outra forma:

            $ service zabbix-server status


    :: Para iniciar um serviço no boot, utilize o comando enable:

        $ systemctl enable application.service



    