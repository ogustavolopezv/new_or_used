from pydantic import BaseModel, conlist
from typing import List, Any, Union, Literal
import pandas as pd

# data: List[conlist(object, min_items=6, max_items=6)]
# listing_type_id: object

class NewOrUsedv9(BaseModel):
    listing_type_id: Literal['free', 'bronze', 'silver', 'gold_special', 'gold', 'gold_premium', 'gold_pro']
    base_price: float
    price: float
    initial_quantity: int
    sold_quantity: int
    available_quantity: int

class NewOrUsed(BaseModel):
    data: NewOrUsedv9


class NewOrUsedPredictionResponse(BaseModel):
    prediction: List[Any]
    probability: List[Any]
    log_probability: List[Any]
    
def format_response_data(data):
    d = dict(data)
    data_formatted = pd.DataFrame([d], columns=d.keys())
    return data_formatted