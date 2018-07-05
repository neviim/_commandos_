# 

    ::: Inicio
        $ sudo systemctl start firewalld
        $ sudo systemctl enable firewalld
        $ sudo systemctl stop firewalld
        $ sudo systemctl disable firewalld

        # verifica o estados do firewall
        $ firewall-cmd --state

        # para obter uma lista das zonas disponíveis, digite.
        $ firewall-cmd --get-zones


    ::: Para obter todas as configurações para uma zona específica:

        $ firewall-cmd --zone=public --list-all
        $ firewall-cmd --list-all-zones

        $ firewall-cmd --zone=public --list-services

    :::

        $ firewall-cmd --reload










# referencias
    # Como configurar um firewall usando o FirewallD no CentOS 7
    https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-7