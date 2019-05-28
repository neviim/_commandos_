# Por.: Neviim
# data: 09/05/2018

	::: Instalando agent zabbix 3.4.13

		# para versão do zabbix server 3.4.13
		$ yum install http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-agent-3.4.13-1.el7.x86_64.rpm
		$ yum install http://repo.zabbix.com/zabbix/3.4/rhel/7/x86_64/zabbix-sender-3.4.13-1.el7.x86_64.rpm

		# Zabbix agent configuration is /etc/zabbix/zabbix_agentd.conf
		$ cat /etc/zabbix/zabbix_agentd.conf

			$ nano /etc/zabbix/zabbix_agentd.conf

				Server=192.168.10.2
				ServerActive=192.168.10.2
				Hostname=proxy.lab.com

		# reinicializa servico
		$ systemctl start application.service
		$ systemctl reload application.service
    $ systemctl enable application.service

		# verificar a porta de serviço se estiver ouvindo
		$ ss -tunelp | grep 10050

		$ sudo iptables -A INPUT -p tcp -m tcp --dport 10050 -j ACCEPT

		$ sudo iptables-save > /etc/iptables-regra
		$ sudo iptables-restore < /etc/iptables-regras

		# https://10.0.9.88:81
