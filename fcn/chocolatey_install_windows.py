# O Chocolatey é um gerenciador de pacotes para o Windows (como o apt-get ou o yum, mas para o Windows).

    :: Os pacotes chocolatey podem ser usados ​​independentemente, mas também se integram com gerenciadores 
       de configuração como SCCM, Puppet e Chef. A Chocolatey é confiável por empresas de todo o mundo 
       para gerenciar suas implantações de software no Windows. 

    :: Com tudo isso em mente, pense em Chocolatey como uma estrutura sobre a qual você pode construir. 
       Chef, Puppet, Boxstarter, PowerShell DSC, Ansible, Saltstack, etc, todos têm maneiras de usar 
       Chocolatey para garantir o estado de um computador e pacotes instalados. Até mesmo a Microsoft 
       decidiu usar o framework do Chocolatey com o agregador de gerenciadores de pacotes do PowerShell.


        $ Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
        $ choco upgrade chocolatey

