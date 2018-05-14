# logar linux no Active Directory

    :: esta configuração funcionou corretamente:

        - ubuntu 18.04 
        - mint 17

    :: ferramentas utilizadas

        $ apt install dnsutils


# maquina server AD

    hostname    'server'
    dns1        'central.local'
    ip          '192.168.0.203'
    gateway     '192.168.0.1'
    dns server  '192.168.0.203'

    # Maquina cliente linux

        :: teste acesso ao servidor AD

            $ ping 192.168.0.203
            ok
            $ ping server.central.local
            ping: unknown host server.central.local


        :: configura host

            $ nano /etc/hosts

                192.168.0.203  server.central.local  server


        :: configura nsswitch.conf

            $ nano /etc/nsswitch.conf

                #hosts:         files mdns4_minimal [NOTFOUND=return] dns
                hosts:          files dns mdns4


        :: configura resolv

            $ nano /etc/resolv.conf 

                search central.local
                nameserver 192.168.0.203


        :: conficurando dhclient '/etc/dhcp/' ou '/etc/dhcp3/'

            $ nano /etc/dhcp/dhclient.conf

                option rfc3442-classless-static-routes code 121 = array of unsigned integer 8;

                supersede domain-name "central.local"
                prepend domain-name-servers 192.168.0.203


        :: configurar visudo

        $ sudo visudo

            # User privilege specification
            root    ALL=(ALL:ALL) ALL
            CENTRAL\\Administrador ALL=(ALL) ALL

            # Members of the admin group may gain root privileges
            %admin ALL=(ALL) ALL
            %central\\central^users ALL=(ALL) ALL

            # membros do grupo SUDO
            %sudo   ALL=(ALL:ALL) ALL
            fcn\\jorge ALL=(ALL) ALL

    :: Instalar dependencias: 

        $ apt install likewise-open

            # caso sistema for atual utilizar

                :: baixa a ultima versão deste sete: https://github.com/BeyondTrust/pbis-open/releases

                    $ wget https://github.com/BeyondTrust/pbis-open/releases/download/8.6.0/pbis-open-8.6.0.427.linux.x86_64.deb.sh
                    $ chmod +x pbis-open-8.6.0.427.linux.x86_64.deb.sh
                    $ ./pbis-open-8.6.0.427.linux.x86_64.deb.sh

                    ou, se tiver este repositorio na sua lista.
                    
                    $ apt install pbis-open pbis-open-gui

            
# executando e conficurando o acesso ao Active Directory

    # modo grafico
    $ /opt/pbis/bin//domainjoin-gui

    # modo terminal exemplo de uso: [ $ /opt/likewise/bin/domainjoin-cli join vmware.local Administrator Password ]
    $ /opt/pbis/bin/domainjoin-cli join fcn.edu.br Administrador
    
        central.local

        Administrador
        #R.........O#

        :: Conectado com sucesso.

        # mostrara em qual servidor de dominio se conecto
        $ domainjoin-cli query
        Name = username
        Domain = example.com
        Distinguished Name = CN=username,CN=Computers,DC=example,DC=com




    # Testar conectividade do usuario

        :: Estando conectado podera testar: 

            $ su - central\\neviim
            Password:

            $ pwd 
            /home/local/LOCAL/neviim 

            $ whoami
            neviim




# Possiveis ERROS:

    :: Error: DNS_ERROR_BAD_PACKET [code 0x0000251e]

        Eu resolvi esse problema adicionando 'dns-nameserver' como o controlador de domínio 
        em '/etc/network/interfaces' antes de tentar 'domainjoin-cli'. 

            $ nano /etc/resolv.conf       

                domain srv-ad1-mqn
                search srv-ad1-mqn
                nameserver 10.0.0.16


    :: Error: LW_ERROR_ACCESS_DENIED [code 0x00009cde]

        Você precisará sudo domainjoin-cli se não for root.


