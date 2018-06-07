# puppte apply

    ::: Puppet mostre o que ele modificaria sem executar essas alterações adicionando o sinalizador --noop

        $ puppet apply --noop your_file.pp



    ::: Se você quiser ver qual versão de um pacote o Puppet acha que está instalado, 
        você pode usar a ferramenta Recurso de Marionetes:

        $ puppet resource package atom 

    
    ::: O Puppet possui uma ferramenta interna para ajudá-lo a descobrir todos os diferentes atributos 
        associados a um recurso chamado Descrever. Por exemplo:

        -  Retorna uma descrição do recurso de serviço e uma lista completa de todos os 
           atributos e seus valores válidos associados.

        $ puppet describe service
        $ puppet describe --list  



# referencias
    http://wragg.io/getting-started-with-puppet-on-windows/
    http://ai.stanford.edu/~llao/puppet/puppet-trainning.html