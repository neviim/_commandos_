# comandos remoto em maquinas windows

:: comandos basicos

%> icm l0105 {ls 'C:\'}
%> icm l0105 {puppet agent -t}

    # no server execute, comando abaixo para testar conectividade.
    %> ping fcn27553.joaopauloii
    %> zabbix_get -s fcn27553.joaopauloii -k agent.ping
    1 # retornando 1 esta ok
    
    %> zabbix_get -s l0105.fcn.edu.br -k agent.ping