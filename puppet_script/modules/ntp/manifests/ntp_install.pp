# Authors
# -------
#
# Author Neviim <jorge@fcn.edu.br>
#
# Copyright
# ---------
#
# Copyright 2018 Your name here, unless otherwise noted.
#
class ntp::ntp_install {

    # distribuiçao familia
    case $::operatingsystem {
        ubuntu: {
            $package_name = 'ntp'
            $service_name = 'ntp'
            $conf_file    = 'ntp.conf'
        }
    }

    # declara pacote
    package {[
        "$package_name",
        "ntpdate",
        "ntpstat",
        ]:
        ensure => present,
    }

    # declara o arquivo de configuração
    file { '/etc/ntp.conf':
        ensure   => file,
        replace  => true,
        owner    => 'root',
        group    => 'root',
        mode     => '0644',
        source   => 'puppet:///modules/ntp/ntp.conf',
    }

    # altera zona paea São Paulo
    exec { 'zonainfo - SP':
        command  => 'ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime',
        path     => '/bin', 
    }

    # restarta o serviço NTP
    exec { 'ntp restart':
        command     => 'service ntp restart',
        path        => '/bin',
        refreshonly => true,
        subscribe   => File['/etc/ntp.conf'],
    }

}