# 

    ::: regra gpsv

         "^(sppsvc|gpsv|Pml Driver HPZ12)$" with "[Result is FALSE]" for now in the Regulair expression option of "Windows service names for discovery"






# referencias
    # filtro nas regras de descobertas
    https://www.zabbix.com/documentation/3.4/manual/discovery/low_level_discovery



# teste
# https://www.zabbix.com/forum/zabbix-help/52050-windows-services-messages (esta opção para desativar gpsvc - sppsvc)


    ::: Se você quiser excluir aqueles que estão agitando, como eu fiz, vá para:

        'Administration' -> 'General' e à direita em um 'dropdown' encontrar:

        Seção de 'expressões regulares'.
        Encontre 'descoberta de serviço do Windows' na lista
        Basta adicionar outra expressão que, '[Result is FALSE]'
        
            Expression: ^(<SERVICE1>|<SERVICE2>)$

        # Definindo uma nova espresao regurar
        Coloque a expressao abaixo com o resultado em false "[Result is FALSE]" para a nova regular expresao de "Windows service names for discovery"

            ^(sppsvc|gpsv|Pml Driver HPZ12)$          
    
        Supostamente o alarme deverá desaparecer depois de um tempo.


        ::: exemplo de espressoes
       
            "[Result is FALSE]"
        
                ^(MMCSS|gupdate|SysmonLog|clr_optimization_v2.0.50727_32|clr_optimization_v4.0.30319_32)$

