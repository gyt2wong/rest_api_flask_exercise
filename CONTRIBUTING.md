# CONTRIBUTING

## How to activate venv

```
.venv\Scripts\activate.bat
```

## How to build docker image

```
docker build -t flask-smorest-api .
```

## How to run the Dockerfile locally

```
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api
```
