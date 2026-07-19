# House Price Prediction API

A FastAPI-based machine learning API that predicts California house prices using an XGBoost model.

## Features

- FastAPI REST API
- XGBoost Machine Learning Model
- Input validation using Pydantic
- Error handling
- Interactive Swagger UI

## Project Structure

```
housepredictionapi/
│
├── app.py
├── predict.py
├── schemas.py
├── house_price_xgboost.pkl
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app:app --reload
```

## Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

## Prediction Endpoint

**POST** `/predict`

Example input:

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.984127,
  "AveBedrms": 1.02381,
  "Population": 322,
  "AveOccup": 2.555556,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

Example response:

```json
{
  "success": true,
  "prediction": {
    "house_price": 4.3658,
    "unit": "$100,000"
  }
}
```