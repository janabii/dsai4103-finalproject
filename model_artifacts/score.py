
import pandas as pd
import numpy as np
import joblib

preprocessor = joblib.load("model_artifacts/preprocessor.joblib")
model = joblib.load("model_artifacts/manual_lightgbm_model.joblib")
feature_cols = joblib.load("model_artifacts/feature_columns.joblib")

def score_new_data(input_data):
    input_df = pd.DataFrame(input_data)
    input_df = input_df[feature_cols]
    
    input_processed = preprocessor.transform(input_df)
    pred_log = model.predict(input_processed)
    pred_price = np.expm1(pred_log)
    
    output_df = input_df.copy()
    output_df["predicted_history_price"] = pred_price
    
    return output_df

if __name__ == "__main__":
    sample_data = [
        {
            "outcode": "SW2",
            "latitude": 51.45,
            "longitude": -0.12,
            "bathrooms": 1.0,
            "bedrooms": 2.0,
            "floorAreaSqM": 75.0,
            "livingRooms": 1.0,
            "tenure": "Leasehold",
            "propertyType": "Flat/Maisonette",
            "currentEnergyRating": "C",
            "rentEstimate_currentPrice": 2200.0,
            "saleEstimate_currentPrice": 450000.0,
            "saleEstimate_confidenceLevel": "HIGH"
        }
    ]
    
    predictions = score_new_data(sample_data)
    print(predictions)
