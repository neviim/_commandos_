# manifesto, referencia de uso das classes

    ::: aplicar um manifesto

        $ puppet apply c:\test.pp


# usando windows
    file { 'c:/mysql/my.ini':
        ensure => 'file',
        mode   => '0660',
        owner  => 'mysql',
        group  => 'Administrators',
        source => 'N:/software/mysql/my.ini',
    }


    ::: somente se?

        exec { 'logrotate':
        path     => '/usr/bin:/usr/sbin:/bin',
        provider => shell,
        onlyif   => 'test `du /var/log/messages | cut -f1` -gt 100000',
        }


    ::: template
        # epp(<FILE REFERENCE>, [<PARAMETER HASH>])
        file { '/etc/ntp.conf':
        ensure  => file,
        content => epp('ntp/ntp.conf.epp', {'service_name' => 'xntpd', 'iburst_enable' => true}),
        # Loads /etc/puppetlabs/code/environments/production/modules/ntp/templates/ntp.conf.epp
        }

        # template(<FILE REFERENCE>, [<ADDITIONAL FILES>, ...])
        file { '/etc/ntp.conf':
        ensure  => file,
        content => template('ntp/ntp.conf.erb'),
        # Loads /etc/puppetlabs/code/environments/production/modules/ntp/templates/ntp.conf.erb
        }


    ::: outra referencia template

        # meu projeto
        /etc/my-project/a.ini
        /etc/my-project/b.ini
        /etc/my-project/c.ini


        define myFile( $file_name ) {
            # multiplos arquivos
            file { "/ect/init.d/${file_name}.ini":
                ensure  => file,
                content => template("myProject/myFiles/${file_name}.erb"),
            }
        }

        $values = {
            item_1 => {file_name => "a"},
            item_2 => {file_name => "b"},
            item_3 => {file_name => "c"}
        }

        create_resources(myFile, $values)



    ::: Executa o puppet a cada 5 minutos

        # ajusta agendamento de execução
        scheduled_task { 'Run Puppet Every 5 Minutes':  
        ensure    => present,
        enabled   => true,
        command   => 'C:/Program Files/Puppet Labs/Puppet/bin/puppet.bat',
        arguments => 'apply C:/puppet',
        working_dir => 'C:/Program Files/Puppet Labs/Puppet/bin/',
        trigger   => {
            schedule   => daily,
            start_time => '08:00',
            minutes_interval => 5,
            minutes_duration => 60,
        }
        }



# referencia

    # puppet windows
    https://github.com/counsyl/puppet-windows
    http://liamjbennett.me/post/2013-10-06-puppet-on-windows-part-1/

    #
    https://puppet.com/docs/puppet/4.10/lang_windows_file_paths.html
