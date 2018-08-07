# comandos de rede
    ::
    $ lsof -i tcp                   # portas abertas
    $ nmap -sT -O localhost         # verifica quais portas estão abertas
    $ cat /etc/resolv.conf
    $ mii-tool                      # verificar se a placa de rede está conectada, a velocidade do link o modo de operação

    $ tcpdump -S -q -i eth0 src 10.0.9.41

    $ free -m -t                    # memória em MB e o -t faz um cálculo de RAM + SWAP
    $ tail -f /var/log/syslog

    $ service --status-all
    $ systemctl list-unit-files

    $ cat /etc/*-release                # Verifica qial distribuição esta sendo otilizada
    $ cat /etc/*-release | grep PRETTY  
    $ cat /proc/version 
    
    # comandos de stree
    $ stress --vm 2 --vm-bytes 256M

    
      
