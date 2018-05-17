# install elasticsearch mac

	:: dependencias

		$ java -version

		- Instalar java 1.8 (http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)



	:: instalando elasticsearch:

		$ brew install nginx

		$ nano /usr/local/etc/nginx/nginx.conf

		$ brew services start nginx



	:: elasticsearch

		$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

		$ brew update
		
		$ brew install elasticsearch
		$ brew install kibana
		$ brew install logstash


		:: config:

			$ nano /usr/local/etc/kibana/kibana.yml

				server.port: 5601
				elasticsearch.url: "http://localhost:9200”

			
			:: Se tudo correr bem, abra o Kibana em 'http://localhost:5601/status'
			
				- Você deveria ver a pagina de status


			:: precisará criar um novo arquivo de configuração do Logstash:

				$ nano /etc/logstash/conf.d/syslog.conf

					input {
					file {
						path => [ "/var/log/*.log", "/var/log/messages", "/var/log/syslog" ]
						type => "syslog"
					}
					}
					
					filter {
					if [type] == "syslog" {
						grok {
						match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?: %{GREEDYDATA:syslog_message}" }
						add_field => [ "received_at", "%{@timestamp}" ]
						add_field => [ "received_from", "%{host}" ]
						}
						syslog_pri { }
						date {
						match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
						}
					}
					}
					
					output {
					elasticsearch {
						hosts => ["127.0.0.1:9200"] 
						index => "syslog-demo"
					}
					stdout { codec => rubydebug }
					}


		:: estartando:

			$ brew services list

			$ brew services start nginx
			$ brew services start elasticsearch
			$ brew services start logstash
			$ brew services start kibana

			$ brew services list

			- Na guia Gerenciamento no Kibana, você deve ver um índice 'syslog-demo' 
			  recém-criado criado pelo novo pipeline do Logstash.

	:: usando:

		$ elasticsearch

		- http://locallhost:9200 			# elasticsearch
		- http://localhost:5601/status      # kibana status
		- http://localhost:5601				# kibana




# referencias
	# install elasticsearch e kibana
	http://blog.abraseucodigo.com.br/melhorando-seus-logs-com-elk.html
	https://logz.io/blog/elk-mac/