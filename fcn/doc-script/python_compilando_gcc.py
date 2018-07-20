# compilando o python 3.7

    ::: Compilando

        $ yum install gcc gcc-c++ openssl-devel bzip2-devel
        $ yum install libffi-devel

        $ cd /usr/src
        $ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

        $ tar xzf Python-3.7.0.tgz
        
        $ cd Python-3.7.0
        $ ./configure --enable-optimizations
        
        $ make
        $ sudo make altinstall

        $ rm /usr/src/Python-3.7.0.tgz
        $ python3.7 -V


    ::: Create virtualenv:

        $ virtualenv -p python3 venv

        