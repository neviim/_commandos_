#
# https://glpi-install.readthedocs.io/en/latest/command-line.html#cdline-install

	::: mysql cria este banco

			database: dbglpi
			user: glpi
			pwd: glpipassword


			# 10.0.9.18

			# backup
			$ mysqldump -u root -p --all-databases > all.sql

			# Upgrade Mariadb
			https://linuxadmin.io/mariadb-upgrade-mysql/


			$ cd /var/www/html/glpi
			$ php scripts/cliinstall.php --db=dbglpi --user=glpi --pass=glpipassword