# arangoDB 3 (https://www.arangodb.com/tutorials/tutorial-python/)

	::: instalando pacote

		$ pip install pyarango --user


	::: Se conectando ao banco

		>>> from pyArango.connection import *
		>>> conn = Connection(arangoURL="http://10.0.9.18:8529", username="twitter", password="twitter")

		
