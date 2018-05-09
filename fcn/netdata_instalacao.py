# Instalando NetData monitoramento.

    :: dependencias da instalaçoes
        $ apt install zlib1g-dev gcc make git autoconf autogen automake pkg-config
        $ apt install libuuid-devel uuid-dev

    :: instalaçoes
        $ git clone https://github.com/firehol/netdata
        $ cd netdata
        $ ./netdata-installer.sh

        $ sudo ln -s /root/install/netdata/netdata-updater.sh /etc/cron.daily/netdata-updater


# Em caso desta ser a maquina server alterar para ela passar a anunciar-se

    :: Alterar: https://10.0.5.29 -> IP do proprio servidor
        
        $ nano /etc/netdata/netdata.conf

            [registry]
                enabled = yes
                registry to announce = https://10.0.5.29



# Em caso deste ser um cliente e ter que mandar seus dados a um servidor.

    :: Alterar, obs: 'https://10.0.5.29' -> IP do proprio servidor netdata
        
        $ nano /etc/netdata/netdata.conf

            [registry]
                registry to announce = https://10.0.5.29

        - desta forma este criente estara se conectando la no servidor 
          cujo ip é '10.0.5.29'


# Pos instalação

    :: Verificar status do serviço

        $ systemctl status netdata
        $ systemctl start  netdata
        $ systemctl stop   netdata

        http://ip.da.maquina:19999/


# Verificando instalação.

    $ netstat -plnt | grep netdata
    tcp        0      0 127.0.0.1:8125          0.0.0.0:*               LISTEN      23733/netdata
    tcp        0      0 0.0.0.0:19999           0.0.0.0:*               LISTEN      23733/netdata
    tcp6       0      0 ::1:8125                :::*                    LISTEN      23733/netdata
    tcp6       0      0 :::19999                :::*                    LISTEN      23733/netdata
