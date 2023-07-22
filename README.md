# new-or-used-ml-deploy
Code repository for Take-Home exercise of Machine Learning classification model deployment with FastAPI and Docker to provide availability of predictions on new or used products for MercadoLibre.

# Demo instructions


### 1. Build the docker image

```
docker build -t new-or-used-ml-build .
```

### 2. Run the container

```
docker run -d -p 84:80 --name new-or-used-api new-or-used-ml-build 
```

### 3. Run Pytest with coverage
```
docker exec -it new-or-used-api pytest --ignore=tests/ --cov=app tests/ --cov-config=.coveragerc
```

### 4. Go to localhost
http://127.0.0.1:84/docs


### 5. Try out the POST /predict method
```
curl -X POST "http://127.0.0.1/v1/new_or_used/predict" -H\
 "accept: application/json"\
 -H "Content-Type: application/json"\
 -d "{\"data\":[[4.8,3,1.4,0.3],[2,1,3.2,1.1]]}"
```
