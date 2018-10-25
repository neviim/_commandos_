# https://www.arangodb.com/download-major/centos/


ArangoDB 3 (https://www.arangodb.com)
  The multi-model NoSQL database: distributed free and open-source database
  with a flexible data model for documents, graphs, and key-values. Build
  high performance applications using a convenient SQL-like query language
  or JavaScript extensions.

First Steps with ArangoDB:
  https://docs.arangodb.com/latest/Manual/GettingStarted/

Upgrading ArangoDB:
  https://docs.arangodb.com/Installing/Upgrading.html

Configuring the storage Engine:
  https://docs.arangodb.com/latest/Manual/Administration/Configuration/GeneralArangod.html#storage-engine

Upgrading ArangoDB database files:
  > /etc/init.d/arangodb3 upgrade

Configuration file:
  /etc/arangodb3/arangod.conf

Start ArangoDB shell client:
  > /usr/bin/arangosh

Start ArangoDB service:
  > systemctl start arangodb3.service

Enable ArangoDB service:
  > systemctl enable arangodb3.service

SECURITY HINT:
run 'arango-secure-installation' to set a root password
the current password is '3d455f66db8aa0f1ce4109c76e6d20eb'
(You should do this for a FRESH install! For an UPGRADE the password does not need to be changed)
  Verifying  : arangodb3-3.3.19-1.x86_64                                                                                                                                                             1/1

Installed:
  arangodb3.x86_64 0:3.3.19-1

Complete!


Web 127.0.0.1:8529
username: root 
password: root



Use the arangosh to create a new database and user.

arangosh> db._createDatabase("example");
arangosh> var users = require("@arangodb/users");
arangosh> users.save("root@example", "password");
arangosh> users.grantDatabase("root@example", "example");
You can now connect to the new database using the user root@example.

shell> arangosh --server.username "root@example" --server.database example







- Alertas
arango-secure-installation
2018-10-24T19:06:12Z [27122] WARNING {memory} environment variable GLIBCXX_FORCE_NEW' is not set. it is recommended to set it to some value to avoid unnecessary memory pooling in glibc++
2018-10-24T19:06:12Z [27122] WARNING {memory} execute 'export GLIBCXX_FORCE_NEW=1'
2018-10-24T19:06:12Z [27122] WARNING {memory} maximum number of memory mappings per process is 65530, which seems too low. it is recommended to set it to at least 256000
2018-10-24T19:06:12Z [27122] WARNING {memory} execute 'sudo sysctl -w "vm.max_map_count=256000"'
2018-10-24T19:06:12Z [27122] WARNING {memory} /sys/kernel/mm/transparent_hugepage/enabled is set to 'always'. It is recommended to set it to a value of 'never' or 'madvise'
2018-10-24T19:06:12Z [27122] WARNING {memory} /sys/kernel/mm/transparent_hugepage/defrag is set to 'always'. It is recommended to set it to a value of 'never' or 'madvise'
2018-10-24T19:06:12Z [27122] WARNING {memory} execute 'sudo bash -c "echo madvise > /sys/kernel/mm/transparent_hugepage/enabled"'
2018-10-24T19:06:12Z [27122] WARNING {memory} execute 'sudo bash -c "echo madvise > /sys/kernel/mm/transparent_hugepage/defrag"'