# mensagens de Erros basicas no zabbix

    ::: "Too many processes on Zabbix server"

        $ ps -ef | awk '{ print $8 }' | sort -n | uniq -c | sort -n | tail -5

        - É mais provável que ele tenha aumentado o número de pollers para um número crescente de hosts e itens passivos para monitorar.
          Se for o caso, ele precisa mudar de monitoração passiva para ativa.

        - O monitoramento passivo não se adapta bem.
          A segunda coisa é adicionar o proxy. Mesmo com apenas um proxy é possível minimizar as
          perdas de dados de monitoramento durante a reinicialização do servidor.

        - Estou usando apenas o KVM. Agora eu recebo cerca de 340 - 380 processos.
          Então, por agora, aumentar o limite de disparo para 400.


    ::: "Zabbix value cache working in low memory mode"

        $ nano /etc/zabbix/zabbix_server.conf

            # CacheSize=16M, alterei para 32M
            CacheSize=64M

    ::: 'Zabbix server is not running the information displayed may not be current'

        Connection to Zabbix server "localhost" refused. Possible reasons:
        1. Incorrect server IP/DNS in the "zabbix.conf.php";
        2. Security environment (for example, SELinux) is blocking the connection;
        3. Zabbix server daemon not running;
        4. Firewall is blocking TCP connection.
        Connection refused

        ::: Checar...

            $ systemctl status mysqld.service
            $ mysql -u zabbix -p


        ::: Alguns passos...

            - Nunca tive o problema até que apareceu de repente uma vez, para mim, a solução foi adicionar (descomentar) a seguinte linha em:

                $ nano /etc/zabbix/zabbix_server.conf

                    ListenIP=0.0.0.0


            # precisa retornar estas tres linhas.
            $ netstat -tulpn | grep zabbix
            tcp        0      0 0.0.0.0:10050           0.0.0.0:*               OUÇA       1060/zabbix_agentd
            tcp        0      0 0.0.0.0:10051           0.0.0.0:*               OUÇA       23079/zabbix_server
            tcp6       0      0 :::10050                :::*                    OUÇA       1060/zabbix_agentd

            # verificar se não esta barrado no proxy
            $ iptables | grep 10051

            $ cat /etc/zabbix/zabbix_server.conf
            $ cat /etc/zabbix/web/zabbix.conf.php
            $ cat /etc/hosts

            # 10050 or 10051
            $ nmap -sS localhost
            $ nmap -sT -p1-10051 localhost


    ::: 'Zabbix unreachable poller processes more than 75% busy'

        - Zabbix unreachable poller processes more than 75% busy


        # Exesso de itens processado por server sem escalar.
        - Mais de 100 itens com dados ausentes por mais de 10 minutos
        - Nós temos uma única implantação de servidor Zabbix. Em nosso servidor Zabbix, o alarme 'Zabbix unreachable poller processa mais de 75% ocupado'
          foi acionado e apagado com freqüência. Esse problema ocorreu depois que alteramos o limite para 90%. A média dos últimos 3 dias é de 82%.

        # uma outra caracteristica relacionada ao numero de processos ao qual op servidor é capas de processar.
        - Isso praticamente responde à sua situação. Você vê, uma vez que cada verificação é realizada pelo próprio Zabbix Server, não é de admirar que esteja lutando para coletar esses 83171 valores de itens.
          A melhor prática é fazer com que todas as verificações possíveis sejam ativas, bem como descarregar o servidor, implementando o proxy no modo ativo, para que o Zabbix Server fique ocupado apenas com
          o processamento dos dados, sem desperdiçar recursos para coletar.
          Por outro lado, você tem uma máquina bastante potente para sua média de 700 NVPS, então você definitivamente pode tentar maximizar a configuração de StartPollers, se isso ajudar a estabilizar a situação
          atual e dar tempo de descarregar o servidor passo a passo ( movendo para cheques ativos). Mesmo que 1000 pollers sejam suficientes para aniquilar a fila e nivelar o desempenho, você ainda não terá
          escalabilidade e acabará sem recursos para adicionar ao seu monitoramento com a configuração atual.

            # algumas medidas de prevenção que podera ser tomadas
            Então, algo que podera ajudar:

                1) Pense em adicionar um proxy para descarregar o servidor Zabbix em longo prazo.
                2) Defina StartPollers = 1000 e veja se seu servidor está OK com essa carga. Ajustar ao seu valor máximo possível para comprar-se algum tempo.
                3) Configure os agentes do Zabbix para o modo ativo, reconfigure os itens para serem verificações ativas.
                4) Configure os StartPollers para o que for mais adequado, quando você concluir a movimentação para as verificações ativas do agente Zabbix.


        # Ajustar a configuração do zabbix server
        $ nano /etc/zabbix/zabbix_server.conf

            # altera este parametro que tem por padrão 1 e atua em um range de 1 a 1000
            # com isso, o Zabbix irá criar 20 processos para o poller e 10 processos para unreachable poller.

            StartDiscoverers=10
            # pingger poller
            StartPingers=20
            # proxy poller
            StartPollers=20
            # unreachable poller
            StartPollersUnreachable=10


        $ zabbix_server -R config_cache_reload
        $ systemctl restart zabbix-server.service
