# instalando redmine

	::: dependencias

		- CentOS is installed and works
		- Apache is installed and works
		- MySQL is installed and works

		# instalando...

		$ yum -y install zlib-devel curl-devel openssl-devel httpd-devel apr-devel apr-util-devel mysql-devel
		$ yum install ImageMagick-devel
		$ yum install gcc-c++
		$ yum -y install net-tools

		$ wget https://cache.ruby-lang.org/pub/ruby/2.5/ruby-2.5.1.tar.gz
		$ ./configure
		$ make
		$ sudo make install

		$ gem install passenger
		$ gem install bundler
		$ passenger-install-apache2-module

		$ systemctl start httpd.service
		$ systemctl status httpd.service

		$ cd /usr/src 
		$ mkdir /var/www/redmine
		$ wget http://www.redmine.org/releases/redmine-3.4.6.tar.gz
		$ cp -av redmine-3.4.6/* /var/www/redmine
		$ cd /var/www/html/redmine

		# Abra o Gemfile do seu aplicativo e adicione 'passageiro':
		$ nano Gemfile

			gem "passenger", ">= 5.3.5", require: "phusion_passenger/rack_handler"

		
		$ bundle install
		$ bundle exec passenger --version
		Phusion Passenger 5.3.5

		$ yum install mariadb-server -y
		$ systemctl enable mariadb
		$ systemctl start mariadb

		$ mysql_secure_installation

		# configurando mysql redmine

		$ mysql -u root -p

		MariaDB [(none)]> create database redmine character set utf8;
		MariaDB [(none)]> create user 'redmine'@'localhost' identified by 'redmine';
		MariaDB [(none)]> grant all privileges on redmine.* to 'redmine'@'localhost'; 
		MariaDB [(none)]> exit

		$ pwd
		/var/www/html/redmine

		$ cp config/database.yml.example config/database.yml
		$ cp config/configuration.yml.example config/configuration.yml
		
		$ nano nano config/environment.rb  (opcional)

			ENV['RAILS_ENV'] ||= 'production'
			RAILS_ENV=production bundle exec rake db:migrate
			RAILS_ENV=production bundle exec rake redmine:load_default_data


		# Rename dispatch CGI files in /var/www/redmine/public/

		$ mv dispatch.fcgi.example dispatch.fcgi
		$ mv htaccess.fcgi.example .htaccess

		$ cd /var/www/html/
		$ chown -R apache:apache redmine

		# configurar o apache para rodar o redmine

		$ yum install libtool httpd-devel apr-devel apr
		$ cd /usr/local/src/

		# ajustes finais

		$ nano database.yml
		$ bundle install
		$ rake generate_secret_token
		$ RAILS_ENV=production rake db:migrate
		$ RAILS_ENV=production rake redmine:load_default_data

		$ chmod -R 755 files log tmp public plugins

		# parei aqui: https://youtu.be/f5kZ61soba4?t=1653
		$ find / -name passenger
		$ find / -name mod_passenger.so

		# configurando redmine.conf
		$ nano /etc/httpd/conf.d/redmine.conf

			LoadModule passenger_module /usr/local/lib/ruby/gems/2.5.0/gems/passenger-5.3.5/buildout/apache2/mod_passenger.so
			PassengerRoot /usr/local/lib/ruby/gems/2.5.0/gems/passenger-5.3.5
			PassengerDefaultRuby ruby 

			Listen 8080

			<VirtualHost *:8080>
				DocumentRoot /var/www/html/redmine/public
				ServerName localhost
				#ServerAdmin root@localhost
				#ErrorLog logs/redmine_error_log

				#If you are using mod_fcgid and are going to upload files larger than
				#131072 bytes you should consider adding the following line
				#that allows to upload files up to 20 mb
				#MaxRequestLen 20971520

				<Directory "/var/www/html/redmine/public">
					#Options Indexes ExecCGI FollowSymLinks
					#Order allow,deny
					Allow from all
					#AllowOverride all
				</Directory>
			</VirtualHost>



		$ RAILS_ENV=production rake redmine:load_default_data
		pt-BR

		$ systemctl restart httpd.service
		$ systemctl status httpd.service




		# Isso é tudo pessoal!



# Erros:

	::: Permission denied (errno=13)

		[ N 2018-10-04 13:13:17.7711 7006/T5 age/Cor/SecurityUpdateChecker.h:517 ]: Security update check: no update found (next check in 24 hours)
		[ E 2018-10-04 13:14:38.8609 7006/Ti age/Cor/App/Implementation.cpp:221 ]: Could not spawn process for application /var/www/html/redmine: An operating system error occurred while preparing to spawn an application process: Cannot create FIFO file /tmp/passenger.spawn.XXXXcn2BQK/response/finish: Permission denied (errno=13)
		  Error ID: 36698a2c
		  Error details saved to: /tmp/passenger-error-IVmQxo.html

			
		$ chmod +t /tmp


# Usando Docker

$ docker run -d --name some-mysql -e MYSQL_ROOT_PASSWORD=redmine -e MYSQL_DATABASE=redmine mysql