# Utilizando tcpdump

    ::: nmap

        # verifica se a porta 161 esta ok
        $ nmap -sU -p 161 10.0.9.18         # 161/udp open   snmp, esta ok
        $ nmap -sU -p 161 172.16.1.31       # 161/udp closed snmp, error

    ::: tcpdump
    
        $ tcpdump -i enp4s0 -A udp port 161 and src 10.0.9.39 or dst 10.0.9.18
        $ tcpdump -i enp1s0 -A udp port 161 and src 10.0.9.18 or dst 172.16.1.77


    ::: snmpbulkwalk

        # verifica se o serviço esta ativo
        $ snmpwalk -v2c -c COMUNIDAD 10.0.9.18

        # do server zabbixsrv
        $ snmpbulkwalk -v2c -c public 10.0.45.78        # Impressora Color: esta ok
        $ snmpbulkwalk -v2c -c public 10.0.9.18         # zabbixsrv: esta ok

        $ snmpbulkwalk -v2c -c public 172.16.1.31 .1.3.6.1.4.1.9.1.1069

        # do server zabbixsrv 
        $ snmpbulkwalk -v2c -c public 10.0.9.39         # mymaquina: Timeout: No Response from 10.0.9.39 
        $ snmpbulkwalk -v2c -c public 172.16.1.31       # wifi rede: Timeout: No Response from 172.16.1.31 



# template cisco zabbix:
#  
# (Cisco Aironet 702i)
# (1262N-E-K9 Cisco Aironet AIR-LAP1262N-E-K9) 
#
# https://dev.bitquell.de/tree/Zabbix!Configs.git/535ec7c7a9216a1335e26c363c2f258c107b4613/Templates!Templates%20Switche





# Captura: estando na maquina cliente 10.0.9.18 para 10.0.9.39 Server

    $ tcpdump -i enp4s0 -A udp port 161 and src 10.0.9.39 or dst 10.0.9.18

        tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
        listening on enp4s0, link-type EN10MB (Ethernet), capture size 262144 bytes
        14:45:51.483397 IP devops.fac.joaopauloii > zabbixsrv.fac.joaopauloii: ICMP echo reply, id 27811, seq 0, length 64
        E..T)q..@.+.
        .       '
        .       ....\l...........................................................
        14:45:52.484295 IP devops.fac.joaopauloii > zabbixsrv.fac.joaopauloii: ICMP echo reply, id 27811, seq 1, length 64
        E..T)...@.*.
        .       '
        .       ....[l...........................................................
        14:45:53.485405 IP devops.fac.joaopauloii > zabbixsrv.fac.joaopauloii: ICMP echo reply, id 27811, seq 2, length 64
        E..T+...@.(.
        .       '
        .       ....Zl...........................................................
        14:45:56.492941 ARP, Reply devops.fac.joaopauloii is-at 00:13:72:10:67:4b (oui Unknown), length 28
        ..........r.gK
        .       '@.\xXB
        .       .
        14:46:26.877696 ARP, Reply devops.fac.joaopauloii is-at 00:13:72:10:67:4b (oui Unknown), length 28
        ..........r.gK
        .       '@.\xXB
        .       .
        14:46:51.503240 IP devops.fac.joaopauloii > zabbixsrv.fac.joaopauloii: ICMP echo reply, id 27897, seq 0, length 64
        E..TF...@...
        .       '
        .       .....l...........................................................
        14:46:52.503923 IP devops.fac.joaopauloii > zabbixsrv.fac.joaopauloii: ICMP echo reply, id 27897, seq 1, length 64
        E..TG...@...
        .       '
        .       .....l...........................................................
        14:46:53.504717 IP devops.fac.joaopauloii > zabbixsrv.fac.joaopauloii: ICMP echo reply, id 27897, seq 2, length 64
        E..TH-..@..D
        .       '
        .       .....l...........................................................
        14:46:56.510758 ARP, Reply devops.fac.joaopauloii is-at 00:13:72:10:67:4b (oui Unknown), length 28
        ..........r.gK
        .       '@.\xXB
        .       .
        14:46:58.955822 ARP, Request who-has zabbixsrv.fac.joaopauloii tell fac32080.joaopauloii, length 46
        ........d.ggxJ
        .       .......
        .       ...................

        ^C
        14 packets captured
        14 packets received by filter
        0 packets dropped by kernel

# Captura: estando na maquina "server zabbixsrv" 10.0.9.18 para 10.0.45.78 "Impressora FCN_Color" 

    $ tcpdump -i enp1s0 -A udp port 161 and src 10.0.9.18 or dst 10.0.45.78

        tcpdump: verbose output suppressed, use -v or -vv for full protocol decode                                                        
        listening on enp1s0, link-type EN10MB (Ethernet), capture size 262144 bytes                                                       
        14:55:22.928788 IP zabbixsrv.fac.joaopauloii.36636 > devops.fac.joaopauloii.snmp:  GetRequest(28)  system.sysUpTime.0             
        E..G..@.@...                                                                                                                      
        .       .                                                                                                                         
        .       '.....3.#0).....public....|.F.......0.0...+.........                                                                      
        14:55:26.929732 IP zabbixsrv.fac.joaopauloii.36636 > devops.fac.joaopauloii.snmp:  GetRequest(28)  system.sysUpTime.0             
        E..G..@.@..w                                                                                                                      
        .       .                                                                                                                         
        .       '.....3.#0).....public....|.F.......0.0...+.........                                                                      
        14:55:40.970220 IP zabbixsrv.fac.joaopauloii.52317 > ap-fcn-new1.fac.joaopauloii.snmp:  GetRequest(28)  system.sysUpTime.0        
        E..G..@.@.9.                                                                                                                      
        .       .                                                                                                                         
        .       ..]...3..0).....public....|.F.......0.0...+.........                                                                      
        14:55:44.974388 IP zabbixsrv.fac.joaopauloii.52317 > ap-fcn-new1.fac.joaopauloii.snmp:  GetRequest(28)  system.sysUpTime.0        
        E..G..@.@.-.                                                                                                                      
        .       .                                                                                                                         
        .       ..]...3..0).....public....|.F.......0.0...+.........                                                                      
        14:55:57.145709 IP zabbixsrv.fac.joaopauloii.35017 > 10.0.45.78.snmp:  GetRequest(28)  system.sysUpTime.0                         
        E..G..@.@.5:                                                                                                                      
        .       .                                                                                                                         
        .-N.....3..0).....public....`S.Z......0.0...+.........                                                                            
        14:55:58.049428 IP zabbixsrv.fac.joaopauloii.60239 > 10.0.45.24.snmp:  GetRequest(28)  system.sysUpTime.0                         
        E..G3.@.@...                                                                                                                      
        .       .                                                                                                                         
        .-..O...3..0).....public..............0.0...+.........                                                                            
        14:56:11.011646 IP zabbixsrv.fac.joaopauloii.41013 > ap-fcn-new2.joaopauloii.snmp:  GetRequest(28)  system.sysUpTime.0            
        E..G..@.@..3                                                                                                                      
        .       ....M.5...3+.0).....public....|.F.......0.0...+.........                                                                  
        14:56:11.011646 IP zabbixsrv.fac.joaopauloii.41013 > ap-fcn-new2.joaopauloii.snmp:  GetRequest(28)  system.sysUpTime.0            
        E..G..@.@..3                                                                                                                      
        .       ....M.5...3+.0).....public....|.F.......0.0...+.........                                                                  
        14:56:12.013902 IP zabbixsrv.fac.joaopauloii.36059 > 172.16.1.31.snmp:  GetRequest(28)  system.sysUpTime.0                        
        E..G..@.@...                                                                                                                      
        .       ..........3?.0).....public....a.........0.0...+.........                                                                  
        14:56:15.015811 IP zabbixsrv.fac.joaopauloii.41013 > ap-fcn-new2.joaopauloii.snmp:  GetRequest(28)  system.sysUpTime.0            
        E..G..@.@...                                                                                                                      
        .       ....M.5...3+.0).....public....|.F.......0.0...+.........                                                                  
        14:56:16.018078 IP zabbixsrv.fac.joaopauloii.36059 > 172.16.1.31.snmp:  GetRequest(28)  system.sysUpTime.0                        
        E..G..@.@...                                                                                                                      
        .       ..........3?.0).....public....a.........0.0...+.........                                                                  
        ^C                                                                                                                                
        10 packets captured                                                                                                               
        11 packets received by filter                                                                                                     
        0 packets dropped by kernel       

# Erro usando o SNMP 

    # Para o Agente zabbix
    ::: Desta vez, vamos tratar como lidar com esse erro quando o tempo limite ao conectar-se ao 
        erro '192.168.1.1: 161' por tal monitoramento Zabbix.  "SNMP - Timeout while connecting to 172.16.1.31:161"

        $ zabbix_get -s 10.0.9.18 -k agent.version
        '3.4.11'

    # Para o Agente SNMP
    ::: Se você estiver usando o agente SNMP para monitoramento, execute o seguinte comando no servidor 
        em que o Zabbix Manager está instalado.

        $ snmpwalk -v 2c -c public 10.0.9.19 .
        $ snmpwalk -v 2c -c public 10.0.9.39 .
        'Timeout: No Response from 10.0.9.39'

