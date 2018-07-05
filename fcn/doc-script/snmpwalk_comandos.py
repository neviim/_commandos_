# 
    ::: instalando snmpwalk

        $ yum install net-snmp-utils
        $ snmpwalk --help
        Version:  5.7.2
        Web:      http://www.net-snmp.org/

    :::

        $ snmpwalk -v 2c -c public localhost
        $ snmpwalk -v 2c -c public localhost iso.3.6.1.2.1.1.6.0
        $ snmpwalk -v 2c -c public -M /root/ismail/ciscoMIB localhost iso.3.6.1.2.1.1.6.0






# referencia
    https://library.netapp.com/ecmdocs/ECMP1368834/html/GUID-113EA449-1EBA-46F2-B954-76A9F36C3FD8.html