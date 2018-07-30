# montando partição

    $ df -h /dev/sda1
    $ df -h -T /dev/sda1
    $ df -a /dev/sda1

    $ df -h --output=source,fstype,size,used,avail,pcent,target -x tmpfs -x devtmpfs
    /dev/md126: PTTYPE="dos"
    /dev/md126p1: UUID="8a313df3-8986-42fc-90c1-f4afcfdfcc27" TYPE="ext4"
    /dev/md126p5: UUID="abfd7801-5ad7-4f1f-9a5b-8a47694fb59c" TYPE="swap"


    # Opçao 1 - 

        $ cp /etc/fstab /etc/fstab.orig
        
        $ nano /etc/fstab

            /dev/md126p1 /mnt/hd450   ext4    defaults    0 2


        # Verifica se ha algum erro no arquivo.
        $ mount -a





    # Opsao 2 - montar uma hd linux

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

    