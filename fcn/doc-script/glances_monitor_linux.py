# Última versão pronta para produção do Glances

    :: instalação

        $ curl -L https://bit.ly/glances | /bin/bash
        $ wget -O- https://bit.ly/glances | /bin/bash


    :: usando:

        $ glances


# monitoramento remoto

    :: Se você quiser monitorar remotamente uma máquina, chamada servidor, de outra, chamada cliente, basta executar no servidor:

        - Onde @servidor é o endereço IP ou o nome do host do servidor.

        server$ glances -s        
        client$ glances -c @server


    :: Se você quiser monitorar remotamente uma máquina, chamada servidor, de qualquer dispositivo com um navegador da Web, 
       basta executar o servidor com a opção -w:

       $ glances -w


        :: em seguida, no cliente, digite o seguinte URL no seu navegador da Web:

            - http://@server:61208

        :: para atualizar a página a cada 10 segundos:

            - http://@server:61208/10


# Referencias:
    http://glances.readthedocs.io/en/latest/quickstart.html