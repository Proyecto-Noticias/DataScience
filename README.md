# AlwaysUpdate ~ DataScience REST API 📰

![Always Update](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/13c1f597-c78c-48cb-b063-d53188615dea/alwaysupdate.vercel.app_login_%2810%29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201114T005339Z&X-Amz-Expires=86400&X-Amz-Signature=2a6ff7e25c657c4926240fbbf4bb4272f0b0303dff5e916d71ab829cfebd4279&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22alwaysupdate.vercel.app_login_%2810%29.png%22)

AlwaysUpdate is an e-NewsPaper from Argentina, Colombia, Venezuela and Mexico, that update its news every day.

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

## Demo

[![Alt text for your video](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/473ce9d0-9aa9-4f36-8807-07d561fe329b/video.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201104T163553Z&X-Amz-Expires=86400&X-Amz-Signature=5686e73ea4d4bec8167d27584b9060564d7093e45eaea4bfd9940c3a3e51ff84&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22video.png%22)](https://www.youtube.com/watch?v=kDm-sx_sU5o)

## Contributing ✒️
Pull requests are welcome!. And if you have an idea for a feature and dont have time to do this, feel free to open a issue!


## License 📄
[MIT](https://choosealicense.com/licenses/mit/)


