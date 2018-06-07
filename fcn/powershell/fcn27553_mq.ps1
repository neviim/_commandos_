# fcn27553.joaopauloii

    ::: preparando ambiente para gerenciamento Remoto a outro computador:

        %> winrm quickconfig
        %> net start winrm
        %> winrm get winrm/config/client/auth

        %> icm fac034378n1 {winrm get winrm/config/client/auth}

        
        ::: o Invoke-Command do PowerShell pode ser usado para a execução de comandos no serviço WinRM.
        
            % > Invoke-Command -ComputerName fac034378n1 -ScriptBlock { dir c:\ }

        ::: comando basico:

            %> icm fcn27553 {ls 'C:\Program Files\'}
            %> icm fcn27553 {zabbix_agentd.exe --version}
            %> icm fcn27553 {choco}
