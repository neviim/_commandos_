# login altomatico linux

	::: passos

		$ yum install ssh
		$ ssh-keygen -t rsa -b 4096

		$ cd /root/.ssh
		$ cd C:\Users\jorge.FCN/.ssh

		$ scp id_rsa.pub neviim@10.0.9.18:/home/neviim
		$ ssh neviim@10.0.9.18

		$ cd /root/.ssh
		$ cat /home/neviim/id_rsa.pub >> authorized_keys
		$ cat authorized_keys

		# windows

		$ nano /etc/ssh/sshd_config

			PermitRootLogin yes

		# Reinicie o serviço ssh, no caso no debian ou ubuntu
		$ service ssh restart

		λ mkdir %CMDER_ROOT%\config\.ssh
		λ ssh-keygen -o -a 100 -t ed25519 -f %CMDER_ROOT%\config\.ssh\id_ed25519
