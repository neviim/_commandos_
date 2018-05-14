# Baixar e instalar pbis-open

    https://github.com/BeyondTrust/pbis-open
    https://github.com/BeyondTrust/pbis-open/releases

    :: linux mint 18

        $ apt install likewise-open

        :: Ainstalacao sera instalada em

            $ ls /opt/pbis/bin

            $ /opt/pbis/bin//domainjoin-gui


    :: Estando conectado podera testar: 

        $ su - local.com\\test.user
        Password:

        $ pwd 
        /home/local/LOCAL/test.user 

        $ whoami
        test.user 











# Referencias:
    # domainjoin-gui
    http://www.linuxcertif.com/man/8/domainjoin-gui/

    # Samba Active Directory : the tool to manage your users
    https://www.youtube.com/watch?v=O2dymYKCYjI

    # authenticate windows AD users from linux machine
    https://www.youtube.com/watch?v=yZHw3ZYxKIA&t=91s

    # join Linux in Active Directory(SSO:Single Sign On), used PBIS
    https://www.youtube.com/watch?v=oZg8P3cXBGA

    # join Ubuntu Linux in Microsoft Active Directory Domain (Fazer este)
    https://www.youtube.com/watch?v=Y3TFPDT9uic


    # testando algumas propostas de configuracoes

        :: configurando DNS placa rede:

            # time 3:33
            https://youtu.be/oNCzh3dkdBM?t=213
            https://youtu.be/oNCzh3dkdBM?t=267

        :: pam.d 

            # time: 9:29
            https://youtu.be/oNCzh3dkdBM?t=569
            https://www.youtube.com/watch?v=oNCzh3dkdBM


        # testando

            $ apt install samba

            :: configura o arquivo vim /etc/resolv.conf, apontando para o servidor de dominio

                $ sudo vim /etc/resolv.conf

                    domain server
                    search central.local
                    nameserver 192.168.0.203

            :: faz o teste com nslookup

                $ nslookup central.local
                Server:		192.168.0.203
                Address:	192.168.0.203#53
        
                Name:	central.local
                Address: 192.168.0.203

            :: este endereco ghost '0.99' eu o reservei no 'AD - DNS' para que seje encontrado no teste

                $ nslookup ghost      
                Server:		192.168.0.203
                Address:	192.168.0.203#53

                Name:	ghost.central.local
                Address: 192.168.0.99


            :: reverso

                $ ntpdate 192.168.0.203
                12 May 13:45:29 ntpdate[31864]: the NTP socket is in use, exiting


                $ vim /etc/ntp.conf
                    #pool 0.ubuntu.pool.ntp.org iburst
                    #pool 1.ubuntu.pool.ntp.org iburst
                    #pool 2.ubuntu.pool.ntp.org iburst
                    #pool 3.ubuntu.pool.ntp.org iburst
                    poll 192.168.0.203

                $ /etc/init.d/ntp restart

                # 



        
        