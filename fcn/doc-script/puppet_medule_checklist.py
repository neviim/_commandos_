# criar um novo modulo

    :: lablist, para manter definido o que pode estar instaldo ou não.
    
        $ cd /etc/puppet/code/environments/production/modules
        $ puppet module generate jads-lablist --skip-interview


        :: Criando um manifesto:

            $ nano pacotes.pp

                class lablist::pacotes {

                        package { ['tree']:
                                ensure => absent,
                        }

                        package { ['openssh']:
                                ensure => latest,
                        }

                        package { ['htop']:
                                ensure => present,
                        }

                }

            $ puppet parser validate pacotes.pp


    - A definição do node (node são os clientes rodando o puppet client, são seus hosts no geral).

        $ cd /etc/puppet/code/environments/production/manifests
        $ nano site.pp

            node default {
            }

            node 'teste1.fcn.edu.br' {
                include dev::hosts
                include lablist::pacotes
            }

        $ puppet parser validate pacotes.pp

        # pode ser em um cliente.
        $ puppet agent -t 



# referencia
    http://fullstack-puppet-docs.readthedocs.io/en/latest/puppet_modules.html