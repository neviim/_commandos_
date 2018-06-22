# grafana plugins

    ::: endereço de acesso.

        http://server-ip:3000

        # usuario defalt
        user padrão:
        
            user: admin
            pawd: admin


    ::: Grafana plugins

        $ grafana-cli
        $ grafana-cli plugins list-remote
        
        $ grafana-cli plugins install grafana-clock-panel
        $ grafana-cli plugins install alexanderzobnin-zabbix-app
        $ grafana-cli plugins install jasonlashua-prtg-datasource
        $ grafana-cli plugins install natel-discrete-panel





        # restarta o servidor.
        $ systemctl restart grafana-server
        $ grafana-cli plugins ls