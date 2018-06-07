# comandos remotos

	::: Verificar se o WinRM permite que o Windows PowerShell se conecte

		%> net start winrm

		:::
			%> winrm get winrm/config/client/auth
			
				Auth
				Basic = true
				Digest = true
				Kerberos = true
				Negotiate = true
				Certificate = true
				CredSSP = false

			%> winrm set winrm/config/client/auth @{Basic="true"}


	::: puppet parser valide

		%> puppet parser validate selinux.pp

		%> alias jcp='cp -r /home/local/FCN/jorge/src/puppet/modules/ntp/* /etc/puppet/code/environments/production/modules/ntp'
		%> jcp



	:: copy server teste

		:: cd /home/local/FCN/jorge/src/puppet/modules/ntp
		
			%> cp -r /home/local/FCN/jorge/src/puppet/modules/ntp/* /etc/puppet/code/environments/production/modules/ntp



	:: Criando modulo

		%> puppet module generate jads-dev --skip-interview
		%> puppet parser validate init.pp

		