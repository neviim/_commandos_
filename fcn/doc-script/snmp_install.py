# instalando snmp

    ::: alguns pacotes snmp

        $ yum search net | grep snmp

        net-snmp-agent-libs.i686 : The NET-SNMP runtime agent libraries
        net-snmp-agent-libs.x86_64 : The NET-SNMP runtime agent libraries
        net-snmp-devel.i686 : The development environment for the NET-SNMP project
        net-snmp-devel.x86_64 : The development environment for the NET-SNMP project
        net-snmp-libs.i686 : The NET-SNMP runtime client libraries
        net-snmp-libs.x86_64 : The NET-SNMP runtime client libraries
        net-snmp-perl.x86_64 : The perl NET-SNMP module and the mib2c tool
        net-snmp-python.x86_64 : The Python 'netsnmp' module for the Net-SNMP
        net-snmp-sysvinit.x86_64 : Legacy SysV init scripts for Net-SNMP daemons
        net-snmp-utils.x86_64 : Network management utilities using SNMP, from the
        erlang-snmp.x86_64 : Simple Network Management Protocol (SNMP) support
        fence-agents-eaton-snmp.x86_64 : Fence agent for Eaton network power switches
        net-snmp.x86_64 : A collection of SNMP protocol tools and libraries
        net-snmp-gui.x86_64 : An interactive graphical MIB browser for SNMP
        pcp-pmda-snmp.x86_64 : Performance Co-Pilot (PCP) metrics for Simple Network


    ::: instalando snmp 

        $ yum install -y net-snmp


        - O comando seguinte mudará o nome do arquivo de configuração original do SNMP

            $ mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf_original

            $ nano /etc/snmp/snmpd.conf

                # Map 'idv90we3rnov90wer' community to the 'ConfigUser'
                # Map '209ijvfwer0df92jd' community to the 'AllUser'
                #       sec.name        source          community
                com2sec ConfigUser      default         idv90we3rnov90wer
                com2sec AllUser         default         209ijvfwer0df92jd
                # Map 'ConfigUser' to 'ConfigGroup' for SNMP Version 2c
                # Map 'AllUser' to 'AllGroup' for SNMP Version 2c
                #                       sec.model       sec.name
                group   ConfigGroup     v2c             ConfigUser
                group   AllGroup        v2c             AllUser
                # Define 'SystemView', which includes everything under .1.3.6.1.2.1.1 (or .1.3.6.1.2.1.25.1)
                # Define 'AllView', which includes everything under .1
                #                       incl/excl       subtree
                view    SystemView      included        .1.3.6.1.2.1.1
                view    SystemView      included        .1.3.6.1.2.1.25.1.1
                view    AllView         included        .1
                # Give 'ConfigGroup' read access to objects in the view 'SystemView'
                # Give 'AllGroup' read access to objects in the view 'AllView'
                #                       context model   level   prefix  read            write   notify
                access  ConfigGroup     ""      any     noauth  exact   SystemView      none    none
                access  AllGroup        ""      any     noauth  exact   AllView         none    none


        # restartando e testando 

        $ systemctl enable snmpd.service

        $ systemctl stop snmpd.service
        $ systemctl start snmpd.service
        $ systemctl restart snmpd.service

        $ chkconfig snmpd on
        $ snmpwalk -v 2c -c idv90we3rnov90wer -O e 127.0.0.1
        $ snmpwalk -v 2c -c 209ijvfwer0df92jd -O e 127.0.0.1








# referencias
    # configurando snmp
    http://tecdistro.com/how-to-install-snmp-in-redhat-7centos-7/