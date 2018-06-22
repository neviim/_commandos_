# iptables -F
# iptables -t nat -F
# /etc/rc.d/init.d/iptables start

#!/bin/bash
iniciar () {

REDE_INT=192.168.10.0/24
FIREWALL=192.168.254.201
OWNCLOUD=192.168.10.4
ZABBIX=192.168.10.254
ASTERISK=192.168.10.2
WINSERVER=192.168.10.253
XP=192.168.10.9
ANY=0.0.0.0/0
IF_EXT=eth0
IF_INT=eth1

#Limpas as regras 
iptables -F
iptables -t mangle -F
iptables -t mangle -X
iptables -t nat -F
modprobe ip_conntrack

#Politica padrao
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

#Inicia o fail2ban 
/etc/init.d/fail2ban restart

#inicia o psad
/etc/init.d/psad restart

#Habilita o roteamento 
echo 1 > /proc/sys/net/ipv4/ip_forward

#Drop e log de pacotes inválidos
iptables -t filter -A INPUT -m state --state INVALID -j LOG --log-prefix=" Pacotes invalidos eth0 " --log-level crit  
iptables -t filter -A INPUT -m state --state INVALID -j DROP
iptables -t filter -A FORWARD -m state --state INVALID -j DROP

#Libera o acesso a loopback
iptables -t filter -A INPUT -i lo -j ACCEPT

#Libera o a acesso a rede local 
iptables -t filter -A INPUT -s $REDE_INT -i $IF_INT  -j ACCEPT

#DNS 53 udp prioriza o trafego
#Protocolo dns udp porta 53 
iptables -t mangle -A INPUT -s $REDE_INT -i $IF_INT -m udp -p udp --sport 53 -j TOS --set-tos 8
iptables -t mangle -A FORWARD -s $REDE_INT -o $IF_EXT -m udp -p udp --sport 53 -j TOS --set-tos 8
iptables -t mangle -A POSTROUTING -s $REDE_INT -o $IF_EXT -m udp -p udp --sport 53 -j TOS --set-tos 8

#Priorizando o tráfego com o tos
#Tráfego de entrada e saída no protocolo ssh na porta 22 do fireawall
iptables -t mangle -A INPUT -s $REDE_INT -i $IF_INT -p tcp --dport 22 -j TOS --set-tos 4
iptables -t mangle -A OUTPUT -s $REDE_INT -o $IF_EXT -p tcp --dport 22 -j TOS --set-tos 4

#Priorida máxima do tos p/ gmail
for i in 80 433 ;do
iptables -t mangle -A INPUT -s $REDE_INT -i $IF_INT -m tcp -p tcp --sport $i -j TOS --set-tos 16
iptables -t mangle -A FORWARD -s $REDE_INT -o $IF_EXT -m tcp -p tcp --dport $i -j TOS --set-tos 16
iptables -t mangle -A POSTROUTING -s $REDE_INT -o $IF_EXT -m tcp -p tcp --sport $i -j TOS --set-tos 16
done

for w in 21 22 ;do
#Portas que estão abertas no firewall
iptables -t filter -A INPUT -i $IF_EXT -p tcp  --dport $w -j LOG --log-prefix=" Acesso ao ssh " --log-level crit
iptables -t filter -A INPUT -i $IF_EXT -p tcp  --dport $w -j ACCEPT
done

for x in 465 587 110 143;do
iptables -t mangle -A INPUT  -s $REDE_INT -i $IF_EXT -m tcp -p tcp --dport $i -j TOS --set-tos 16
iptables -t mangle -A FORWARD -s $REDE_INT -i $IF_INT -m tcp -p tcp --dport $x -j TOS --set-tos 16
iptables -t filter -A FORWARD -s $REDE_INT -i $IF_INT -m tcp -p tcp --dport $x -j ACCEPT
iptables -t mangle  -A POSTROUTING -s $REDE_INT -o $IF_EXT -m tcp -p tcp --sport $x -j TOS --set-tos 16
iptables -t nat -A POSTROUTING -s $REDE_INT -o $IF_EXT -m tcp -p tcp --sport $x -j SNAT --to $FIREWALL
done

#DNS 53 udp
#Protocolo dns udp porta 53 
iptables -t filter -A FORWARD -s $REDE_INT -i $IF_INT -m udp -p udp --dport 53 -j ACCEPT
iptables -t nat -A POSTROUTING -s $REDE_INT -o $IF_EXT -m udp -p udp --sport 53 -j SNAT --to $FIREWALL

#Libera o ping para rede interna
iptables -t filter -A INPUT -s $REDE_INT -i $IF_INT -p icmp  -j ACCEPT
iptables -t nat -A POSTROUTING -s $REDE_INT -o $IF_EXT -p icmp -j SNAT --to $FIREWALL

#Libera o acesso para os servidores internos ter acesso para fora
#Servidor owncloud
iptables -t filter -A FORWARD -s $OWNCLOUD -i $IF_INT  -j ACCEPT 
iptables -t nat  -A POSTROUTING  -s $OWNCLOUD -o $IF_EXT -d $ANY  -j SNAT --to $FIREWALL

#Servidor zabbix
iptables -t filter -A FORWARD -s $ZABBIX -i $IF_INT  -j ACCEPT
iptables -t nat  -A POSTROUTING  -s $ZABBIX -o $IF_EXT -d $ANY  -j SNAT --to $FIREWALL

#Servidor asterisk
iptables -t filter -A FORWARD -s $ASTERISK  -i $IF_INT  -j ACCEPT
iptables -t nat  -A POSTROUTING  -s $ASTERISK -o $IF_EXT -d $ANY  -j SNAT --to $FIREWALL

#Servidor winserver
iptables -t filter -A FORWARD -s $WINSERVER  -i $IF_INT  -j ACCEPT
iptables -t nat  -A POSTROUTING  -s $WINSERVER -o $IF_EXT -d $ANY  -j SNAT --to $FIREWALL

#REGRAS ADCIONAIS DE SEGURANÇA

# sync
iptables -A INPUT -i $IF_EXT -p tcp ! --syn -m state --state NEW -m limit --limit 5/m --limit-burst 7 -j LOG --log-level crit --log-prefix=" Drop Syn"
iptables -A INPUT -i $IF_EXT -p tcp ! --syn -m state --state NEW -j DROP
 
#Fragmentos
iptables -A INPUT -i $IF_EXT -f -m limit --limit 5/m --limit-burst 7 -j LOG --log-prefix=" Fragments Packets " --log-level crit 
iptables -A INPUT -i $IF_EXT -f -j DROP

# bloquear bad stuff
iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags ALL FIN,URG,PSH -j DROP
iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags ALL ALL -j DROP

iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags ALL NONE -m limit --limit 5/m --limit-burst 7 -j LOG --log-prefix=" NULL Packets " --log-level crit
iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags ALL NONE -j DROP #NULL Packets

iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP
iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags SYN,FIN SYN,FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-prefix=" XMAS Packets " --log-level crit 
 
iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP #XMAS

iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags FIN,ACK FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-prefix=" Fin Packets Scan " --log-level crit

iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags FIN,ACK FIN -j DROP # FIN packet scans

iptables -A INPUT -i $IF_EXT -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP

#Liberar toda conexão de saída, sem entrada stuff
iptables -A INPUT -i $IF_EXT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -o $IF_EXT -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

# liberar entradas ICMP ping pong stuff
iptables -A INPUT -p icmp --icmp-type 8 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -p icmp --icmp-type 0 -m state --state ESTABLISHED,RELATED -j ACCEPT

#BLOQUEIA O PING DA MORTE
iptables -t filter -A INPUT -i $IF_EXT -p tcp --syn -m limit --limit 1/s -j ACCEPT 

 #Não compartilhar pacotes smb/windows
iptables -A INPUT -p tcp -i $IF_EXT --dport 137:139 -j REJECT
iptables -A INPUT -p udp -i $IF_EXT --dport 137:139 -j REJECT
#O SERVIDOR NAO PARTICIPA INVOLUTARIAMENTE DE ATAQUES DE DOS
echo 0 > /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts

#BLOQUEIO DE ATAQUES SYN/FLOOD -DOS OU DED
echo 1 >  /proc/sys/net/ipv4/tcp_syncookies

#RP_FILTER FAZ COM QUE O FIREWALL SÓ RESPONDA A REQUISICOES DA MESMA INTERFACE
echo 1 > /proc/sys/net/ipv4/conf/default/rp_filter

#Redirecionamentos para servidores internos 
#REDIRECIONAMENTO DA PORTA WEB  PARA MAQUINA LOCAL OWNCLOUD 
iptables -t filter -A FORWARD -s $ANY -d $OWNCLOUD  -i $IF_EXT -m tcp -p tcp --dport 80 -j LOG --log-prefix=" Acesso ao owncloud " --log-level crit
iptables -t nat -A PREROUTING -s $ANY -d $FIREWALL -m tcp -p tcp --dport 8081 -j DNAT --to $OWNCLOUD:80
iptables -t filter -A FORWARD -s $ANY -d $OWNCLOUD  -i $IF_EXT -m tcp -p tcp --dport 80 -j ACCEPT
iptables -t nat -A POSTROUTING -s $OWNCLOUD -d $ANY -m tcp -p tcp --sport 80 -j SNAT --to $OWNCLOUD:8081

#REDIRECIONAMENTO DA PORTA SSH  PARA A MAQUINA LOCAL OWNCLOUD
iptables -t filter -A FORWARD -s $ANY -d $OWNCLOUD  -i $IF_EXT -m tcp -p tcp --dport 22 -j LOG --log-prefix=" Acesso ao ssh owncloud " --log-level crit
iptables -t nat -A PREROUTING -s $ANY -d $FIREWALL -m tcp -p tcp --dport 2122  -j DNAT --to $OWNCLOUD:22
iptables -t filter -A FORWARD -s $ANY -d $OWNCLOUD  -i $IF_EXT -m tcp -p tcp --dport 22 -j ACCEPT
iptables -t nat -A POSTROUTING -s $OWNCLOUD -d $ANY -m tcp -p tcp --sport 22 -j SNAT --to $OWNCLOUD:2122

#REDIRECIONAMENTO RPD  PARA MAQUINA LOCAL XP
iptables -t filter -A FORWARD -s $ANY -d $XP  -i $IF_EXT -m tcp -p tcp --dport 3389 -j LOG --log-prefix=" Acesso ao TS XP " --log-level crit
iptables -t nat -A PREROUTING -s $ANY -d $FIREWALL -m tcp -p tcp --dport 3377 -j DNAT --to $XP:3389
iptables -t filter -A FORWARD -s $ANY -d $XP  -i $IF_EXT -m tcp -p tcp --dport 3389 -j ACCEPT
iptables -t nat -A POSTROUTING -s $XP -d $ANY -m tcp -p tcp --sport 3389 -j SNAT --to $XP:3377

#REDIRECIONAMENTO PARA ZABBIX  SSH 
iptables -t filter -A FORWARD -s $ANY -d $ZABBIX  -i $IF_EXT -m tcp -p tcp --dport 22 -j LOG --log-prefix=" Acesso ao ssh zabbix " --log-level crit
iptables -t nat -A PREROUTING -s $ANY -d $FIREWALL -m tcp -p tcp --dport 23 -j DNAT --to $ZABBIX:22
iptables -t filter -A FORWARD -s $ANY -d $ZABBIX  -i $IF_EXT -m tcp -p tcp --dport 22 -j ACCEPT
iptables -t nat -A POSTROUTING -s $ZABBIX -d $ANY -m tcp -p tcp --sport 22 -j SNAT --to $ZABBIX:23

#REDIRECIONAMENTO PARA O ZABBIX HTTP
iptables -t filter -A FORWARD -s $ANY -d $ZABBIX  -i $IF_EXT -m tcp -p tcp --dport 80 -j LOG --log-prefix=" Acesso a porta 80 zabbix " --log-level crit
iptables -t nat -A PREROUTING -s $ANY -d $FIREWALL -m tcp -p tcp --dport 81 -j DNAT --to $ZABBIX:80
iptables -t filter -A FORWARD -s $ANY -d $ZABBIX  -i $IF_EXT -m tcp -p tcp --dport 80 -j ACCEPT
iptables -t nat -A POSTROUTING -s $ZABBIX -d $ANY -m tcp -p tcp --sport 80 -j SNAT --to $ZABBIX:81

# Logar qualquer coisa, se tiver suspeita de invasores
# *** Requer o psad ****
iptables -A INPUT -j LOG
iptables -A FORWARD -j LOG
iptables -A INPUT -j DROP

#LIBERA CONEXOES ESTABELECIDAS
iptables -t filter -A INPUT -m state --state ESTABLISHED,RELATED,NEW -j ACCEPT 
iptables -t filter -A FORWARD -m state --state ESTABLISHED,RELATED,NEW -j ACCEPT 
iptables -t filter -A OUTPUT -m state --state ESTABLISHED,RELATED,NEW -j ACCEPT

#BLOQUEIA TUDO O QUE FOR PACOTE TCP EXCETO O QUE FOI LIBERADO
iptables -t filter -A INPUT -p tcp --syn -j DROP
iptables -t filter -A FORWARD -p tcp --syn -j DROP
iptables -t filter -A OUTPUT -p tcp --syn -j DROP

#BLOQUEIA AS PORTA BAIXAS UDP 0:1023
iptables -A INPUT -p udp --dport 0:1023 -j DROP

echo "Firewall ativado!  :....................[ok]"

}

parar(){
echo 0 > /proc/sys/net/ipv4/ip_forward
/etc/init.d/fail2ban stop
/etc/init.d/psad stop
psad -F
iptables -t mangle -F
iptables -t nat -F
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F
iptables -X
echo "Firewall desativado! :..................[ok]"

}

case "$1" in
"start") iniciar;;
"stop") parar;;
"restart") parar; iniciar;;
*) echo "use: sh /sbin/firewall (star/stop/restart)"
esac