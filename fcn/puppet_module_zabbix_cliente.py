# criar um novo modulo
# https://www.youtube.com/watch?v=1WZgmpoU7Oc&t=26s
#

    :: lablist, para manter definido o que pode estar instaldo ou não.
    
        # referencia
        $ cd /etc/puppet/code/environments/production/manifests/site.pp 
        $ cd /etc/puppet/code/environments/production/modules

        $ cd /etc/puppet/code/environments/production/modules/zabbix/manifests

        $ puppet module generate jads-zabbix --skip-interview
        # chave do repositorio zabbis
        $ wget http://repo.zabbix.com/zabbix-official-repo.key


        # editando manifestos
        $ nano /etc/puppet/code/environments/production/manifests/site.pp 
        $ nano /etc/puppet/code/environments/production/modules/zabbix/manifests/agent.pp


    :: comandos powersheel

        $ Get-command
        $ Add-command 

    :: comandos Chocolatey:

        # c:\ProgramData\chocolatey
        # c:\ProgramData\zabbix\zabbix_agentd.conf
        $ choco install zabbix-agent --version 3.0.4

    :: comandos linux:

        $ egrep ^[^#] zabbix_agentd.conf.erb > zabbix_agentd.conf.erb.tmp
        $ mv zabbix_agentd.conf.erb.tmp zabbix_agentd.conf.erb

        $ zabbix_get -s 10.0.9.41 -k system.uname


    :: comandos puppet:

        $ puppet module install genebean-zabbixagent --version 3.0.4


    # preparando ambiente para instalar zabbixagent por puppet no windows.

        :: puppet agent zabbix para windows:

            $ puppet module install --modulepath modules/ chocolatey/chocolatey
            $ puppet module install ceritsc-chocolatey_sw --version 0.9.3

        :: acertando o zabbix/templates:

            $ nano zabbix_agentd.conf.erb

                LogFileSize=0
                Server=<%= @zabbix_server %>
                ServerActive=<%= @zabbix_server %>
                Homename=<%= @fqdn %>


'''
c:> puppet agent -t
Info: Using configured environment 'production'
Info: Retrieving pluginfacts
Info: Retrieving plugin
Info: Retrieving locales
Info: Loading facts
Info: Caching catalog for pdlab01.fcn.edu.br
Error: Failed to apply catalog: Parameter provider failed on Package[zabbix-agent]: Invalid package provider 'chocolatey' (file: /etc/puppet/code/environments/production/modules/zabbix/manifests/agent.pp, line: 21)

'''


''' Teste de instalação de um modulo zabbix-agent do puppet

$ puppet module install genebean-zabbixagent --version 3.0

Notice: Preparing to install into /etc/puppet/code/environments/production/modules ...
Notice: Downloading from https://forgeapi.puppet.com ...
Notice: Installing -- do not interrupt ...
/etc/puppet/code/environments/production/modules
└─┬ genebean-zabbixagent (v3.0.0)
  └─┬ puppetlabs-chocolatey (v2.0.2)
    ├── puppetlabs-powershell (v2.1.5)
    ├── puppetlabs-registry (v2.0.1)
    └── puppetlabs-stdlib (v4.25.1)

'''

# Referencia
    # agente chocolatey_sw para windows
    https://forge.puppet.com/ceritsc/chocolatey_sw