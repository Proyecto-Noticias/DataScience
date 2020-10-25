# AlwaysUpdate ~ DataScience REST API 📰


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


