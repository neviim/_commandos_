# como alterar o logotipo do Zabbix Frontend na página de login e no canto superior esquerdo do painel. 

    ::: root @ ylplzbx01: ~ # cp /usr/share/zabbix/styles/dark-theme.css{,.otg}
    ::: root @ ylplzbx01: ~ # cp /usr/share/zabbix/styles/blue-theme.css{,.org}


        * Signin Logo

            - Use FTP ou outras ferramentas para inserir seu logotipo personalizado no diretório /usr/share/zabbix/img/, 
            neste tutorial estamos usando um logotipo png com uma dimensão 280px x 30px chamado signin-logo.png

            - Abra agora o dark-theme.css e o blue-theme.css e faça a seguinte modificação:


        .signin-logo {
            margem: 0 auto;
            margem-fundo: 21px;
            altura: 30px;
            background: url (../ img / signin-logo.png) sem repetição 0;  }


        * Logotipo do painel superior esquerdo

            - Para alterar o logotipo do Painel superior esquerdo do Zabbix Frontend , usamos um logotipo png personalizado com 
            dimensão 95px x 25px com nome de logotipo do painel inserido no diretório /usr/share/zabbix/img/

            - Abra o dark-theme.css e o blue-theme.css e faça a seguinte modificação:

        
                .logo {
                    float: esquerda;
                    display: bloco;
                    largura: 95px;
                    altura: 25 px;
                    background: url (../ img / dashboard-logo.png) não-repetir 0;  }

                .browser-logo-chrome {
                    plano de fundo: url (../ img / dashboard-logo.png) no-repeat 0 0;  }

                .browser-logo-ff {
                    background: url (../ img / dashboard-logo.png) sem repetição;  }

                .browser-logo-ie {
                    background: url (../ img / dashboard-logo.png) não-repetir 0;  }

                .browser-logo-opera {
                    background: url (../ img / dashboard-logo.png) não-repetir 0;  }

                .browser-logo-safari {
                    background: url (../ img / dashboard-logo.png) não-repetir 0;  }



    - Uma vez que você tenha feito a modificação, reinicie o serviço apache.

        $ systemctl restart apache2 # para o sistema operacional Ubuntu
        $ systemctl restart httpd   # Para CentOS 7 / RHEL OS
