# O Zabbix Get é um utilitário de linha de comando que pode ser utilizado para se comunicar 
# com o agente de monitoração do Zabbix e requisitar um dado do agente.


    :: Este utilitário é normalmente utilizado em ações de desenvolvimento ou debug de chaves no agente.


       λ> c:\zabbix\bin\win64\zabbix_get -s 127.0.0.1 -p 10050 -k system.cpu.load[all,avg1]


    :: O Zabbix Get aceita os sequintes parâmetros:  
    
        -s --host <nome ou IP>      Especifica o DNS ou IP do host a ser consultado.
        -p --port <porta>           Especifica o número da porta em execução pelo agente (normalmente a porta **10050**).
        -I --source-address <IP>    Especifica o IP de origem (caso existam múltiplos IPs na máquina que origina a requisição).
        -k --key <chave>            Especifica a chave de item que se deseja o valor.
        -h --help                   Exibe este help.
        -V --version                Exibe a versão do comando.

