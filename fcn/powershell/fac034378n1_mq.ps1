# comandos remoto em maquinas windows

    :: comandos basicos

        %> icm fac034378n1 {ls 'C:\Program Files\'}
        %> icm fac034378n1 {ls 'C:\Program Files\Puppet Labs\'}

        %> icm fac034378n1 {winrm get winrm/config/client/auth}

    
    :: chocolate

        # powershell.exe "-NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        # Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

        %> icm fac034378n1 {ls 'C:\ProgramData\'}
        %> icm fac034378n1 {ls 'C:\ProgramData\chocolatey\'}


    :: PuppetLabs

        %> icm fac034378n1 {ls 'C:\ProgramData\PuppetLabs\code\environments\production\'}
        %> icm fac034378n1 {ls 'C:\Program Files\Puppet Labs\Puppet\'}





# referencias
    https://puppet.com/docs/pe/2018.1/managing_windows_nodes/installing_and_using_windows_modules.html