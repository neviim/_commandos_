# configurando active directory em um centos 7

    ::: 
    
        $ yum install sssd realmd oddjob oddjob-mkhomedir adcli samba-common samba-common-tools krb5-workstation openldap-clients policycoreutils-python
        ok

        $ nano /etc/hosts
            10.0...   serverfcn adserver fcn.edu.br

        $ nano /etc/resolv.conf 
            search fcn.edu.br
            nameserver 10.0.0...

        $ realm join --user=manoel adserver
        Senha para manoel:


        # comandos para verificar as configurações 
        $ realm list
        fcn.edu.br
        type: kerberos
        realm-name: FCN.EDU.BR
        domain-name: fcn.edu.br
        configured: kerberos-member
        server-software: active-directory
        client-software: sssd
        required-package: oddjob
        required-package: oddjob-mkhomedir
        required-package: sssd
        required-package: adcli
        required-package: samba-common-tools
        login-formats: %U@fcn.edu.br
        login-policy: allow-realm-logins

        $ cat /etc/sssd/sssd.conf
        $ id neviim@fcn.edu.br 
        uid=12776802829(usuario@fcn.edu.br) gid=12776800512(admins. do domínio@fcn.edu.br) grupos=12776800512(admins. do domínio@fcn.edu.br),
        12776800572(grupo de replicação de senha rodc nega@fcn.edu.br),12776801118(gerenciar contas@fcn.edu.br),12776800513(usuários do domínio@fcn.edu.br)




# Erro

    ::: id: usuario: no such user

        $ id ususario
        id: usuario: no such user

        $ nano /etc/sssd/sssd.conf

            # use_fully_qualified_names = True
            # fallback_homedir = /home/%u@%d
            use_fully_qualified_names = False
            fallback_homedir = /home/%u

        $ systemctl restart sssd
        $ systemctl daemon-reload

        $ id usuario
        uid=12776802829(usuario) gid=12776800512(admins. do domínio) grupos=12776800512(admins. do domínio),12776800513(usuários do domínio),
        12776801118(gerenciar contas),12776800572(grupo de replicação de senha rodc nega)

        $ cat /etc/sudoers.d/sudoers
            %sudoers    ALL=(ALL)       ALL