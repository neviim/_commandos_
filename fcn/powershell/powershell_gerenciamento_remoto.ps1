# Serviço remoto
# https://www.youtube.com/watch?v=qMDt_NY9Qw0

    *** preparando ambiente para gerenciamento Remoto a outro computador:

        %> winrm quickconfig

        *** Usando o powerShell

            - No windows a politica de execusao de comandos pode estar desabilitada

                # deleta um serviço do windows 
                %> sc delete nome_servico

                # verifica o status 
                %> Get-ExecutionPolicy -List
                %> Get-ExecutionPolicy -Scope CurrentUser

                # mudar a politica de execução
                %> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
                %> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned

                # retorna a politica de execução
                Set-ExecutionPolicy Undefined -scope LocalMachine
                Set-ExecutionPolicy Undefined



            # lista os processos de uma maquina remota
            %> icm fac034378n1 {get-process}
            %> Get-Content c:\temp\Serves.txt

            %> icm fac034378n1 {cat c:\zabbix_agentd.log}
            %> icm fac034378n1 {ls 'C:\Program Files\'}

            # obter uma lista de aplicativos instalados em uma máquina, muito lemto
            %> Get-WmiObject -Class Win32_Product | Select Name, Version

