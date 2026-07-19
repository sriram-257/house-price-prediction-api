import joblib
import pandas as pd

# Load model only once when the application starts
model = joblib.load("house_price_xgboost.pkl")


def predict_house_price(data):

    # Validate input
    if data["AveOccup"] == 0:
        raise ValueError("AveOccup cannot be zero.")

    if data["AveRooms"] == 0:
        raise ValueError("AveRooms cannot be zero.")

    # Feature engineering
    rooms_per_household = data["AveRooms"] / data["AveOccup"]
    bedrooms_per_room = data["AveBedrms"] / data["AveRooms"]
    population_per_household = data["Population"] / data["AveOccup"]

    # Create DataFrame with the same feature order used during training
    input_data = pd.DataFrame([{
        "MedInc": data["MedInc"],
        "HouseAge": data["HouseAge"],
        "AveRooms": data["AveRooms"],
        "AveBedrms": data["AveBedrms"],
        "Population": data["Population"],
        "AveOccup": data["AveOccup"],
        "Latitude": data["Latitude"],
        "Longitude": data["Longitude"],
        "RoomsPerHousehold": rooms_per_household,
        "BedroomsPerRoom": bedrooms_per_room,
        "PopulationPerHousehold": population_per_household
    }])

    prediction = model.predict(input_data)

    return float(prediction[0])