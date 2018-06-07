# puppet master

    :: puppetfile

        - Quase todos os manifestos Puppet são mantidos em módulos, coleções de código Puppet e dados com uma estrutura de diretórios específica. 
          Por padrão, Code Manager e r10k instalam conteúdo em um diretório de módulos (./modules) no mesmo diretório no qual o Puppetfile está. 
          Por exemplo, declarar o módulo puppetlabs-apache no Puppetfile normalmente instala o módulo em ./modules/apache. Para aprender mais sobre 
          módulos, consulte a documentação do módulo.



    :: puppet manifesto

        %> puppet module install puppetlabs-chocolatey --version 3.0.0
        %> cd /etc/puppet/code/environments/production/modules/lablist/manifests

        %> nano /etc/puppet/code/environments/production/manifests/site.pp
        %> nano /etc/puppet/code/environments/production/modules/lablist/manifests/pacotes.pp 


    :: puppet parser validate um manifesto

        %> puppet parser validate pacotes.pp 


    :: Aplique o arquivo de manifesto.

        %> puppet apply --certname meu_projeto puppet-www.pp

