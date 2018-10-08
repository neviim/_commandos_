# Docker remover

	::: Seguem alguns comandos úteis pro Docker

		# Remover todos os containers
			$ docker rm -f $(docker ps -qa)
		
		# Remover os containers parados (status exited)
			$ docker rm $(docker ps -qf status=exited)
		
		# Parar todos os containers
			$ docker stop $(docker ps -q)
		
		# Remover todas as imagens locais
			$ docker rmi $(docker images -qa)
		
		# Remove imagens sem tag (nome e tag = <none> no docker images)
			$ docker rmi $(docker images -qf dangling=true)
		
		# Remove volumes “órfãos”
			$ docker volume rm $(docker volume ls -qf dangling=true)
		
		# Mostra uso de recursos dos containers rodando (Contribuição: Wellington Silva)
			$ docker stats $(docker ps --format {{.Names}})