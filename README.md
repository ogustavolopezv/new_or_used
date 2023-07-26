# new-or-used-ml-deploy
Code repository for Take-Home exercise of Machine Learning classification model deployment with FastAPI and Docker to provide availability of predictions on new or used products for MercadoLibre.

- Original problem description and requirements can be found in [DS_MLE_TakeHome_NewOrUsed_202307.ipynb](.\DS_MLE_TakeHome_NewOrUsed_202307.ipynb).
- The EDA and insights obtained therein, as well as the Machine Learning Modeling can be found in [EDA&Modeling.ipynb](.\eda\EDA&Modeling.ipynb). Also, an auxiliary profile report of the dataset is documented in [ml_new_or_used_profile_report.html](.\eda\ml_new_or_used_profile_report.html).

- The productive approach of the solution is implemented as a REST API (supported by FastAPI) and containerized for modularity and ease of demostration (supported by Docker). The repository tree is as follows:

* [eda/](.\eda)
  * [EDA&Modeling.ipynb](.\eda\EDA&Modeling.ipynb)
  * [MLA_100k.jsonlines](.\eda\MLA_100k.jsonlines)
  * [ml_new_or_used_profile_report.html](.\eda\ml_new_or_used_profile_report.html)
* [machine_learning/](.\machine_learning)
  * [models/](.\machine_learning\models)
    * [new_or_used_v1.joblib](.\machine_learning\models\new_or_used_v1.joblib)
    * [new_or_used_v10.joblib](.\machine_learning\models\new_or_used_v10.joblib)
    * [new_or_used_v2.joblib](.\machine_learning\models\new_or_used_v2.joblib)
    * [new_or_used_v3.joblib](.\machine_learning\models\new_or_used_v3.joblib)
    * [new_or_used_v4.joblib](.\machine_learning\models\new_or_used_v4.joblib)
    * [new_or_used_v5.joblib](.\machine_learning\models\new_or_used_v5.joblib)
    * [new_or_used_v6.joblib](.\machine_learning\models\new_or_used_v6.joblib)
    * [new_or_used_v7.joblib](.\machine_learning\models\new_or_used_v7.joblib)
    * [new_or_used_v8.joblib](.\machine_learning\models\new_or_used_v8.joblib)
    * [new_or_used_v9.joblib](.\machine_learning\models\new_or_used_v9.joblib)
  * [schemas/](.\machine_learning\schemas)
    * [new_or_used_v1.py](.\machine_learning\schemas\new_or_used_v1.py)
    * [new_or_used_v9.py](.\machine_learning\schemas\new_or_used_v9.py)
  * [classifier.py](.\machine_learning\classifier.py)
  * [loader.py](.\machine_learning\loader.py)
  * [trainer.py](.\machine_learning\trainer.py)
* [routes/](.\routes)
  * [v1/](.\routes\v1)
    * [new_or_used_predict.py](.\routes\v1\new_or_used_predict.py)
  * [v9/](.\routes\v9)
    * [new_or_used_predict.py](.\routes\v9\new_or_used_predict.py)
  * [home.py](.\routes\home.py)
* [tests/](.\tests)
  * [load_test.py](.\tests\load_test.py)
  * [test_response_v9.py](.\tests\test_response_v9.py)
* [.coveragerc](.\.coveragerc)
* [.gitignore](.\.gitignore)
* [app.py](.\app.py)
* [deploy.sh](.\deploy.sh)
* [Dockerfile](.\Dockerfile)
* [DS_MLE_TakeHome_NewOrUsed_202307.ipynb](.\DS_MLE_TakeHome_NewOrUsed_202307.ipynb)
* [LICENSE](.\LICENSE)
* [README.md](.\README.md)
* [requirements.txt](.\requirements.txt)

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
curl -X 'POST' \
  'http://localhost:84/v9/new_or_used/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": {
    "listing_type_id": "free",
    "base_price": 60.0,
    "price": 60.0,
    "initial_quantity": 1,
    "sold_quantity": 0,
    "available_quantity": 1
  }
}'
```
