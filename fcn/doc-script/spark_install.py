# 

    ::: Instalando spark centOS 7


        # caso o java não esteja instalado/atualizado
        $ java -version
        java version "1.8.0_171"
        Java(TM) SE Runtime Environment (build 1.8.0_171-b11)
        Java HotSpot(TM) 64-Bit Server VM (build 25.171-b11, mixed mode)        

            # instalação opcional
            $ yum install java-1.8.0-openjdk* -y


        # precisa instalar o scala
        $ wget https://downloads.lightbend.com/scala/2.12.6/scala-2.12.6.rpm
        $ rpm -ivh scala-2.12.6.rpm
        $ scala -version
        Scala code runner version 2.12.6 -- Copyright 2002-2018, LAMP/EPFL and Lightbend, Inc.



            ::: Baixar source ".tgz" e instalar de: https://www.igniterealtime.org/downloads/

                $ cd /tmp
                $ wget http://ftp.unicamp.br/pub/apache/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
                $ tar xf spark-2.3.1-bin-hadoop2.7.tgz
                $ mkdir /usr/local/spark
                $ cp -r spark-2.3.1-bin-hadoop2.7/* /usr/local/spark


        ::: Executando spark

            $ /usr/local/spark/bin/spark-shell

                ____              __
                / __/__  ___ _____/ /__
                _\ \/ _ \/ _ `/ __/  '_/
            /___/ .__/\_,_/_/ /_/\_\   version 2.3.1
                /_/

            Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_171)
            Type in expressions to have them evaluated.
            Type :help for more information.

            scala>

            