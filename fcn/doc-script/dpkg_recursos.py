# dpkg

    ::: Como descobrir a qual pacote um arquivo pertence

        $ apt-file list nomedopacote
        $ dpkg -S stdio.h



    ::: Para saber de quais pacotes ele depende, apenas:

        $ apt-cache depends penguin-command


    ::: saber nome do pacote instalado no sistema

        $ dpkg -l | grep mozilla
        $ COLUMNS=132 dpkg -l | grep mozilla
        


# referencia 
    https://www.debian.org/doc/manuals/apt-howto/ch-search.pt-br.html