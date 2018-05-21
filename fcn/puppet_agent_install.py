# puppet agent

    :: https://downloads.puppetlabs.com/windows/puppet/

        - Usando o puppet server 5.4.0

        :: O agente puppet sera instalado em:

            - C:\Program Files\Puppet Labs\Puppet\
            - puppet


    :: Instalar utilizando Choco

        C:\> choco install puppet-agent -y
        C:\> choco install puppet-agent --version 5.4.0
        C:\> choco upgrade puppet-agent --version 5.4.0

        - Você pode passar installArgs para Chocolatey para várias propriedades. 
          Consulte http://docs.puppetlabs.com/puppet/latest/reference/install_windows.htmlmsi-properties 
          para as propriedades exatas. Você passaria pelos argumentos para o instalador usando 'installArgs'. 
          Aqui está um exemplo de mudar a localização do Puppet Master, caso o master tiver um nome diferente 
          de 'puppet':

          # -installArgs '"PUPPET_MASTER_SERVER=puppet.fqdn.com"'

          C:\> choco install puppet-agent -installArgs '"PUPPET_MASTER_SERVER=puppet-1.domain.com"' -y --version 5.4.0

          C:\> cat 'C:\ProgramData\PuppetLabs\puppet\etc\puppet.conf'  

            [main]
            server=zabbix.fcn.edu.br
            autoflush=true


        - Solicita ao puppet server sua autenticação

          C:\> puppet agent --test –waitforcert=60
            '''
            Info: Caching certificate for ca
            Info: csr_attributes file loading from C:/ProgramData/PuppetLabs/puppet/etc/csr_attributes.yaml
            Info: Creating a new SSL certificate request for maquina.fcn.edu.br
            Info: Certificate Request fingerprint (SHA256): 28:4A:38:47:6E:8C:EC:2D:20:0C:94:06:26:2E:25:B2:FD:41:7D:57:B2:C6:14:49:C3:34:70:A9:5F:54:42:1C
            Info: Caching certificate for ca
            Exiting; no certificate found and waitforcert is disabled '''

            - correndo tudo certo podera confirmar a alyenticação no server.

                $ puppet cert sign <nome_maquina>
                '''
                Signing Certificate Request for:
                "maquina.fcn.edu.br" (SHA256) 28:4A:38:47:6E:8C:EC:2D:20:0C:94:06:26:2E:25:B2:FD:41:7D:57:B2:C6:14:49:C3:34:70:A9:5F:54:42:1C
                Notice: Signed certificate request for maquina.fcn.edu.br
                Notice: Removing file Puppet::SSL::CertificateRequest maquina.fcn.edu.br at '/var/lib/puppet/ssl/ca/requests/maquina.fcn.edu.br.pem' '''


    :: Testando o resultado final da implantação:

        - Teste no cliente usando PowerShell com um comando puppet agent -t. 
          Observe que, por padrão, o puppet agente é executado a cada 30 minutos:

          C:\> puppet agent -t



# Referencia
    # instalando puppet cliente no windows
    https://www.youtube.com/watch?v=vOLaMDyYtcI
    https://chocolatey.org/packages/puppet-agent/1.2.2
    https://blog.ipswitch.com/managing-windows-with-puppet
    http://www.tomsitpro.com/articles/puppet-agent-on-windows,1-3681.html

