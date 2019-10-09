# local do download dos agentes do zabbix
#
# Por.: Neviim
# data: 09/05/2018

    # link do agente zabbix

        - https://www.zabbix.com/download_agents

    :: Indicações:

            Utilizar o 'Visual Studio Code' para melhor compreender este doc.
            e utilizar o cliente de prompt 'cmder', caso não esteja instalado
            verifique onde baixa-lo e 'instala-los' em: ferramentas_tralaho_windows.py


    # baixa e instala o agente

        - Criar uma pasta C:\zabbix
        - Criar uma pasta C:\zabbix\log
        - Copia as pastas 'bin' e 'conf' do agente para dentro desta pasta 'c:\zabbix'
        - Configura o arquivo 'zabbix_agentd.win.conf'
        - Onde esta o IP '10.0.9.41', colocar o IP do servidor zabbix, atualmente
          estara sendo o '10.0.5.29'
        - Caso prefira pode 'apagar' todo conteudo deste arquivo e deixar só os atributos abaixo.
        - Com o editor escolhido abrir o arquivo: 'C:\zabbix\conf\zabbix_agentd.win.conf'

            Server=10.0.9.41
            ListenPort=10050
            ServerActive=10.0.9.41
            Hostname=nome_desta_maquina
            LogFile=c:\zabbix\log\zabbix_agentd.log


        # inicializando o cliente agente zabbix:

            λ cd C:\zabbix\bin\win64

            λ  .\zabbix_agentd.exe -i -c C:\zabbix\conf\zabbix_agentd.win.conf
            zabbix_agentd.exe [1332]: service [Zabbix Agent] installed successfully
            zabbix_agentd.exe [1332]: event source [Zabbix Agent] installed successfully

            :: o comando acima dando certo, precisa iniciar o zabbix-server no SERVIÇOS do windows.

                - Em pesquisa da cortana digite 'serviços'
                - Localize 'Zabbix Agente' na lista de soft.
                - De 2 click nele em tipo de inicialização: 'Automático' <ok>
                - Click em 'iniciar' o serviço
                - Verifique se o 'Status' passo para 'Em Execução'
                - Cliente estara sendo executado agora.



        # Executar o agente por linha de comando

            λ zabbix_agentd.exe -d -c C:\Zabbix\conf\zabbix_agentd.conf


    # Erro Unit zabbix-agent.service is masked (este erro pode ocorrer em sistema linux)

        $ service zabbix-agent start
        Failed to start zabbix-agent.service: Unit zabbix-agent.service is masked.

            $ systemctl unmask nginx.service

            # não resolvendo utiliza isso.
            $ rm /etc/systemd/system/nginx.service

        $ systemctl --all --no-pager


# Referencias:
    # systemclt
    https://sempreupdate.com.br/como-usar-o-systemctl-para-gerenciar-servicos-do-systemd/

    # varios postes sobre zabbix
    https://technologyrss.com/upgrade-zabbix-server-3-2-6-to-3-4-1/
