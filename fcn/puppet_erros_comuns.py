# Erros ao instalar o puppet

    :: Warning: Failed to open TCP connection to puppet:8140 (Device or resource busy - getaddrinfo)

        - Verifique se a configuração /etc/hosts consta em 127.0.1.1 puppet

            $ car /etc/hosts

                127.0.0.1 zabbix.fcn.edu.br zabbix localhost.localdomain localhost
                127.0.1.1 puppet

                10.0.0.16 srv-ad1-fcn adserver

                # The following lines are desirable for IPv6 capable hosts
                ::1 localhost ip6-localhost ip6-loopback
                ::1 localhost6.localdomain6 localhost6
                fe00::0 ip6-localnet
                ff02::1 ip6-allnodes
                ff02::2 ip6-allrouters
                ff02::3 ip6-allhosts

            - isso resolvera este erro.

    