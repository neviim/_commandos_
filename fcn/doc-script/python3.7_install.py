# instalando pythom 3.7

	::: compilando

		$ yum install gcc openssl-devel bzip2-devel
		$ cd /usr/src
		$ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
		$ tar xzf Python-3.7.0.tgz
		$ cd Python-3.7.0
		$ ./configure --enable-optimizations
		$ make altinstall
		$ rm /usr/src/Python-3.7.0.tgz

		$ python3.7 -V