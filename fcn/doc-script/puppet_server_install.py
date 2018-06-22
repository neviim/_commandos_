# pupper server install

    $ apt update
    $ apt install puppetserver

    $ systemctl start puppet.service

    
    $ puppet --version
    5.4.0


    $ puppet resource user              # lista todos os usuarios
    $ puppet resource user `whoami`     # usuario atual


    $ puppet agent -t
    $ puppet agent --test


    