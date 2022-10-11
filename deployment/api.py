from fastapi import FastAPI
import pickle 
from pydantic import BaseModel
import pandas as pd



app = FastAPI()


with open("./model-training/model.pkl", 'rb') as f:
    MODEL =pickle.load(f)

with open("./model-training/preprocess.pkl", 'rb') as f:
    PROCESS =pickle.load(f)

class Item(BaseModel):
    distance_from_home: float
    distance_from_last_transaction: float
    ratio_to_median_purchase_price:float
    repeat_retailer:float
    used_chip:float
    used_pin_number:float
    online_order:float




@app.post("/predict")
def predict(item:Item):
    df = pd.DataFrame(pd.Series(item.dict())).transpose()
    df[["distance_from_home",
        "distance_from_last_transaction",
        "ratio_to_median_purchase_price"]] = PROCESS.transform(df[["distance_from_home",
                                                                    "distance_from_last_transaction",
                                                                    "ratio_to_median_purchase_price"]]) 

    result = MODEL.predict(df)
    return {"response": "fraud" if result[0] else "non-fraud"}

@app.get("/health")
def health():
    return {"health": "im ok"}