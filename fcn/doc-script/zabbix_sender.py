# O Zabbix Sender é um utilitário de linha de comando que pode ser utilizado para enviar dados para o Zabbix Server.

    :: Situações usuais de utilização:

        - Traps de inicio ou finalização de scripts
        - Envio de métricas de negócio diretamente a partir dos sistemas que os hospedam (sem coleta periódica)
        - Envio de traps de incidentes não monitoráveis diretamente pelo Zabbix


    :: Exemplo de utilização:

        λ 
        λ c:\zabbix\bin\win64\zabbix_sender -z zabbix -s "Linux DB3" -k db.connections -o 43

            :: Onde:

                z - IP ou nome do Zabbix Server que receberá o dado
                s - Nome técnico do host monitorado pelo Zabbix (deverá estar igual ao registrado na interface web do Zabbix, inclusive maiúsculas e minúsculas)
                k - Chave do item
                o - Valor a enviar
