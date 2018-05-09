# Instalando NetData monitoramento.

    :: dependencias da instalaçoes
        $ apt install zlib1g-dev gcc make git autoconf autogen automake pkg-config
        $ apt install libuuid-devel
        $ apt install uuid-dev

    :: instalaçoes
        $ git clone https://github.com/firehol/netdata
        $ cd netdata
        $ ./netdata-installer.sh

        $ sudo ln -s /root/install/netdata/netdata-updater.sh /etc/cron.daily/netdata-updater

# Pos instalação

    $ systemctl start netdata
    $ systemctl stop  netdata

    http://ip.da.maquina:19999/

