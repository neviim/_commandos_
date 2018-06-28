# 
zabbix_get=\
    {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "output": "extend",
            "host": "fac034378n1.fcn.edu.br"
            "search": {
                "key_": "vfs.fs.size"
            },
            "sortfield": "name"
        },
        "auth": authToken.get("result"),
        "id": authToken.get("id")
    }