# icecast servidor broadcast de audio

	::: instalando

		$ yum install icecast


	::: configurando o serviço.

		$ icecast -c /etc/icecast.xml -b
		

	::: Usando no VLC config streamer: Rede
	    (http://write.flossmanuals.net/vlc/streaming-to-icecast/)

		:sout=#duplicate{dst=std{access=http,mux=ogg,dst=pwdicecast@10.0.9.95:8000/live}}


