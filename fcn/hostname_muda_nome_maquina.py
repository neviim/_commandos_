# Como mudar o nome do host no Ubuntu 18.04 Bionic

    ::: verifica nome atual

        $ hostnamectl
        Static hostname: puppetmaster
                Icon name: computer-desktop
                Chassis: desktop
                Machine ID: e8d4e71101e8416c9d7566163f9d5cde
                Boot ID: f3bf210aa9404cf8a0e55b63efa7239b
        Operating System: Ubuntu 18.04 LTS
                    Kernel: Linux 4.15.0-23-generic
            Architecture: x86-64

        $ hostnamectl set-hostname puppetmaster


    :::

         $ nano /etc/cloud/cloud.cfg

            # This will cause the set+update hostname module to not operate (if true)
            preserve_hostname: false