# usando jupyter com o vccode

	::: https://marketplace.visualstudio.com/items?itemName=donjayamanne.jupyter

		- No vsCode instalar o plugin jupyter, configura o arquivo: keybindings.json


	::: depoios de subir o anaconda jupyter, abrir um arquivo para pegar o token.

		- No VS Code:

			ctrl+shift+p
			Jupyter: Enter the url of local/remote Jupyter Notebook

		- No windows linha de comando, ja usando a maquina virtual py37, ou outra que tenha criado execute.

			$ (py37) C:\>jupyter notebook list
			Currently running servers:
			http://localhost:8888/?token=6031a497d4a65e264ea5874d47f49d2ac27b758dedc4d408 :: C:\Users\jorge.FCN
			http://localhost:8888/?token=f414b5de973f421c3317aabe88ea75b32bc957ae567918c7 :: C:\Users\jorge.FCN

			(py37) C:\>

