# certificados

    ::: find

        $:> find /var/lib/puppet/ssl -name zabbix.fac.joaopauloii.pem -delete
        c:> del "\var\lib\puppet\ssl\certs\zabbix.fac.joaopauloii.pem" /f


    ::: revoke - apagar

        $ puppet cert list --all
        $ puppet cert revoke zabbix.dominio
        
        $ puppet cert clean zabbix.dominio
        $ puppet cert list --all


    ::: valida todos de uma vez

        $ puppet cert sign --all 

        


