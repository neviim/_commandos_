# 

    ::: Dica adicional de como liberar a porta udp 161 (SNMP) no iptables:

        $ iptables -A INPUT  -p tcp --dport 161 -j ACCEPT
        $ iptables -A OUTPUT -p tcp --sport 161 -j ACCEPT
        $ iptables -A INPUT  -p udp --dport 161 -j ACCEPT
        $ iptables -A OUTPUT -p udp --sport 161 -j ACCEPT
        $ iptables -L -n 







# Referencia
    # 2.3.3. CONFIGURANDO O FIREWALL IPTABLES PARA PERMITIR COMPONENTES DO CLUSTER.
    https://access.redhat.com/documentation/pt-br/red_hat_enterprise_linux/6/html/cluster_administration/s2-iptables_firewall-ca