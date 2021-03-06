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
        - Onde esta o IP '10.0.9.41', colocar o IP do servidor zabbix, atualmente estara sendo o '10.0.5.29'
        - Caso prefira pode 'apagar' todo conteudo deste arquivo e deixar só os atributos abaixo.
        - Com o editor escolhido abrir o arquivo: 'C:\zabbix\conf\zabbix_agentd.win.conf'

            λ nano C:\zabbix\conf\zabbix_agentd.win.conf

                Server=10.0.9.41
                ListenPort=10050
                ServerActive=10.0.9.41
                Hostname=nome_desta_maquina
                LogFile=c:\zabbix\log\zabbix_agentd.log


        # inicializando o cliente agente zabbix:

            λ cd c:\zabbix\bin\win64
            λ  .\zabbix_agentd.exe -i -c C:\zabbix\conf\zabbix_agentd.win.conf
            zabbix_agentd.exe [1332]: service [Zabbix Agent] installed successfully
            zabbix_agentd.exe [1332]: event source [Zabbix Agent] installed successfully

            # na versao 3.4
            λ cd c:\zabbix\bin\win64
            λ  .\zabbix_agentd.exe -d -c C:\zabbix\conf\zabbix_agentd.win.conf
            zabbix_agentd.exe [18344]: service [Zabbix Agent] uninstalled successfully
            zabbix_agentd.exe [18344]: event source [Zabbix Agent] uninstalled successfully

            :: o comando acima dando certo, precisa iniciar o zabbix-server no SERVIÇOS do windows.

                - Em pesquisa da cortana digite 'serviços'
                - Localize 'Zabbix Agente' na lista de soft.
                - De 2 click nele em tipo de inicialização: 'Automático' <ok> 
                - Click em 'iniciar' o serviço
                - Verifique se o 'Status' passo para 'Em Execução'
                - Cliente estara sendo executado agora.


        # liberar o Firewall no windows local

            :: este soft agente trabalha com as porta 10050, 10051

                - Para isso é necessario que o soft 'zabbix-agente' seja liberado no firewall local 
                - Entras neste item: 'Painel de Controle\Sistema e Segurança\Windows Defender Firewall\Aplicativos permitidos'
                - Clik no botão 'Permitir outro aplicativo'
                - 'Procure' no diretorio 'c:\zabbix\bin\win64\zabbix_agentd.exe' e de permição para ser executado na 'rede do dominio'
                - Fazer a mesma coisa com o agente: 'zabbix_sender.exe'  


    # Erro Unit zabbix-agent.service is masked (este erro pode ocorrer em sistema linux)
    
        $ service zabbix-agent start
        Failed to start zabbix-agent.service: Unit zabbix-agent.service is masked.
        
            $ systemctl unmask nginx.service

            # não resolvendo utiliza isso.
            $ rm /etc/systemd/system/nginx.service

        $ systemctl --all --no-pager




# referencia de configuração ao agente zabbix 

%> nano c:\zabbix\conf\zabbix_agentd.win.conf

        LogFile=C:\zabbix\log\agentd.log
        LogFileSize=10
        EnableRemoteCommands=1
        LogRemoteCommands=1
        Server='ip ou fqdn do servidor remoto'
        ServerActive='ip ou fqdn do servidor remoto'
        Hostname='nome deste servidor' #(deverá ser igual ao cadastrado no servidor Zabbix)
        Timeout=20



# Referencias:
    # systemclt
    https://sempreupdate.com.br/como-usar-o-systemctl-para-gerenciar-servicos-do-systemd/

    # varios postes sobre zabbix
    https://technologyrss.com/upgrade-zabbix-server-3-2-6-to-3-4-1/