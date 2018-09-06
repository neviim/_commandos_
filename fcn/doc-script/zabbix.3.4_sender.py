# envio de dados para uma variavel no zabbix server

    ::: terremoto

        - No zabbix server cria um host trigger do tipo "zabbix trapper" com o nome da variavel a receber o valorself.
        - Este valor sera enviado pelo zabbix_sender

    ::: zabbix_sender

        $ zabbix_sender.exe -z zabbixsrv.joaopauloii -s "Trigger" -k trap.terremoto -o 30
        info from server: "processed: 0; failed: 1; total: 1; seconds spent: 0.001334"
        sent: 1; skipped: 0; total: 1
