# criando uma nova key ssh para git

	::: https://help.github.com/articles/connecting-to-github-with-ssh/

		$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
		
		$ # start the ssh-agent in the background
		$ eval $(ssh-agent -s)
		$ ssh-add ~/.ssh/id_rsa

		$ sudo yum install clip

		$ clip < ~/.ssh/id_rsa.pub

