# comandos de rede
    ::
    $ lsof -i tcp                   # portas abertas
    $ nmap -sT -O localhost         # verifica quais portas estão abertas
    $ cat /etc/resolv.conf
    $ mii-tool                      # verificar se a placa de rede está conectada, a velocidade do link o modo de operação

    $ tcpdump -S -q -i eth0 src 10.0.9.41