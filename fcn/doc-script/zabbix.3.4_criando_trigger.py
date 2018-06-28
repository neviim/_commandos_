# Algumas configuraçoes uteis:

    ::: gatilho que me envie alerta com o nome de usuário que logou para este servidor

        Primeiro você deve criar um gatilho no seu item

        '''
        Name: User login {ITEM.LASTVALUE} found on {HOSTNAME}
        Severity: Lets say WARNING for example
        Expression: {YOURHOSTNAME:system.run[query user].str()}=1
        '''

        Marque a caixa de seleção 'Permitir fechamento manual', caso contrário o gatilho ficará 
        ativo para sempre com esta caixa habilitada você pode reconhecê-lo, e o gatilho desaparecerá 

        Então vá para Configuração> ações e crie uma ação 
        New Condition: trigger name como Login do usuário 
        Agora, nas operações, configure as operações necessárias 

        ps: para fechar o gatilho, na visualização do gatilho, clique na coluna ack no no e marque 
            a caixa de seleção Fechar problema