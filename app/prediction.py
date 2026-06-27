import joblib
import pandas as pd

# ==========================================
# LOAD MODELS
# ==========================================

irrigation_model = joblib.load(
    "../models/irrigation_required_model.pkl"
)

water_model = joblib.load(
    "../models/water_quantity_required_model.pkl"
)

yield_model = joblib.load(
    "../models/yield_prediction_model.pkl"
)

# ==========================================
# LOAD FEATURE FILES
# ==========================================

irrigation_features = joblib.load(
    "../models/irrigation_features.pkl"
)

water_features = joblib.load(
    "../models/water_quantity_features.pkl"
)

yield_features = joblib.load(
    "../models/yield_prediction_features.pkl"
)

# ==========================================
# IRRIGATION PREDICTION
# ==========================================

def predict_irrigation(input_dict):

    input_df = pd.DataFrame([input_dict])

    input_df = input_df.reindex(
        columns=irrigation_features,
        fill_value=0
    )

    prediction = irrigation_model.predict(input_df)[0]

    if prediction == 1:
        return "Irrigation Required"
    else:
        return "No Irrigation Required"


# ==========================================
# WATER QUANTITY PREDICTION
# ==========================================

def predict_water_quantity(input_dict):

    input_df = pd.DataFrame([input_dict])

    input_df = input_df.reindex(
        columns=water_features,
        fill_value=0
    )

    prediction = water_model.predict(input_df)[0]

    return round(float(prediction), 2)


# ==========================================
# YIELD PREDICTION
# ==========================================

def predict_yield(input_dict):

    input_df = pd.DataFrame([input_dict])

    input_df = input_df.reindex(
        columns=yield_features,
        fill_value=0
    )

    prediction = yield_model.predict(input_df)[0]

    return round(float(prediction), 2)


# ==========================================
# GET FEATURE LISTS
# ==========================================

def get_irrigation_features():
    return irrigation_features


def get_water_features():
    return water_features


def get_yield_features():
    return yield_features

yield_defaults = joblib.load(
    "../models/yield_default_values.pkl"
)

def get_yield_defaults():
    return yield_defaults


water_defaults = joblib.load(
    "../models/water_defaults_values.pkl"
)

def get_water_defaults():
    return water_defaults


crop_stress_encoder = joblib.load(
    "../models/crop_water_stress_level.pkl"
)

importance_df = pd.DataFrame({
    "feature": water_features,
    "importance": water_model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="importance",
    ascending=False
)