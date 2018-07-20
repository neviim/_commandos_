# 
    ::: instalando snmpwalk

        $ yum install net-snmp-utils
        $ snmpwalk --help
        Version:  5.7.2
        Web:      http://www.net-snmp.org/

    :::

        $ snmpwalk -v 2c -c public localhost
        $ snmpwalk -v 2c -c public localhost iso.3.6.1.2.1.1.6.0
        $ snmpwalk -v 2c -c public -M /root/ismail/ciscoMIB localhost iso.3.6.1.2.1.1.6.0


    ::: OKI Printer: SNMP OID

        # OKI MC780 
        $ snmpwalk -v 2c -c public 10.0.45.78                                   # lista completa de todos os itens
        $ snmpwalk -v 2c -c public 10.0.45.78 sysName.0                         # sysName       - SNMPv2-MIB::sysName.0 = STRING: OKI-MC780-ACF96E
        $ snmpwalk -v 2c -c public 10.0.45.78 sysUpTime.0                       # sysUpTime     - DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (86787800) 10 days, 1:04:38.00

        $ snmpwalk -v 1  -c public 10.0.45.78 .1.3.6.1.2.1.43.11.1.1
        $ snmpwalk -v 2c -c public 10.0.45.78 .1.3.6.1.2.1.43.11.1.1.9.1.4      # Yellow  Toner - SNMPv2-SMI::mib-2.43.11.1.1.9.1.4 = INTEGER: 80 - Ok
        $ snmpwalk -v 2c -c public 10.0.45.78 .1.3.6.1.2.1.43.11.1.1.9.1.3      # Magenta Toner - SNMPv2-SMI::mib-2.43.11.1.1.9.1.3 = INTEGER: 80 - Ok
        $ snmpwalk -v 2c -c public 10.0.45.78 .1.3.6.1.2.1.43.11.1.1.9.1.2      # Cyan    Toner - SNMPv2-SMI::mib-2.43.11.1.1.9.1.2 = INTEGER: 40 - Ok
        $ snmpwalk -v 2c -c public 10.0.45.78 .1.3.6.1.2.1.43.11.1.1.9.1.1      # Black   Toner - SNMPv2-SMI::mib-2.43.11.1.1.9.1.1 = INTEGER: 90 - Ok

        # O valores do toner/pagina impressas
        $ snmpget -v 2c -c public 10.0.45.78 .1.3.6.1.2.1.43.11.1.1.8.1.1       # Valor maximo toner        - SNMPv2-SMI::mib-2.43.11.1.1.8.1.1 = INTEGER: 100
        $ snmpget -v 2c -c public 10.0.45.78 .1.3.6.1.2.1.43.11.1.1.9.1.1       # Valor disponivel toner    - SNMPv2-SMI::mib-2.43.11.1.1.9.1.1 = INTEGER: 90
        $ snmpget -v 2c -c public 10.0.45.78 .1.3.6.1.2.1.43.10.2.1.4.1.1       # Contador pagina impressa  - SNMPv2-SMI::mib-2.43.10.2.1.4.1.1 = Counter32: 251510


        $ snmpwalk -v 2c -c public 10.0.45.78 mib-2.43.8.2.1.9.1.1              # SNMPv2-SMI::mib-2.43.8.2.1.9.1.1 = INTEGER: 530

        # Interface rede
        $ snmpwalk -v 2c -c public 10.0.45.78 1.3.6.1.2.1.2.2.1.2
        IF-MIB::ifDescr.1 = STRING: lo
        IF-MIB::ifDescr.2 = STRING: eth0

        # OKI
        $ snmpwalk -v 2c -c public 10.0.45.24




::: Configurando Host e Item no Zabbix:

    - Agora vem a parte interessante. Vamos criar um novo Host no Zabbix para monitorarmos os itens.

        1. Acesse o menu ‘Configurações > Hosts';
        2. Clique no botão ‘Criar Host';
        3. Preencha nome, novo grupo (opcional) e o IP na interface SNMP. Não precisamos preencher nada nos campos do Agente Zabbix.
        4. Clique no botão ‘Adicionar';
        5. Voltando a tela de hosts, ao lado do host recém criado, clique em ‘Itens';
        6. No canto superior direito, clique em ‘Criar Item';
        7. Preencha os campos conforme a figura (alterando o necessário para seu ambiente):

    - Duas peculiaridades na tela acima:

        (1) O nome da chave, pode ser o que você achar interessante, mas é obrigatório. Essa chave é usada nos Triggers que vamos criar. 
        (2) No intervalo de atualização, coloquei 86400 (1 dia), pois não há necessidade de ficar lendo valor do contador o tempo todo. 
            No meu caso, essa informação é relevante apenas no dia do fechamento da locação. Configure conforme sua necessidade.

    - Criando um Item para monitorar o Toner:
    
        Vamos repetir os passos 6 e 7, porém, com algumas modificações (Nome, OID, chave, intervalo de atualização e aplicação):
        Após adicionar os itens, podemos verificar se o Zabbix já está lendo os valores no menu ‘Monitoramento > Dados Recentes':



::: Criando um Trigger para o nível do Toner:

    - No caso dessa impressora com dados ficticios, o valor retornado pelo objeto que monitora o toner, é a quantidade de cópias que ainda podem ser impressas 
      (648 na figura acima). O valor máximo do toner, no exemplo desse artigo, é 940 (como podemos ver no início). Vou criar um Trigger, que alerte quando a 
      capacidade do toner estiver abaixo de 10%. Logo, quando o nível do toner estiver abaixo de 94 (10% de 940), quero que o Trigger dispare. Mãos a obra!

        1. Acesse o menu ‘Configurações > Hosts';
        2. Ao lado do host monitorado (Impressora OKI) clique em ‘Triggers';
        3. No canto superior direito, clique em ‘Criar Trigger';
        4. Escolha um nome para seu Trigger. Eu coloquei ‘Toner está abaixo de 10%';
        5. Ao lado de ‘Expressão’, clique em ‘Adicionar';
        6. Ao lado de ‘Item’, clique em ‘Selecionar';
        7. Selecione o item que criamos, que monitora o toner e preencha o restante da seguinte forma:
        'Queremos que o Trigger dispare quando o último valor recebido (T) é menor que 94 (N).'
        8. Clique em ‘Inserir';
        9. Selecione uma severidade para seu Trigger. Eu selecionei ‘Atenção':
        10. Clique em ‘Adicionar’.

    - Está feito. Agora você recebe um alerta no sistema, quando o nível do toner ficar abaixo de 10% da capacidade de impressão. Adicionalmente, consegue 
      ter o controle do total de impressões. Esse tutorial deve funcionar para outros modelos de impressora, contanto que tenha suporte à SNMP.




# referencia
    https://library.netapp.com/ecmdocs/ECMP1368834/html/GUID-113EA449-1EBA-46F2-B954-76A9F36C3FD8.html



# PRTG Tray
    Nome:
    prtgtrial

    Licence Key:
    000014-2ZPKFM-8FFPUZ-7C66HR-EQH2M3-VWYW6J-QU3X3W-7D8MNN-3U1UR8-CGYFXN

