# Criando um ambiente virtual usando conda e VSCode

	::: 

		$ conda create --prefix C:\path_do_projeto\py37\ python=3.7

		$ conda activate C:\path_do_projeto\py37
		$ conda deactivate


		::: Na configuração do launch.json do VSCode, defina o seu 'pythonPath' para:

			"pythonPath":"${workspaceRoot}/awesomeEnv/python.exe"