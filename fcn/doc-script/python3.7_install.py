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


		::: criar um env

			$ python3 -m venv tutorial-env
			$ virtualenv -p python3.7 py37


		::: colocar debuge para funcionar [referencia: https://github.com/Microsoft/vscode-python/issues/1828]

			# testa se o serve esta conectando
			$ python -m http.server -b localhost 62775

			#
			$ pip install ptvsd --pre

			$ python -m ptvsd --server --port 62775 --file codigo.py

			# no lauch sera criado 
			$ .vscode/launch.json

		        {
		            "name": "Attach (Remote Debug)",
		            "type": "pythonExperimental",
		            "request": "attach",
		            "port": 62775,
		            "host": "localhost"
		        },

		    # no ambiente vscode terminal ele esta funcionando com estes parametros
		    PS D:\__GitHub-Projetos\_python_projetos\terremotos> cd 'd:\__GitHub-Projetos\_python_projetos\terremotos'; 
		         ${env:PYTHONIOENCODING}='UTF-8'; ${env:PYTHONUNBUFFERED}='1'; ${env:PYTHONPATH}='c:\Users\jorge.FCN\.vscode\extensions\ms-python.python-2018.8.0\pythonFiles\experimental\ptvsd'; & 
		         'D:\__CondaVirtual\pytr37\python.exe' '-m' 'ptvsd' '--host' 'localhost' '--port' '1193' 'd:\__GitHub-Projetos\_python_projetos\terremotos\src\alerta_nt7.py'


