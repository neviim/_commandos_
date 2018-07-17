# fazer um upgrade mongodb 2.6 para 4.x 
 
    :::

        $ yum repolist

        $ nano /etc/yum.repos.d/mongodb.repo

            [mongodb-org-4.0]
            name=MongoDB Repository
            baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/testing/x86_64/
            gpgcheck=1
            enabled=1
            gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc


        $ yum install -y deltarpm
        $ yum update -y

        $ yum install mongodb-org-server


    ::: 
        $ yum remove mangodb*
        $ yum clean all
        $ yum install mongodb-org
        $ rm -rf /var/cache/yum

        $ tail -j /var/log/mongodb/mongod.log


        $ mongoimport --db test --collection restaurants --file /tmp/primer-dataset.json