# NTP configurando para server brasil.

    :: servidores do brasil

        a.st1.ntp.br	200.160.7.186 e 2001:12ff:0:7::186
        b.st1.ntp.br	201.49.148.135
        c.st1.ntp.br	200.186.125.195
        d.st1.ntp.br	200.192.232.8
        a.ntp.br	    200.160.0.8 e 2001:12ff::8
        b.ntp.br	    200.189.40.8
        c.ntp.br	    200.192.232.8
        gps.ntp.br	    200.160.7.193 e 2001:12ff:0:7::193


        :: Se você utiliza GNU/Linux, FreeBSD ou Solaris, use o comando zic para modificar o arquivo correspondente ao seu fuso horário:

            - 1. Crie um arquivo com extensão .zic na pasta onde está o arquivo do fuso horário utilizado. Por exemplo, se você utiliza Brazil/East, 
                crie o arquivo /usr/share/zoneinfo/Brazil/verao.zic. O conteúdo é o seguinte:

                $ nano /usr/share/zoneinfo/Brazil/verao.zic

                    Rule Brazil 2015 only - May 30 00:00 1 S
                    Rule Brazil 2015 only - Jun 22 00:00 0 -
                    Zone Brazil/East -3:00 Brazil BR%sT

                $ zic verao.zic



    :: instalando e configurando NTP Server:

        $ apt install ntp 
        $ apt install ntpstart 
        $ apt install ntpdate 


        :: servidores publicos 

            $ nano /etc/ntp.conf

                server a.ntp.br
                server b.ntp.br
                server c.ntp.br


        :: setando zona info para São Paulo, caso não esteja:

            $ ls -ls /etc/localtime
            /etc/localtime -> /usr/share/zoneinfo/Etc/UTC

            $ /etc/init.d/ntp stop
            $ rm /etc/localtime
            $ ln -s /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
            $ /etc/init.d/ntp start


            :: Caso seja necessário corrigir o horário manualmente:

                $ date -s "xx:xx:xx"
                $ clock -w


        - Sincronize o relógio do sistema com o servidor a.ntp.br manualmente 
          (use este comando apenas uma vez, ou conforme necessário):

            $ ntpdate a.ntp.br


        # monitorando syslog - log NTP
        $ tail -f /var/log/syslog | grep ntpd
        $ ntpdate -q pool.ntp.br




