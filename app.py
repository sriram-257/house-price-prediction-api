from fastapi import FastAPI
from schemas import HouseData
from predict import predict_house_price
from fastapi import HTTPException

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to House Price Prediction API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: HouseData):

    try:
        prediction = predict_house_price(data.model_dump())

        return {
            "success": True,
            "prediction": {
                "house_price": round(prediction, 4),
                "unit": "$100,000"
            }
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )