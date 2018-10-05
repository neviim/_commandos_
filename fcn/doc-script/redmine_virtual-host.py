# nano /etc/httpd/conf.d/redmine.conf

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