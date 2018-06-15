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

    
    ::: Warning: Unable to fetch my node definition, but the agent run will continue:
        Warning: SSL_connect returned=1 errno=0 state=error: certificate verify failed (certificate rejected): [ok for /CN=puppetmaster.fcn.edu.br]


        $ puppet agent --configprint ssldir
        /var/lib/puppet/ssl

        $ mv /var/lib/puppet/ssl /var/lib/puppet/ssl.old


        $ puppet agent -t --trace --debug



    ::: Error: Could not request certificate: Find /puppet-ca/v1/certificate/ca?environment=production&fail_on_404=true resulted in 404 with the message: 
        {"message":"Not Found: Could not find certificate ca","issue_kind":"RESOURCE_NOT_FOUND"}


        - na maquina puppetmaster

            $ puppet config print certname
            puppetmaster.fcn.edu.br


            $ puppet agent -t
            Info: Caching certificate for ca
            Info: csr_attributes file loading from /etc/puppet/csr_attributes.yaml
            Info: Creating a new SSL certificate request for puppetmaster.fcn.edu.br
            Info: Certificate Request fingerprint (SHA256): 44:F4:B6:F4:F7:E2:DE:C0:E9:24:1D:91:D8:4E:D1:8A:81:C4:7B:16:D7:FF:F1:ED:B7:E4:A4:E5:B9:0F:AE:58
            Info: Caching certificate for ca
            Exiting; no certificate found and waitforcert is disabled


            # removendo um certificado no server
            $ puppet cert revoke zabbixsrv.fcn.edu.br
            $ puppet cert clean zabbixsrv.fcn.edu.br
            Notice: Revoked certificate with serial 3
            Notice: Removing file Puppet::SSL::Certificate zabbixsrv.fcn.edu.br at '/var/lib/puppet/ssl/ca/signed/zabbixsrv.fcn.edu.br.pem'
            Notice: Removing file Puppet::SSL::Certificate zabbixsrv.fcn.edu.br at '/var/lib/puppet/ssl/certs/zabbixsrv.fcn.edu.br.pem'


        - na maquina puppet agent

            # remove todos os certificados de puppet
            $ puppet agent --configprint ssldir
            /var/lib/puppet/ssl/*

            $ rm -r /var/lib/puppet/ssl/*

            $ puppet agent -t

            # remove umcertificado especifico
            $ find /var/lib/puppet/ssl -name zabbixsrv.fcn.edu.br.pem -delete



    ::: Error: /File[/var/cache/puppet/facts.d]: Failed to generate additional resources using 'eval_generate': 
        SSL_connect returned=1 errno=0 state=error: certificate verify failed (self signed certificate in certificate chain): 
        [self signed certificate in certificate chain for /CN=Puppet CA: zabbix.fcn.edu.br]

        - O problema foi resolvido com a exclusão do certificado do nó 
        (mv /var/lib/puppet/ssl /var/lib/puppet/ssl.original)

        $ puppet agent -t