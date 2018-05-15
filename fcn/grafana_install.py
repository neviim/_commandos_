# instalando grafana

    :: versao estavel

        $ wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana_5.1.2_amd64.deb
        $ sudo apt-get install -y adduser libfontconfig
        $ sudo dpkg -i grafana_5.1.2_amd64.deb       

    :: conficurando repositorio

        $ nano /etc/apt/sources.d/grafana.list

            deb https://packagecloud.io/grafana/stable/debian/ stretch main

        # adicione a chave Package Cloud. Isso permite que você instale pacotes assinados.
        $ curl https://packagecloud.io/gpg.key | sudo apt-key add -

        :: Em algumas versões mais antigas do Ubuntu e Debian você pode precisar instalar 
           o pacote apt-transport-https que é necessário para buscar pacotes via HTTPS.

           $ apt install -y apt-transport-https


        :: detalhes da instalação:

            Installs binary to '/usr/sbin/grafana-server'
            Installs Init.d script to '/etc/init.d/grafana-server'
            Creates default file (environment vars) to '/etc/default/grafana-server'
            Installs configuration file to '/etc/grafana/grafana.ini'
            Installs systemd service (if systemd is available) name 'grafana-server.service'
            The default configuration sets the log file at '/var/log/grafana/grafana.log'
            The default configuration specifies an sqlite3 db at '/var/lib/grafana/grafana.db'
            Installs HTML/JS/CSS and other Grafana files at '/usr/share/grafana'


    :: inicializando serviço:

        $ systemctl daemon-reload
        $ systemctl start grafana-server
        $ systemctl status grafana-server


        :: Ative o serviço systemd para que o Grafana inicie na inicialização.

            $ systemctl enable grafana-server.service

            - O arquivo de serviço systemd e o script init.d usam o arquivo 
              localizado em '/etc/default/grafana-server' para as variáveis 
              ​​de ambiente usadas ao iniciar o back-end. Aqui você pode substituir 
              o diretório de log, diretório de dados e outras variáveis.

              Por padrão, o Grafana irá gera os log em '/var/log/grafana'

            - A configuração padrão especifica um banco de dados sqlite3 localizado 
              em '/var/lib/grafana/grafana.db'. Por favor, faça backup desse banco de 
              dados antes de fazer upgrades. Você também pode usar o MySQL ou Postgres 
              como o banco de dados Grafana, conforme detalhado na página de configuração.

              O arquivo de configuração está localizado em '/etc/grafana/grafana.ini'. 
              Vá para a página de configuração para obter detalhes sobre todas essas opções.



    :: iniciando

        ip_maquina:3000

        - user padrão:

            user: admin
            pawd: admin

    :: instalar plugin do grafana - zabbiz

        $ grafana-cli plugins install alexanderzobnin-zabbix-app

            - O plugin será instalado em seu diretório de plugins do grafana; 
              o padrão é '/var/lib/grafana/plugins'.

            - Para ativar o aplicativo, clique na guia Config. Siga as instruções 
              fornecidas com o aplicativo e clique em Ativar. O aplicativo e todas 
              as novas páginas da interface do usuário agora podem ser acessadas no 
              menu principal, conforme projetado pelo criador do aplicativo.




# comandos do grafana-cli

    :: aplicado

        $ grafana-cli plugins list-remote

        $ grafana-cli plugins install alexanderzobnin-zabbix-app

        $ service grafana-server restart

        :: baixando direto do github

            $ cd /var/lib/grafana/plugins
            $ git clone https://github.com/alexanderzobnin/grafana-zabbix


        :: Você precisa do NodeJS, npm e Grunt para construir o plugin a partir das fontes. 
           Leia mais sobre as versões requeridas em Grafana docs.

            $ git clone https://github.com/alexanderzobnin/grafana-zabbix.git
            $ cd grafana-zabbix
            $ npm install
            $ npm install -g grunt-cli
            $ grunt


        :: construindo plugins

            - Plugin será construído em dist/diretório. Então você pode copiá-lo 
              para o diretório de plugins do seu grafana ou configurar o caminho 
              para o plugin compilado em grafana config:

              [plugin.zabbix]
              path = /home/your/clone/dir/grafana-zabbix/dist

# condigirando zabbix plugin datasource

    :: Settings

        Name: Zabbix Conect
        Type: Zabbix

    :: HTTP
    
        Url....: http://10.0.9.41/zabbix/api_jsonrpc.php
        Access.: Server (Default)

    :: Zabbix API details

        Username: Admin
        Password: zabbix

    
    - Ok, Zabbix API version: 3.0.12

