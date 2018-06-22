# comando para backup

    :: /mnt/hd450 - hd especifica para backup

        # Fazer BACKUP
        $ tar -cvf /mnt/hd450/Backup/tar_etc_bak/etc-backup-11_06_2018.tar /etc

        $ ls -ls /mnt/hd450/Backup/tar_etc_bak



    # Cuidado ...

        :: 'RESTAURA', muito cuidado nesta hora, isso ira reescrever todo /etc,
           use com moderação por sua conta e risco.

            $ tar -xvjf /mnt/hd450/Backup/tar_etc_bak/etc-backup.tar -C /