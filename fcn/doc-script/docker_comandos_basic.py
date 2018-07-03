# docker images

    $ docker images
    $ docker search (parametro)
    
    $ docker ps 
    $ docker ps -a

    $ docker stats (id ou apelido do container)
    $ docker stats bfb37c3e9a59

    # lista detalhes da configuração docker container
    $ docker inspect (id da imagem ou container)
    $ docker inspect bfb37c3e9a59


    # deletar imagem
    $ docker rmi (nome da imagem)


    # Com o exec nós podemos executar qualquer comando nos nossos contêineres sem precisarmos estar na console deles.
    $ docker exec (id_container ou nome_container) 

        Vejamos a baixo alguns dos parâmetros que podemos utilizar com ele:

        -i permite interagir com o container
        -t associa o seu terminal ao terminal do container
        -it é apenas uma forma reduzida de escrever -i -t
        --name algum-nome permite atribuir um nome ao container em execução
        -p 8080:80 mapeia a porta 80 do container para a porta 8080 do host
        -d executa o container em background
        -v /pasta/host:/pasta/container cria um volume '/pasta/container' dentro do container com o conteúdo da pasta '/pasta/host' do host






# referencias
    # resumo de comandos basicos que podem ser utilizados com docker
    https://medium.com/@programadriano/principais-comandos-docker-f9b02e6944cd
