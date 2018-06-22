# instalando module puppet zabbix

    ::: Na instalação padrão tive que alterar em params.pp para php7.2 deu erro no procedimento 
        padrão da instalação em um modulo php7, desistalando um modulos anteriores e reinstalar 
        manualmente funciono, isso para a nova versão do ubuntu server 18.04

        $ sudo apt-get purge apache2 
        $ sudo apt-get purge php5 libapache2-mod-php5 
        $ sudo apt-get purge autoremove 
        $ sudo apt-get install apache2 libapache2-mod-php7.2 php7.2 




