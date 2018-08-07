# telegram bot
# sets fora, nada.

    zbFcnBot
    zabbix_fcn_bot
    ID: 1013083020183 nv
    ID: 4201859540916 ws

    Use this token to access the HTTP API:
    6193621820189:AA7EwsM_UeNfsL7Wfje9aIqn1h4xXaZSWAK7NM
                  

    ::: Instalando

        $ yum install python-pip
        $ pip install pyTelegramBotAPI 

        $ cd /usr/lib/zabbix/alertscripts
        $ nano telegram.sh

            #!/usr/bin/env python

            import telebot,sys

            BOT_TOKEN='6193621820189:AA7EwsM_UeNfsL7Wfje9aIqn1h4xXaZSWAK7NM'
            DESTINATION=sys.argv[1]
            SUBJECT=sys.argv[2]
            MESSAGE=sys.argv[3]

            MESSAGE = MESSAGE.replace('/n','\n')

            tb = telebot.TeleBot(BOT_TOKEN)
            tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE)

        $ chown zabbix:zabbix telegram.sh
        $ chmod +x telegram.sh


    ::: entrando no telegram web

        https://api.telegram.org/bot(Trocar_Por_CHAVE_DO_TELEGRAM)/getUpdates
        https://api.telegram.org/bot6193621820189:AA7EwsM_UeNfsL7Wfje9aIqn1h4xXaZSWAK7NM/getUpdates

       { "ok":true,"result":[{"update_id":836787886,
         "message":{"message_id":1,"from":{"id":1013083020183,"is_bot":false,"first_name":"Neviim","last_name":"Jads","username":"Neviim","language_code":"pt-BR"},"chat":{"id":1013083020183,"first_name":"Neviim","last_name":"Jads","username":"Neviim","type":"private"},"date":1530207779,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}},{"update_id":836787887,
         "message":{"message_id":2,"from":{"id":1013083020183,"is_bot":false,"first_name":"Neviim","last_name":"Jads","username":"Neviim","language_code":"pt-BR"},"chat":{"id":1013083020183,"first_name":"Neviim","last_name":"Jads","username":"Neviim","type":"private"},"date":1530207799,"text":"Neviim testando bot FCN"}},{"update_id":836787888,
         "message":{"message_id":3,"from":{"id":1013083020183,"is_bot":false,"first_name":"Neviim","last_name":"Jads","username":"Neviim","language_code":"pt-BR"},"chat":{"id":1013083020183,"first_name":"Neviim","last_name":"Jads","username":"Neviim","type":"private"},"date":1530207804,"text":"Teste"}}]
       }


    ::: testando o script

        $ cd /usr/lib/zabbix/alertscripts
        $ ./telegram.sh 1013083020183 Neviim Jads


# ERROS

    ::: "Cannot exectue command "/usr/share/zabbix/alertscripts/telegram.sh": [2] No such file or directory"

