# instalar puppte agent em uma maquina linux zerada.

    :: Instalar dependencias diretas:

        # $ apt install facter
        # $ apt install ruby-full

        $ apt install puppet
        
        $ facter -v
        3.10.0
        $ puppet --version
        5.4.0
        $ ruby -v
        ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-linux-gnu]


    :: 




# ERROS:

    ::: Error: Could not request certificate: Failed to open TCP connection to puppet:8140 (Device or resource busy - getaddrinfo)
        Exiting; failed to retrieve certificate and waitforcert is disabled

        - 'para corrigir precisa especificar o endereço dns do puppetmaster, de forma que o cliente o localize.'

        $ puppet resource user root
        $ puppet resource package puppet-agent
        $ puppet resource service puppet
        $ facter os


        # verifica path do puppet
        $ which puppet agent
        /usr/bin/puppet


        # verifica configuração de /etc/hosts
        $ nano /etc/hosts

            127.0.0.1       localhost.localdomain   localhost
            127.0.1.1       zabbixsrv.fcn.edu.br    zabbixsrv               zabbix

            # The following lines are desirable for IPv6 capable hosts
            ::1     localhost ip6-localhost ip6-loopback
            ::1     localhost6.localdomain6 localhost6
            fe00::0 ip6-localnet
            ff02::1 ip6-allnodes
            ff02::2 ip6-allrouters
            ff02::3 ip6-allhosts

            # dominio
            10.0.0.16 srv-ad1-fcn adserver fcn.edu.br
            10.0.9.41 puppetmaster.fcn.edu.br puppet


        # configuração puppet.conf
        $ nano /etc/puppet/puppet.conf

            [main]
            ssldir = /var/lib/puppet/ssl
            server=puppetmaster.fcn.edu.br
            autoflush=true

            [master]
            vardir = /var/lib/puppet
            cadir  = /var/lib/puppet/ssl/ca
            dns_alt_names = puppet,puppetmaster,puppetmaster.fcn.edu.br

        $ systemctl restart puppet-master.service


        # status do resviço que esta rodando, puppet-master.service
        $ systemctl status puppet-master.service

            ● puppet-master.service - Puppet master
            Loaded: loaded (/lib/systemd/system/puppet-master.service; enabled; vendor preset: enabled)
            Active: active (running) since Tue 2018-06-12 16:11:38 -03; 17h ago
                Docs: man:puppet-master(8)
            Main PID: 1900 (puppet)
                Tasks: 4 (limit: 4915)
            CGroup: /system.slice/puppet-master.service
                    └─1900 /usr/bin/ruby /usr/bin/puppet master