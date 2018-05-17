# instalar PHP

    :: Se você instalou o php7.2-fpm acima, e usando o Apache, o a2enconf php7.2 
       fará o Apache usar o PHP 7.2 FPM. Digite a2disconf php7.1-fpm para 
       desabilitar as configurações existentes do FPM.

        $  apt install php7.2 php7.2-common php7.2-cli php7.2-fpm


    :: Apache com php-fpm

        - Antes de removermos os pacotes PHP antigos, certifique-se de que o seu servidor web use corretamente
          os PHP7.2sockets/modules. Se você instalou o 'php7.2-fpm' acima, e usando o Apache, o 'a2enconf php7.2' 
          fará o Apache usar o PHP 7.2 FPM. Digite 'a2disconf php7.1-fpm' para desabilitar as configurações 
          existentes do FPM.

            $ a2disconf php7.1-fpm

            - As etapas seriam semelhantes para o Nginx.


        - Você pode desabilitar a integração atual do PHP com o 'a2dismod php7.1' (ou sua versão atual) e habilitar 
          o novo módulo PHP 7.2 com 'a2enmod php7.2'.

            $ a2dismod php7.1
            $ a2enmod php7.2


        - Se tudo estiver funcionando bem (verifique seu phpinfo () e php --info), você pode remover os pacotes antigos:

            $ apt purge php7.1*






        $ php --info


