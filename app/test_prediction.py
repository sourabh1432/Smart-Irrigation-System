from prediction import *
import joblib

import joblib


from prediction import get_water_defaults

defaults = get_water_defaults

print(defaults)


# defaults = joblib.load("../models/yield_default_values.pkl")

# print(defaults.keys())

# model = joblib.load(
#     "../models/yield_prediction_model.pkl"
# )

# print(type(model))

# water_model = joblib.load(
#     "../models/water_quantity_model.pkl"
# )

# water_features = joblib.load(
#     "../models/water_quantity_features.pkl"
    
# )

# features = joblib.load("../models/yield_prediction_features.pkl")

# print(len(features))
# print(features)

# def predict_water_quantity(input_data):

#     import pandas as pd

#     input_df = pd.DataFrame([input_data])

#     input_df = input_df.reindex(
#         columns=water_features,
#         fill_value=0
#     )

#     prediction = water_model.predict(input_df)[0]

#     return prediction


# print("Irrigation Features:")
# print(len(get_irrigation_features()))

# print("Water Features:")
# print(len(get_water_features()))

# print("Yield Features:")
# print(len(get_yield_features()))

# print(get_irrigation_features())



# features = joblib.load("../models/irrigation_features.pkl")

# print("Total Features:", len(features))

# for feature in features:
#     print(feature)
    
    
    
    
# features = joblib.load("../models/water_quantity_features.pkl")

# print(len(features))
# print(features)

