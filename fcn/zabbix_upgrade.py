# upgrade zabbix

    :: backup

        $ mkdir /mnt/hd450/Backup/zabbix_backup

        :: zabbix conf

            $ cp /etc/zabbix/zabbix_server.conf /mnt/hd450/Backup/zabbix_backup
            $ cp /etc/apache2/conf-enabled/zabbix.conf /mnt/hd450/Backup/zabbix_backup

        
        :: arquivo php e zabbix binario:

            $ cp -R /usr/share/zabbix/ /mnt/hd450/Backup/zabbix_backup
            $ cp -R /usr/share/doc/zabbix-* /mnt/hd450/Backup/zabbix_backup

        
    :: remove repositorio

        $ rm -Rf /etc/apt/sources.list.d/zabbix.list

    

# instalar

    :: Ubuntu 18.04 run:

        $ wget http://repo.zabbix.com/zabbix/3.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_3.4-1+bionic_all.deb
        $ dpkg -i zabbix-release_3.4-1+bionic_all.deb

        # usando apt
        $ apt update
        $ apt upgrade zabbix-server-mysql zabbix-frontend-php zabbix-agent

        # usando apt-get
        $ apt-get update
        $ apt-get install --only-upgrade zabbix-server-mysql zabbix-frontend-php zabbix-agent


    :: start

        $ systemctl start zabbix-server.service
        $ systemctl start zabbix-agent.service