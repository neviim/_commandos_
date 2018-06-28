# 
    $ df -h /dev/sda1
    $ df -h -T /dev/sda1
    $ df -a /dev/sda1



# montar uma hd linux

    $ mount /dev/md126p1 /mnt/hd450

# Crie um arquivo para seu script e escreva os comandos nele.

    $ sudo nano /etc/init.d/SEUSCRIPT
        Exemplo:

        #!/bin/bash 
        echo "Script de exemplo"

    $ sudo chmod 755 /etc/init.d/SEUSCRIPT


    - Registra o script para ser executado na inicialização

        $ sudo update-rc.d SEUSCRIPT defaults

        # demora um pouquinho para retornar ao prompt

    