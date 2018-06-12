# colocando uma maquina linux no dominio AD - Microsoft

    ::: dependencias

        # verificar se esta instalado.
        $ apt install dnsutils


        ::: colocar o dns do server no hosts

            $ nano /etc/hosts
            
                10.0.0.16       srv-ad1-fcn     adserver


        ::: configura nsswitch.conf

            $ nano /etc/nsswitch.conf

                # hosts:        files mdns4_minimal [NOTFOUND=return] dns
                # hosts:        files dns
                hosts:          files dns mdns4

        
        ::: configura resolv

            $ nano /etc/resolv.conf 

                nameserver 10.0.0.16
                search fcn.edu.br


        ::: conficurando dhclient '/etc/dhcp/' ou '/etc/dhcp3/'

            $ nano /etc/dhcp/dhclient.conf

                option rfc3442-classless-static-routes code 121 = array of unsigned integer 8;

                supersede domain-name "fcn.edu.br";
                prepend domain-name-servers 10.0.0.16;

                send host-name = gethostname();


        ::: configurar visudo

            $ sudo visudo

                # User privilege specification
                root    ALL=(ALL:ALL) ALL
                fcn\\Administrador ALL=(ALL:ALL) ALL

                # Members of the admin group may gain root privileges
                %admin ALL=(ALL) ALL
                %fcn\\central^users ALL=(ALL) ALL

                # membros do grupo SUDO
                %sudo   ALL=(ALL:ALL) ALL
                fcn\\neviim ALL=(ALL:ALL) ALL


        ::: install powerBroker "pbis-open" para linux

            $ wget https://github.com/BeyondTrust/pbis-open/releases/download/8.6.0/pbis-open-8.6.0.427.linux.x86_64.deb.sh
            $ chmod +x pbis-open-8.6.0.427.linux.x86_64.deb.sh
            $ ./pbis-open-8.6.0.427.linux.x86_64.deb.sh



# conficurando o acesso ao Active Directory

    ::: modo terminal exemplo de uso: [ /opt/likewise/bin/domainjoin-cli join vmware.local Administrator Password ] 
    
        $ /opt/pbis/bin/domainjoin-cli join fcn.edu.br Administrador

            Joining to AD Domain:   fcn.edu.br
            With Computer DNS Name: zabbix.fcn.edu.br

            Administrador@FCN.EDU.BR's password: #Senha_Acesso#

            Warning: System restart required
            Your system has been configured to authenticate to Active Directory for the first time.  It is recommended that you restart your system to ensure that all applications recognize the
            new settings.

            SUCCESS


        $ domainjoin-cli query