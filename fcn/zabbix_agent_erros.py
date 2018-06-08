
# Erro: Get value from agent failed: cannot connect to [[10.0.45.4]:10050]: [111] Connection refused

    - Olá, os usuários do Zabbix por muitos anos desde a nova instalação, temos um problema com hosts externos, 
    temos a mensagem Falha em obter valor do agente: não é possível conectar-se a [[ip]: 10050]: [4] 
    Interrompida a chamada do sistema para hosts dentro da rede funciona bem para clientes externos impossíveis 
    de se conectar ao servidor Zabbix.

        - Resposta ao problema:

            - Estas são verificações de agentes passivos que estão falhando do zabbix server para o zabbix agent.

                # No server zabbix utilizar comando para testar o timeout entre server e agent.

                    $ zabbix_get -s 10.0.5.31 -k agent.ping
                    1


            - Uma possivel solução:

                # Obrigado pela sua contribuição. Na verdade, meu problema foi resolvido há muito tempo, depois que mudei a 
                configuração de criptografia do agente na página de configuração do host de:
                
                    [PSK]  [NONE] [PSK] [CERT] para 
                    [NONE] [NONE] [PSK] [CERT]. 
                         
                Como eu estava monitorando hosts em diferentes locais usando o agente ativo, não percebi que não deveria ativar 
                a criptografia dupla.


# Erro: Get value from agent failed: ZBX_TCP_READ() failed: [104] Connection reset by peer

    ::: nmap mostra que as portas estão abertas no lado do servidor:

        10050/tcp open
        10051/tcp open

        ::: Tente este comando no servidor e veja se ele te dá algo diferente "zabbix_get -s clienthostname -k system.uname"
            
            $ zabbix_get -s fac034378n1.fcn.edu.br -k system.uname

            $ ping fac034378n1.fcn.edu.br
            $ telnet fac034378n1.fcn.edu.br 10050