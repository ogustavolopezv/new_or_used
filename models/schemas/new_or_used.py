from pydantic import BaseModel, conlist
from typing import List, Any


class NewOrUsed(BaseModel):
    data: List[conlist(float, min_items=4, max_items=4)]


class NewOrUsedPredictionResponse(BaseModel):
    prediction: List[Any]
