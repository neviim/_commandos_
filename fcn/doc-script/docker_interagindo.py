# imagens do docker

	::: start o serviço docker

		$ systemctl start docker.service

	::: carregar imagens

		$ docker pull centos
		$ docker pull ubuntu
		$ docker images 
		
		$ docker rm -f exemplo01 

		$ docker run -dt --name exemplo01 centos
		#  -dt 					- Modo deimom em segundo plano 
		# --nome exemplo01 		- nome do container
		# centos            	- nome da imagem a ser utilizada

		$ docker run -dt --name exemplo02 ubuntu
		#  -it 					- Modo interativo 
		# --nome exemplo02 		- nome do container
		# centos            	- nome da imagem a ser utilizada

			Ctrl+p+q			- sai do container sem sair fechar ele.

		# como voltar para o container que sai
		$ docker exec -it exemplo02 bash
		root@f6f6c715b143:/# 
		# por não tem entrado em modo interativo, mas por exec, pode dar exit que não matara o container.

		root@f6f6c715b143:/# exit
		$

		$ docker ps
		# posso formatar esta saida, usando as formataçoes de Go, docker foi desenvolvido em go.
		$ docker ps --format '{{.Names}}, {{.Image}}\n{{.Status}}, Portas: {{.Ports}}\n'

		# para colocar este comando no .bashrc ou .zshrc, crie esta função.
		$ nano ~/.zshrc

			function docker.ps.loop() {
				watch -n 3 -t "docker ps --format '{{.Names}}, {{.Image}}\n{{.Status}}, Portas: {{.Ports}}\n'"
			} 

		$ docker.ps.loop

		# podemos restartar e parar esta container
		$ docker restart exemplo02
		$ docker stop exemplo02
		$ docker start exemplo02

		$ docker ps -la
		$ docker exec exemplo02 ls -lha /etc
		$ docker exec exemplo02 ls -lha /etc | grep rc

		# Commitar uma imagem personalizada com minhas configuraçoes
		$ docker commit exemplo02 jadsid/ubuntu-master:1.0
		$ docker images 

		# contruir uma container a partir de uma imagens ja criada.
		$ docker run -it --name exemplo03 jadsid/ubuntu-master:1.0
		root@bbd4c4258947:/#

		# criando um dockerfile
		$ mkdir ~/docker-exe
		$ cd ~/docker-exe
		$ touch exemplo04.txt

		$ nano dockerfile

			FROM jadsid/ubuntu-master:1.0

			ADD exemplo04 /etc/exemplo04.txt

			ENV DEBIAN_FRONTEND noninteractive
			ENV PKG=git

			RUN apt-get -y install $PKG


		# vamos contruir uma imagem com build usando o dockerfile
		$ docker build -t jadsid/ubuntu-master:1.1 .
		...
		---> 2da3f0e13fe2
		Removing intermediate container 25f36dbb8b30
		Successfully built 2da3f0e13fe2

		# parado aqui...
		# https://www.youtube.com/watch?v=JUZEPeqkajY


