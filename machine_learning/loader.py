
import pandas as pd
import numpy as np
import json
from joblib import load
import classifier as clf

def new_or_used_dataset():
    new_or_used_dataset_pd = None
    new_or_used_dataset_pd = pd.DataFrame([json.loads(x) for x in open("MLA_100k.jsonlines")])
    return new_or_used_dataset_pd

def new_or_used_featured_dataset(new_or_used_dataset):
    new_or_used_dataset_featured_pd = None
    new_or_used_dataset_featured_pd = new_or_used_dataset
    
    # Transform sub_status as string
    new_or_used_dataset_featured_pd['sub_status_2']  = [''.join(map(str, l)) for l in new_or_used_dataset_featured_pd['sub_status']]
    # Categoricals to booleans.
    new_or_used_dataset_featured_pd['has_warranty'] = np.where(new_or_used_dataset_featured_pd['warranty'].isnull(), False, True)
    new_or_used_dataset_featured_pd['has_parent_item'] = np.where(new_or_used_dataset_featured_pd['parent_item_id'].isnull(), False, True)
    new_or_used_dataset_featured_pd['has_official_store'] = np.where(new_or_used_dataset_featured_pd['official_store_id'].isnull(), False, True)
    new_or_used_dataset_featured_pd['has_video'] = np.where(new_or_used_dataset_featured_pd['video_id'].isnull(), False, True)
    new_or_used_dataset_featured_pd['has_variations'] = np.where(new_or_used_dataset_featured_pd['variations'].size == 0, False, True)
    return new_or_used_dataset_featured_pd

def load_and_predict():
  data_example_1 =  {
        "listing_type_id": "free",
        "base_price": 0,
        "price": 0,
        "initial_quantity": 0,
        "sold_quantity": 0,
        "available_quantity": 0
      }

  data_example_2 = {
    "data": 
      {
        "listing_type_id": "free",
        "base_price": 0,
        "price": 0,
        "initial_quantity": 0,
        "sold_quantity": 0,
        "available_quantity": 0
      }
  }    

  clf.model = load('models/new_or_used_v9.joblib')
  # data = dict(data_example_2)['data']
  print("RRRRRRRRRRRRRRRRrrrr")
  print(data_example_2)
  data = dict(data_example_2)['data']
  # data = pd.DataFrame(a)
  print("DATAAAAAAAAAAAAA")
  print(data)
  eu = pd.DataFrame(data, index=[0])
  print("EEUUUUUUUUU")
  print(eu)
  print(clf.model.predict(eu).tolist())
  # print(prediction)
  # pipeline = load('models/new_or_used_v9pichu.joblib')
  # print(pipeline.predict(pd.DataFrame(data_example_2)).tolist())
  # print(clf.model.predict_log_proba([[0,0,0,0],[1000,1,2,3]]).tolist())
  # print(clf.model.predict_proba([[0,0,0,0],[1000,1,2,3]]).tolist())

load_and_predict()