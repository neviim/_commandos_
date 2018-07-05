# mensagens de Erros basicas no zabbix

    ::: Zabbix unreachable poller processes more than 75% busy

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

            # pingger poller
            StartPingers=20
            # proxy poller
            StartPollers=20
            # unreachable poller
            StartPollersUnreachable=10


        $ zabbix_server -R config_cache_reload
        $ systemctl restart zabbix-server.service

