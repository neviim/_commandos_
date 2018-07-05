# 
    ::: descompactando um pacote src.rpm

        - Você deve instalar pacotes de origem como um usuário não raiz. Para fazer isso, você precisa instalar o pacote rpmdevtools. 
          Para construir uma árvore fonte a partir de um pacote rpm, você também precisa do rpm-build.

        - Um exemplo vamos baixar um pacote rpm e extrair ele para ter acesso aos codigos fontes.

          [jorge]$  wget https://repo.zabbix.com/zabbix/3.4/rhel/7/SRPMS/zabbix-3.4.10-1.el7.src.rpm
          [jorge]$   
