echo killing old docker processes
docker-compose rm -fs

docker-compose up --build -d

sleep 5

curl -i http://127.0.0.1:9080/apisix/admin/routes/1 -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' -X PUT -d '
{
    "uri": "/*",
    "plugins": {
        "uri-blocker": {
            "block_rules": ["^/private(/?).*"]
        }
    },
    "upstream": {
        "type": "roundrobin",
        "nodes": {
            "backend:8000": 1
        }
    }
}'
