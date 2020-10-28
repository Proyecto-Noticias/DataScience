# AlwaysUpdate ~ DataScience REST API 📰

![alt text](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/13c1f597-c78c-48cb-b063-d53188615dea/alwaysupdate.vercel.app_login_%2810%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201028%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201028T172015Z&X-Amz-Expires=86400&X-Amz-Signature=3bfe3af415897a09aef8f5ce74657160b5936dba0d0f06836a04df226a4cda2d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22alwaysupdate.vercel.app_login_%2810%29.png%22)

EasyNews is an e-NewsPaper from Argentina, Colombia, Venezuela and Mexico, that update its news every day.

# Getting started 🚀
## Things that you need to have installed in your system: 🛠️
 * Python 3.7
 * pip
 * virtualenv
 * MySQL
 * Docker (If you want)
 
## Configuration 🔧
### Virtual enviroment
```bash
virtualenv venv --python=python.3.7
source venv/bin/activate
```
### Dependencies installation
```bash
pip install -r requirements.txt
```

### Command to run on dev mode 💻
```bash
uvicorn app.main:app --reload 
```

### Docker
```bash
docker build -t datascience_api .
docker run --rm -p 8080:8080 -e PORT=8080 datascience_api
```

## API 🌈
[HERE](https://dsapi-maa3kukuyq-ue.a.run.app/docs) you will have fully documentation of every endpoint of the api.


## Contributing ✒️
Pull requests are welcome!. And if you have an idea for a feature and dont have time to do this, feel free to open a issue!


## License 📄
[MIT](https://choosealicense.com/licenses/mit/)


