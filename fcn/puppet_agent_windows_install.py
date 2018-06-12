# Instalando o agente puppet em uma maquina cliente.
#

    :: EM um pendrive colocar a versão puppet-agent-5.4.0-x64 e instalar 
       na maquina windows, fazer as ateraçoes abaixo para efetuar e
       receber a chave liberada no servidor.
	   
	   - Abrir o CMD como administrador
	   
			c:\ ipconfig /all 
			
			- aqui listara os dados completo desta maquina, caso precise saber
			  o hostename "nome" da mesma para identifica-la na altenticação
			  no server (puppet-master)
			  

	:: Ao executar o programa ele lhe perguntara duas opção o diretorio de
	   instalação e o nome do dominio do puppet master, este você altera para:
	   
	
        zabbix.fcn.edu.br 
	   
	   
	   
	    - precione o botão Install
	   
	   
	    - Ao termino ele crio este arquivo a baixo com a configuração do puppet
		  apontando para o server, em caso de precisar conferir ele se encontra 
		  nesta pasta. Do mais o sistema puppet ja devera esta funcionando 
		  corretamente.
		  
		  
            C:\> cat 'C:\ProgramData\PuppetLabs\puppet\etc\puppet.conf'  

                [main]
                server=zabbix.fcn.edu.br
                autoflush=true


    :: Solicita ao puppet server sua autenticação

		C:\> puppet agent --server *MasterName* --waitforcert 60 --test
		C:\> puppet agent --test -waitforcert=60
        Exiting; no certificate found and waitforcert is disabled
		  

        - correndo tudo certo podera confirmar a solicitação la no puppet-server.

            $ puppet cert sign <nome_maquina>
            '''
               Signing Certificate Request for:
              "maquina.fcn.edu.br" (SHA256) 28:4A:38:47:6E:8C:EC:2D:20:0C:94:06:26:2E:25:B2:FD:41:7D:57:B2:C6:14:49:C3:34:70:A9:5F:54:42:1C
               Notice: Signed certificate request for maquina.fcn.edu.br
               Notice: Removing file Puppet::SSL::CertificateRequest maquina.fcn.edu.br at '/var/lib/puppet/ssl/ca/requests/maquina.fcn.edu.br.pem' '''

			   
		:: estando confirmado, dentro de 30 minutos os pacotes necessarios poderão 
		   estar sendo instalados, para verificar se esta tudo certo, pode executar 
		   o seguinte comando, no prompt do windows:
		   
		   C:\ puppet agent -t
		   
		   
		   - não ocorrendo erro, o cliente puppet estara instalado e configurado.
		   
		   
		   
		   
''' resumo da seguencia dos comandos:

	- Apos instalar o puppet-agent.
	- Abrir o CMD como administrador
	
		c:\> puppet agent --test -waitforcert=60
		
		#### ESPERAR LIBERA A CHAVE SOLICITADA AO SERVIDOR PUPPET ###
		
		c:\> puppet agent -t
		
		:: os soft necessario complementar serão instalados altomaticamente...
	

'''
	
