#!/bin/sh
chmod +x cloud_sql_proxy
./cloud_sql_proxy -instances=easynewsmaster:us-east1:easynews=tcp:3306 -credential_file=credentials.json &
sleep 10
uvicorn --host=0.0.0.0 --port 8080 app.main:app