# superdesck


	::: 

		# server
		$ cd $path/server
		$ pip install -r requirements.txt
		$ python manage.py app:initialize_data
		$ python manage.py users:create -u admin -p admin -e 'admin@example.com' --admin

		# se você precisar de alguns dados
		$ python manage.py app:prepopulate

		# start server
		$ honcho start



	:::

		# client
		$ cd $path/client
		$ npm install

		$ grunt server

		# open http://localhost:9000 in browser



	::: docker verificando como utilizar

		# docker run superdesk ./scripts/fig_wrapper.sh python3 manage.py users:create -u admin -p admin -e 'usuario@fcn.edu.br' --admin