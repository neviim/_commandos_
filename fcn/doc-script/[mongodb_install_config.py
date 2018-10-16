# instalando mongodb centos 7

	::: Colocar repositorio MongoDB 

		$ nano /etc/yum.repos.d/mongodb-org.repo

			[mongodb-org-4.0]
			name=MongoDB Repository
			baseurl=https://repo.mongodb.org/yum/redhat/7/mongodb-org/4.0/x86_64/
			gpgcheck=1
			enabled=1
			gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc


		$ yum repolist
		$ yum install mongodb-org
		$ systemctl start mongod.service
		$ systemctl status mongod.service


	::: Master e Slave


