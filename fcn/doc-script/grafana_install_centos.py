# Instalando Grafana

    ::: configurando repositorio

        $ cd /etc/yum.repos.d/
        $ nano grafana.repo

            [grafana]
            name=grafana
            baseurl=https://packagecloud.io/grafana/stable/el/7/$basearch
            repo_gpgcheck=1
            enabled=1
            gpgcheck=1
            gpgkey=https://packagecloud.io/gpg.key https://grafanarel.s3.amazonaws.com/RPM-GPG-KEY-grafana
            sslverify=1
            sslcacert=/etc/pki/tls/certs/ca-bundle.crt

        # instala
        $ yum -y install grafana


    ::: agora precisa recarregar a configuração do gerenciador do systemd e, em seguida, iniciar o serviço Grafana.

        $ systemctl daemon-reload
        $ systemctl start grafana-server
        $ systemctl enable grafana-server


    ::: endereço de acesso.

        http://server-ip:3000

        # usuario defalt
        user padrão:
        
            user: admin
            pawd: admin


    ::: Grafana cli

        $ grafana-cli
        $ grafana-cli plugins list-remote
        
        $ grafana-cli plugins install grafana-clock-panel
        $ grafana-cli plugins install alexanderzobnin-zabbix-app

        $ systemctl restart grafana-server
        $ grafana-cli plugins ls


# condigirando zabbix plugin datasource

    ::: Settings

        Name: Zabbix_Mysql
        Type: Zabbix

    ::: HTTP
    
        Url....: http://10.0.9.41/zabbix/api_jsonrpc.php
        Access.: Server (Default)

    ::: Zabbix API details 

        # usuario e senha do zabbix server
        Username: Admin
        Password: zabbix

    
        ::: Ok, Zabbix API version: 3.4.10



# referencias
    # instalar plugin zabbix grafana
    https://www.youtube.com/watch?v=yYkyKpwk3uY