# Instalando Liveblog, gerenciador de times para poste de materis

	::: https://github.com/liveblog/liveblog

		# instalado maquina teste Dell380
		$ yum install mongodb redis-server


    ::: Instalando java para centos7 [https://tecadmin.net/install-java-8-on-centos-rhel-and-fedora/]
    	# instalado maquina teste tilab
        $ wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jdk-8u181-linux-x64.tar.gz"
        $ tar -zxvf jdk-8u*-linux-x64.tar.gz
        $ mv jdk1.8.*/ /usr/

        $ alternatives --install /usr/bin/java java /usr/jdk1.8.*/bin/java 2
        $ alternatives --config java

        $ java –version

        ::: 
            $ export JAVA_HOME=/usr/jdk1.8.0_*
            $ export JRE_HOME=/usr/jdk1.8.0_*/jre/
            $ export PATH=$JAVA_HOME/bin:$PATH


    ::: Instalando nodejs

    	# maquina teste devops 
    	$ yum install nodejs
    	$ yum install python3

    	# instalar grunt-cli
    	$ npm install -g grunt-cli

    	# instalar liveblog-server
    	$ mkdir /usr/share/liveblog-server
    	$ cd /usr/share/liveblog-server

    		::: cria ambiente python virtual

    			$ virtualenv -p python3.6 liveblogVenv
    			$ source liveblogVenv/bin/activate

    			$ git clone https://github.com/liveblog/liveblog.git

    			$ cd ./liveblog/server
    			$ pip install --upgrade setuptools
    			$ pip install -r requirements.txt

				$ python manage.py app:initialize_data;
				$ python manage.py users:create -u admin -p admin -e 'admin@example.com' --admin ;
				$ python manage.py register_local_themes ;

				# Ainda no virtualenv, agora você pode iniciar o servidor
				$ honcho -f ../docker/Procfile-dev start

				# Cliente
				$ cd ../client 
				$ npm install 


			::: Criar usuario no server

				$ python manage.py users:create -u <username> -p <password> -e <email>
				$ python manage.py users:create -u neviim -p senhajads -e neviim@gmail.com


			::: Agora podemos executar o servidor do cliente:

				$ grunt --force server --server='http://localhost:5000/api' --ws='ws://localhost:5100'

				# Agora você pode acessar sua cópia local em http: // localhost: 9000 
				# (usuário: admin, senha: admin)


				http://10.0.9.95:9000






