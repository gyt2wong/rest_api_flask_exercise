# CONTRIBUTING

## How to activate venv

```
.venv\Scripts\activate.bat
```

## How to build docker image

```
docker build -t rest-api-flask-exercise .
```

## How to run the Dockerfile locally

```
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api

docker run -dp 5005:5000 -w /app -v "$(pwd):/app" rest-api-flask-exercise sh -c "flask run --host 0.0.0.0"
```
