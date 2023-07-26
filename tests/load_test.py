from locust import HttpUser, TaskSet, task, between, tag

"""
Run locus with:
locust -f ./tests/load_test.py
"""

data_example_0 = [3000.00, 3000.00, 1.0, 0.0, 1.0,
                  "free", "buy_it_now", "active", "", "ARS",
                  True, False, False, False, False, False, True]

class NewOrUsedPredict(TaskSet):
    @tag('Predictions')
    @task
    def predict(self):
        request_body = {"data": [data_example_0]}
        self.client.post('/v9/new_or_used/predict', json=request_body)

    @tag('Baseline')
    @task
    def health_check(self):
        self.client.get('/')


class NewOrUsedLoadTest(HttpUser):
    tasks = [NewOrUsedPredict]
    host = 'http://127.0.0.1'
    stop_timeout = 200
    wait_time = between(1, 5)
