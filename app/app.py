import streamlit as st
import joblib
from prediction import *
import plotly.express as px
water_feature_importance = pd.read_csv(
    "../models/water_feature_importance.csv"
)
dataset = pd.read_csv(
    "../data/processed/smart_irrigation_cleaned.csv"
)


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Smart Irrigation System",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.hero-box{
    background: linear-gradient(135deg,#16a34a,#065f46);
    padding:35px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-bottom:25px;
}

.hero-title{
    font-size:42px;
    font-weight:800;
}

.hero-subtitle{
    font-size:18px;
    color:#d1fae5;
}

.stat-card{
    background:#111827;
    border-radius:15px;
    padding:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.08);
}

.stat-icon{
    font-size:35px;
}

.stat-value{
    font-size:28px;
    font-weight:bold;
    color:#22c55e;
}

.stat-label{
    color:#cbd5e1;
    font-size:15px;
}

.feature-card{
    background:#111827;
    padding:20px;
    border-radius:12px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
    min-height:240px;
}

.feature-title{
    color:white;
    font-size:18px;
    font-weight:bold;
}

.feature-text{
    color:#94a3b8;
    font-size:14px;
}

label {
    color: white !important;
    font-weight: 600 !important;
}

.stSelectbox label,
.stNumberInput label,
.stSlider label {
    color: white !important;
    font-size: 15px !important;
    font-weight: bold !important;
}

h1,h2,h3,h4,h5,h6,p {
    color: white !important;
}

.footer-container{
    background: linear-gradient(135deg,#0f172a,#1e293b);
    padding:20px;
    border-radius:12px;
    text-align:center;
    margin-top:30px;
    border:1px solid rgba(255,255,255,0.1);
}

.feature-title{
    color:white;
    font-size:20px;
    font-weight:bold;
    margin-bottom:10px;
}

.feature-text{
    color:#cbd5e1;
    font-size:15px;
    line-height:1.6;
}

.footer-tech{
    color:#94a3b8;
    font-size:13px;
}

.footer-version{
    color:#64748b;
    font-size:12px;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown(
"""


"""
)

page = st.sidebar.title("🌱 Smart Irrigation")

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"

if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.page = "🏠 Home"

if st.sidebar.button("💧 Irrigation Prediction", use_container_width=True):
    st.session_state.page = "💧 Irrigation Prediction"

if st.sidebar.button("🚰 Water Quantity Prediction", use_container_width=True):
    st.session_state.page = "🚰 Water Quantity Prediction"

if st.sidebar.button("🌾 Yield Prediction", use_container_width=True):
    st.session_state.page = "🌾 Yield Prediction"

if st.sidebar.button("📊 Insights Dashboard", use_container_width=True):
    st.session_state.page = "📊 Insights Dashboard"

if st.sidebar.button("💡 Smart Recommendations", use_container_width=True):
    st.session_state.page = "💡 Smart Recommendations"

page = st.session_state.page


st.sidebar.markdown("---")

st.sidebar.success("✅ Machine Learning Powered")

st.sidebar.info("""
### 📌 Modules

💧 Irrigation Prediction

🚰 Water Quantity Prediction

🌾 Yield Prediction

📊 Insights Dashboard

💡 Smart Recommendations
""")

# ==========================================
# HOME PAGE
# ==========================================
if page == "🏠 Home":

    
    st.markdown(
    """
# 🌱 Smart Irrigation System

### AI Powered Agriculture Decision Support Platform

Improve Water Efficiency • Predict Crop Yield • Optimize Irrigation
"""
)

    # KPI Cards
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">💧</div>
            <div class="stat-value">40%</div>
            <div class="stat-label">Water Saving</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">🌾</div>
            <div class="stat-value">92%</div>
            <div class="stat-label">Yield Accuracy</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">🚰</div>
            <div class="stat-value">RF</div>
            <div class="stat-label">Irrigation Model</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-icon">🤖</div>
            <div class="stat-value">3</div>
            <div class="stat-label">ML Models</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📊 Project Workflow")

    st.markdown("""
    ✅ Enter Crop & Weather Information

    ✅ Run Machine Learning Predictions

    ✅ Analyze Dashboard Insights

    ✅ Receive Smart Recommendations

    ✅ Improve Water Management & Crop Productivity
    """)

    st.markdown("---")

    st.subheader("🤖 Machine Learning Models Used")

    model1, model2, model3 = st.columns(3)

    with model1:
        st.success(
            """
            Irrigation Prediction

            Random Forest Classifier
            """
        )

    with model2:
        st.success(
            """
            Water Quantity Prediction

            Random Forest Regressor
            """
        )

    with model3:
        st.success(
            """
            Yield Prediction

            XGBoost Regressor
            """
        )

    st.markdown("---")

    st.info(
        "👈 Use the sidebar to navigate through prediction modules and smart recommendations."
    )

# if page == "🏠 Home":

#     st.markdown(
#         """
#         <h1 style='text-align:center;color:#22c55e;'>
#         🌱 Smart Irrigation System
#         </h1>
#         <h4 style='text-align:center;color:#94a3b8;'>
#         AI Powered Agriculture Decision Support Platform
#         </h4>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown("---")

#     st.markdown(
#         """
#         ### 📌 Project Overview

#         Smart Irrigation System uses Machine Learning algorithms
#         to help farmers optimize irrigation scheduling,
#         predict water requirements, and estimate crop yield.

#         The platform improves water efficiency,
#         reduces resource wastage, and supports
#         data-driven farming decisions.
#         """
#     )

#     st.markdown("---")

#     st.subheader("🚀 Key Features")

#     col1, col2 = st.columns(2)

#     with col1:

#         st.success(
#             "💧 Predict Irrigation Requirements"
#         )

#         st.success(
#             "🚰 Estimate Water Quantity Required"
#         )

#         st.success(
#             "🌾 Forecast Crop Yield"
#         )

#     with col2:

#         st.success(
#             "📊 Interactive Insights Dashboard"
#         )

#         st.success(
#             "💡 Smart Farming Recommendations"
#         )

#         st.success(
#             "🌍 Improve Water Efficiency"
#         )

#     st.markdown("---")

#     st.subheader("🤖 Machine Learning Models")

#     model1, model2, model3 = st.columns(3)

#     with model1:
#         st.info(
#             """
#             💧 Irrigation Prediction

#             Model:
#             Random Forest Classifier
#             """
#         )

#     with model2:
#         st.info(
#             """
#             🚰 Water Quantity Prediction

#             Model:
#             Random Forest Regressor
#             """
#         )

#     with model3:
#         st.info(
#             """
#             🌾 Yield Prediction

#             Model:
#             XGBoost Regressor
#             """
#         )

#     st.markdown("---")

#     st.subheader("📈 Project Workflow")

#     st.markdown(
#         """
#         1️⃣ Enter Crop & Environmental Parameters

#         2️⃣ Run Machine Learning Predictions

#         3️⃣ Analyze Dashboard Insights

#         4️⃣ Get Smart Farming Recommendations

#         5️⃣ Optimize Water & Crop Management
#         """
#     )

#     st.markdown("---")

#     st.subheader("🎯 Benefits")

#     benefit1, benefit2, benefit3 = st.columns(3)

#     with benefit1:
#         st.metric(
#             "Water Saving",
#             "30-40%"
#         )

#     with benefit2:
#         st.metric(
#             "Decision Accuracy",
#             "90%+"
#         )

#     with benefit3:
#         st.metric(
#             "Crop Productivity",
#             "Higher Yield"
#         )

#     st.markdown("---")

#     st.success(
#         "✅ Use the sidebar to start predictions and explore insights."
#     )

# ==========================================
# IRRIGATION PAGE
# ==========================================


elif page == "💧 Irrigation Prediction":

    st.title("💧 Irrigation Prediction")

    st.markdown("### Enter Crop & Weather Details")

    col1, col2 = st.columns(2)

    # ================= LEFT COLUMN =================
   
    
    with col1:

        growth_stage = st.selectbox(
            "🌱 Growth Stage",
            ["Seedling", "Vegetative", "Flowering", "Maturity"],
            key="growth_stage"
        )

        crop_type = st.selectbox(
            "🌾 Crop Type",
            ["Maize", "Rice", "Sugarcane", "Wheat"],
            key="crop_type_irrigation"
        )

        region = st.selectbox(
            "🗺️ Region",
            ["North", "South", "West"],
            key="region_irrigation"
        )

        soil_type = st.selectbox(
            "🌱 Soil Type",
            ["Loamy", "Sandy", "Silty"],
            key="soil_type"
        )

        irrigation_type = st.selectbox(
            "🚿 Irrigation Type",
            ["Flood", "Sprinkler"],
            key="irrigation_type_irrigation"
        )

        temperature = st.number_input(
            "🌡️ Temperature",
            value=25.0
        )

        humidity = st.number_input(
            "💧 Humidity",
            value=60.0
        )

    # ================= RIGHT COLUMN =================
  
    
    with col2:

        rainfall = st.number_input(
            "☔ Rainfall",
            value=100.0
        )

        forecast_rainfall = st.number_input(
            "🌦️ Forecast Rainfall",
            value=50.0
        )

        soil_moisture = st.number_input(
            "🌱 Soil Moisture",
            value=40.0
        )

        nitrogen = st.number_input(
            "🧪 Nitrogen",
            value=50.0
        )

        phosphorus = st.number_input(
            "🧪 Phosphorus",
            value=50.0
        )

        potassium = st.number_input(
            "🧪 Potassium",
            value=50.0
        )

        # crop_water_stress_level = st.slider(
        #     "⚠️ Water Stress Level",
        #     0.0,
        #     1.0,
        #     0.5
        # )


encoder = joblib.load(
    "../models/growth_stage_encoder.pkl"
)

# ================= PREDICTION BUTTON =================

#if st.button("🚀 Predict Irrigation"):
if page == "💧 Irrigation Prediction" and st.button("🚀 Predict Irrigation", key="predict_irrigation"):

        growth_stage_encoded = encoder.transform(
            [growth_stage]
        )[0]

        input_data = {
            "growth_stage": growth_stage_encoded,
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall,
            "forecast_rainfall": forecast_rainfall,
            "soil_moisture": soil_moisture,
            "nitrogen": nitrogen,
            "phosphorus": phosphorus,
            "potassium": potassium,
            #"crop_water_stress_level": crop_water_stress_level,

            # Default Values
            "wind_speed": 10,
            "solar_radiation": 300,
            "pressure": 1013,
            "cloud_cover": 30,
            "dew_point": 15,
            "soil_temperature": 25,
            "soil_ph": 6.5,
            "organic_matter": 2,
            "ec": 1,
            "leaf_wetness": 20,
            "evapotranspiration": 2,
            "ndvi": 0.5,
            "crop_age_days": 60,
            "water_usage": 100,
            "pest_risk": 0.3,
            "disease_risk": 0.2,
            "crop_health_index": 0.7,
            "previous_yield": 5,
            "groundwater_level": 50,
            "reservoir_level": 60,
            "fertilizer_usage": 30,
            "labor_hours": 8,

            "crop_type_Maize": 1 if crop_type == "Maize" else 0,
            "crop_type_Rice": 1 if crop_type == "Rice" else 0,
            "crop_type_Sugarcane": 1 if crop_type == "Sugarcane" else 0,
            "crop_type_Wheat": 1 if crop_type == "Wheat" else 0,

            "region_North": 1 if region == "North" else 0,
            "region_South": 1 if region == "South" else 0,
            "region_West": 1 if region == "West" else 0,

            "soil_type_Loamy": 1 if soil_type == "Loamy" else 0,
            "soil_type_Sandy": 1 if soil_type == "Sandy" else 0,
            "soil_type_Silty": 1 if soil_type == "Silty" else 0,

            "irrigation_type_Flood": 1 if irrigation_type == "Flood" else 0,
            "irrigation_type_Sprinkler": 1 if irrigation_type == "Sprinkler" else 0
        }

        result = predict_irrigation(input_data)
        
        st.session_state["irrigation_result"] = result

        st.session_state["irrigation_soil_moisture"] = soil_moisture

        st.session_state["irrigation_temperature"] = temperature

        st.session_state["irrigation_rainfall"] = rainfall

        st.session_state["irrigation_forecast_rainfall"] = forecast_rainfall

        # Ensure ndvi is defined: take from input_data if present, otherwise use a safe default
        ndvi_value = input_data.get("ndvi", 0.5)
        st.session_state["irrigation_ndvi"] = ndvi_value

        if result == "Irrigation Required":
            st.success("💧 Irrigation Required")
        else:
            st.error("🌱 No Irrigation Required")
        

# ==========================================
# WATER PAGE
# ==========================================

elif page == "🚰 Water Quantity Prediction":
        st.title("🚰 Water Quantity Prediction")
        water_defaults = get_water_defaults()

        st.markdown("### Enter Crop & Wether Details")

        col1, col2 = st.columns(2)

        with col1:

            growth_stage = st.selectbox(
                "🌱 Growth Stage",
                ["Seedling", "Vegetative", "Flowering", "Maturity"],
                key="water_growth"
            )

            crop_type = st.selectbox(
                "🌾 Crop Type",
                ["Maize", "Rice", "Sugarcane", "Wheat"],
                key="water_crop"
            )

            evapotranspiration = st.number_input(
                "💨 Evapotranspiration",
                min_value=0.0,
                max_value=15.0,
                value=5.0,
                step=0.1
            )

            temperature = st.number_input(
                "🌡️ Temperature (°C)",
                min_value=0.0,
                max_value=60.0,
                value=25.0
            )

            rainfall = st.number_input(
                "☔ Rainfall (mm)",
                min_value=0.0,
                value=100.0
            )
            disease_risk = st.slider(
                "🦠 Disease Risk",
                min_value=0,
                max_value=100,
                value=int(yield_defaults["disease_risk"])
            )

        with col2:

            forecast_rainfall = st.number_input(
                "🌦️ Forecast Rainfall (mm)",
                min_value=0.0,
                value=50.0
            )

            soil_moisture = st.number_input(
                "🌱 Soil Moisture (%)",
                min_value=0.0,
                max_value=100.0,
                value=40.0
            )

            # evapotranspiration = st.number_input(
            #     "💦 Evapotranspiration",
            #     min_value=0.0,
            #     value=2.0
            # )
            humidity = st.number_input(
                "💧 Humidity",
                value=float(yield_defaults["humidity"])
            )
            
            pest_risk = st.slider(
                "🐛 Pest Risk",
                min_value=0,
                max_value=100,
                value=int(yield_defaults["pest_risk"])
            )
            crop_water_stress_level = st.selectbox(
                "💧 Crop Water Stress Level",
                ["Low", "Medium", "High"]
            )
            
            ndvi = st.number_input(
                "🌾 NDVI",
                min_value=0.0,
                max_value=1.0,      # allow up to 1.0
                value=0.5,
                step=0.001,         # allow increments of 0.001
                format="%.3f"       # display three decimal places
            )

            
            
encoder = joblib.load(
    "../models/growth_stage_encoder.pkl"
)


    
            
# ================= PREDICTION BUTTON =================

#if st.button("🚰 Predict Water Quantity"):
if page == "🚰 Water Quantity Prediction" and st.button("🚰 Predict Water Quantity", key="predict_water"):

    # map growth stage to numeric
   
    growth_stage_encoded = encoder.transform(
            [growth_stage]
        )[0]
    
    encoder_stress = joblib.load(
            "../models/crop_water_stress_level.pkl")
    crop_stress_text = crop_water_stress_level
    crop_water_stress_level = crop_stress_encoder.transform([crop_water_stress_level])

    

    input_data = {

        # User Inputs
        "growth_stage": growth_stage_encoded,
        "temperature": temperature,
        "humidity": humidity,
        "rainfall": rainfall,
        "soil_moisture": soil_moisture,
        "forecast_rainfall": forecast_rainfall,
        "ndvi" : ndvi,
        "disease_risk": disease_risk,
        "pest_risk": pest_risk,
        "crop_water_stress_level" : crop_water_stress_level,
        "evapotranspiration" : evapotranspiration,
        

        # Default Values
        "wind_speed": water_defaults["wind_speed"],
        "solar_radiation": water_defaults["solar_radiation"],
        "pressure": water_defaults["pressure"],
        "cloud_cover": water_defaults["cloud_cover"],
        "dew_point": water_defaults["dew_point"],

        "soil_temperature": water_defaults["soil_temperature"],
        "soil_ph": water_defaults["soil_ph"],
        "organic_matter": water_defaults["organic_matter"],
        "ec": water_defaults["ec"],

        "leaf_wetness": water_defaults["leaf_wetness"],
        #"evapotranspiration": water_defaults["evapotranspiration"],

        #"ndvi": water_defaults["ndvi"],
        "crop_age_days": water_defaults["crop_age_days"],
        "nitrogen": water_defaults["nitrogen"],
        "phosphorus": water_defaults["phosphorus"],
        "potassium" : water_defaults["potassium"],

        # "water_usage": 100,
        "crop_health_index": water_defaults["crop_health_index"],

        "previous_yield": water_defaults["previous_yield"],
        "groundwater_level": water_defaults["groundwater_level"],
        "reservoir_level": water_defaults["reservoir_level"],

        "fertilizer_usage": water_defaults["fertilizer_usage"],
        "labor_hours": water_defaults["labor_hours"],

        # One-Hot Encoded Crop Type
        "crop_type_Maize": 1 if crop_type == "Maize" else 0,
        "crop_type_Rice": 1 if crop_type == "Rice" else 0,
        "crop_type_Sugarcane": 1 if crop_type == "Sugarcane" else 0,
        "crop_type_Wheat": 1 if crop_type == "Wheat" else 0,

        # Fixed Region
        "region_North": 1,
        "region_South": 0,
        "region_West": 0,

        # Fixed Soil Type
        "soil_type_Loamy": 1,
        "soil_type_Sandy": 0,
        "soil_type_Silty": 0,

        # Fixed Irrigation Type
        "irrigation_type_Flood": 1,
        "irrigation_type_Sprinkler": 0
    }
      



    result = predict_water_quantity(input_data)

    # Save values for Smart Recommendations page
    st.session_state["water_result"] = result
    st.session_state["disease_risk"] = disease_risk
    st.session_state["pest_risk"] = pest_risk
    st.session_state["ndvi"] = ndvi

    # If crop_water_stress_level is encoded, save the original text value
    st.session_state["crop_water_stress_level"] = crop_stress_text

    st.success(
        f"💧 Water Required: {result:.2f} Liters"
    )
    # result = predict_water_quantity(input_data)

    # st.success(
    #     f"💧 Water Required: {result:.2f} Liters"
    
            
# ==========================================
# YIELD PAGE
# ==========================================   
elif page == "🌾 Yield Prediction":
    st.title("🌾 Yield Prediction")
    yield_defaults = get_yield_defaults()

    col1, col2 = st.columns(2)

    with col1:
        growth_stage = st.selectbox(
            "🌱 Growth Stage",
            ["Seedling", "Vegetative", "Flowering", "Maturity"]
        )
        crop_type = st.selectbox(
            "🌾 Crop Type",
            ["Maize","Rice","Sugarcane","Wheat"],
            key="yield_crop"
        )

        temperature = st.number_input(
            "🌡️ Temperature",
            value=25.0
        )

        humidity = st.number_input(
            "💧 Humidity",
            value=float(yield_defaults["humidity"])
        )

        rainfall = st.number_input(
            "☔ Rainfall",
            value=100.0
        )

        soil_moisture = st.number_input(
            "🌱 Soil Moisture",
            value=40.0
        )

        nitrogen = st.number_input(
            "🧪 Nitrogen",
            value=50.0
        )

        phosphorus = st.number_input(
            "🧪 Phosphorus",
            value=40.0
        )

    with col2:

        potassium = st.number_input(
            "🧪 Potassium",
            value=45.0
        )

        crop_health_index = st.number_input(
            "❤️ Crop Health Index",
            value=float(yield_defaults["crop_health_index"])
        )
        
        previous_yield = st.number_input(
            "🌾 Previous Yield",
            value=float(yield_defaults["previous_yield"])
        )

        organic_matter = st.number_input(
            "🌿 Organic Matter",
            value=float(yield_defaults["organic_matter"])
        )

        ndvi = st.number_input(
                "🌾 NDVI",
                min_value=0.0,
                max_value=1.0,      # allow up to 1.0
                value=0.5,
                step=0.001,         # allow increments of 0.001
                format="%.3f"       # display three decimal places
        )
        pest_risk = st.slider(
            "🐛 Pest Risk",
            min_value=0,
            max_value=100,
            value=int(yield_defaults["pest_risk"])
        )
        
        disease_risk = st.slider(
            "🦠 Disease Risk",
            min_value=0,
            max_value=100,
            value=int(yield_defaults["disease_risk"])
        ) 

    # ================= PREDICTION BUTTON =================
    # st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    # col_left, col_center, col_right = st.columns([2.4, 2.0, 0.8])
    # with col_center:
    if st.button("🌾 Predict Yield"):
            encoder = joblib.load(
                "../models/growth_stage_encoder.pkl"
            )

            growth_stage_encoded = encoder.transform(
                [growth_stage]
            )[0]

            input_data = {

                "growth_stage": growth_stage_encoded,
                "temperature": temperature,
                "humidity": humidity,
                "rainfall": rainfall,
                "soil_moisture": soil_moisture,

                "nitrogen": nitrogen,
                "phosphorus": phosphorus,
                "potassium": potassium,

                "crop_health_index": crop_health_index,
                "disease_risk": disease_risk,
                "pest_risk": pest_risk,

                "previous_yield": previous_yield,
                "organic_matter": organic_matter,
                "ndvi": ndvi,
                
                # "water_quantity_required_liters": water_quantity_required_liters,
                # "crop_water_stress_level": crop_water_stress_level,

                # Default values
                "forecast_rainfall": 50,
                "wind_speed": yield_defaults["wind_speed"],
                "solar_radiation": yield_defaults["solar_radiation"],
                "pressure": yield_defaults["pressure"],
                "cloud_cover": yield_defaults["cloud_cover"],
                "dew_point": yield_defaults["dew_point"],
                "soil_temperature": yield_defaults["soil_temperature"],
                "soil_ph": yield_defaults["soil_ph"],
                "ec": yield_defaults["ec"],
                "leaf_wetness": yield_defaults["leaf_wetness"],
                "water_usage": yield_defaults["water_usage"],
                "groundwater_level": yield_defaults["groundwater_level"],
                "reservoir_level": yield_defaults["reservoir_level"],
                "fertilizer_usage": yield_defaults["fertilizer_usage"],
                "labor_hours": yield_defaults["labor_hours"],

                "crop_type_Maize": 1 if crop_type=="Maize" else 0,
                "crop_type_Rice": 1 if crop_type=="Rice" else 0,
                "crop_type_Sugarcane": 1 if crop_type=="Sugarcane" else 0,
                "crop_type_Wheat": 1 if crop_type=="Wheat" else 0,

                "region_North": 1,
                "region_South": 0,
                "region_West": 0,

                "soil_type_Loamy": 1,
                "soil_type_Sandy": 0,
                "soil_type_Silty": 0,

                "irrigation_type_Flood": 1,
                "irrigation_type_Sprinkler": 0
            }

            result = predict_yield(input_data)
            
            st.session_state["yield_result"] = result

            st.session_state["yield_ndvi"] = ndvi

            st.session_state["yield_disease_risk"] = disease_risk

            st.session_state["yield_pest_risk"] = pest_risk

            st.session_state["yield_organic_matter"] = organic_matter

            st.session_state["yield_previous_yield"] = previous_yield

            st.success(
                f"🌾 Predicted Yield: {result:.2f}"
            )
            
# ==========================================
#  INSIGHT DASHBOARD"
# ==========================================
elif page == "📊 Insights Dashboard":

    st.title("📊 Insights Dashboard")

    # ===============================
    # WATER REQUIREMENT DRIVERS
    # ===============================

    st.subheader("💧 Water Requirement Drivers")

    st.info("""
    Water requirement is primarily influenced by:

    • Soil Moisture
    • Temperature
    • Rainfall
    • Evapotranspiration
    • Crop Water Stress Level

    Lower soil moisture generally increases water requirement.
    """)
    st.subheader(
    "📊 Top Water Requirement Factors"
        )

    st.bar_chart(
    water_feature_importance
        .head(10)
        .set_index("Feature")
)
    st.subheader(
    "💧 Soil Moisture vs Water Requirement"
)

    chart_df = dataset[
        [
            "soil_moisture",
            "water_quantity_required_liters"
        ]
    ]

    st.scatter_chart(
        chart_df,
        x="soil_moisture",
        y="water_quantity_required_liters"
    )
    st.success(
    """
    Insight:

    As soil moisture decreases,
    water requirement increases.
    """
)   
    st.subheader(
        "🌾 NDVI vs Yield"
    )

    dataset["Health"] = dataset["ndvi"].apply(
        lambda x:
        "Healthy" if x >= 0.7
        else "Moderate" if x >= 0.4
        else "Poor"
    )

    fig = px.scatter(
        dataset,
        x="ndvi",
        y="yield_prediction",
        color="Health"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.success(
    """
    Higher NDVI generally indicates
    healthier vegetation and higher yield.
    """
)
    st.subheader(
    "🦠 Disease Risk Distribution"
)
    st.bar_chart(
    dataset["disease_risk"]
        .value_counts()
        .sort_index()
)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Yield",
            f"{dataset['yield_prediction'].mean():.2f}"
        )

    with col2:
        st.metric(
            "Average Water Required",
            f"{dataset['water_quantity_required_liters'].mean():.2f}"
        )

    with col3:
        st.metric(
            "Average NDVI",
            f"{dataset['ndvi'].mean():.2f}"
        )

    st.subheader(
        "📌 Executive Summary"
    )

    st.success(
        f"""
        • Average Yield:
        {dataset['yield_prediction'].mean():.2f}

        • Average Water Requirement:
        {dataset['water_quantity_required_liters'].mean():.2f} L

        • Average NDVI:
        {dataset['ndvi'].mean():.2f}

        • Soil Moisture is the most important factor
        affecting water requirement.

        • NDVI is highly correlated with crop yield.

        • Rainfall and forecast rainfall strongly
        influence irrigation decisions.
        """
    )

# ==========================================
#  SMART RECOMMENDATIONS"
# ==========================================
elif page == "💡 Smart Recommendations":


    st.title("💡 Smart Farming Recommendations")
    irrigation_result = st.session_state.get("irrigation_result")
    water_result = st.session_state.get("water_result")
    yield_result = st.session_state.get("yield_result")
    disease_risk = st.session_state.get("disease_risk")
    pest_risk = st.session_state.get("pest_risk")
    ndvi = st.session_state.get("ndvi")
    crop_water_stress_level = st.session_state.get(
        "crop_water_stress_level"
    )

    if water_result is None:

        st.warning(
            "⚠️ Please run Water Quantity Prediction first."
        )

    else:

        # ===============================
        # TOP SUMMARY CARDS
        # ===============================

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="💧 Water Required",
                value=f"{water_result:.2f} L"
            )

        with col2:
            if yield_result is not None:
                st.metric(
                    label="🌾 Predicted Yield",
                    value=f"{yield_result:.2f}"
                )

        with col3:
            st.metric(
                label="🦠 Disease Risk",
                value=f"{disease_risk}%"
            )

        with col4:
            st.metric(
                label="🐛 Pest Risk",
                value=f"{pest_risk}%"
            )

        st.divider()
        
        st.subheader(
            "🚰 Irrigation Recommendation"
        )

        if irrigation_result == "Irrigation Required":

            st.error(
                "Irrigation is required immediately."
            )

        else:

            st.success(
                "No irrigation required currently."
            )

        st.divider()

        # ===============================
        # WATER RECOMMENDATION
        # ===============================

        with st.container():

            st.subheader("💧 Water Recommendation")

            if water_result < 20:

                st.success(
                    f"Low irrigation requirement ({water_result:.2f} Liters)"
                )

            elif water_result < 50:

                st.info(
                    f"Apply approximately {water_result:.2f} Liters of water."
                )

            else:

                st.warning(
                    f"High irrigation requirement ({water_result:.2f} Liters)."
                )

        st.divider()

        # ===============================
        # CROP STRESS
        # ===============================

        with st.container():

            st.subheader("🌱 Crop Water Stress")

            if crop_water_stress_level == "Low":

                st.success(
                    "Crop water stress is LOW."
                )

            elif crop_water_stress_level == "Medium":

                st.warning(
                    "Crop water stress is MEDIUM."
                )

            elif crop_water_stress_level == "High":

                st.error(
                    "Crop water stress is HIGH."
                )

            else:

                st.info(
                    f"Stress Level: {crop_water_stress_level}"
                )

        st.divider()

        # ===============================
        # DISEASE & PEST
        # ===============================

        left, right = st.columns(2)

        with left:

            st.subheader("🦠 Disease Analysis")

            if disease_risk < 30:

                st.success(
                    "Low disease risk."
                )

            elif disease_risk < 70:

                st.warning(
                    "Moderate disease risk. Monitor crop regularly."
                )

            else:

                st.error(
                    "High disease risk detected."
                )

        with right:

            st.subheader("🐛 Pest Analysis")

            if pest_risk < 30:

                st.success(
                    "Low pest risk."
                )

            elif pest_risk < 70:

                st.warning(
                    "Moderate pest risk."
                )

            else:

                st.error(
                    "High pest risk detected."
                )

        st.divider()

        # ===============================
        # NDVI ANALYSIS
        # ===============================

        st.subheader("📈 NDVI Analysis")

        if ndvi >= 0.7:

            st.success(
                f"Healthy vegetation (NDVI = {ndvi:.2f})"
            )

        elif ndvi >= 0.4:

            st.warning(
                f"Moderate vegetation health (NDVI = {ndvi:.2f})"
            )

        else:

            st.error(
                f"Poor vegetation health (NDVI = {ndvi:.2f})"
            )

        st.divider()
        # ===============================
        # YIELD RECOMMENDATION
        # ===============================

        st.subheader("🌾 Yield Recommendation")

        if yield_result is not None:

            if yield_result >= 8:

                st.success(
                    f"Excellent expected yield ({yield_result:.2f} Ton/Ha)."
                )

            elif yield_result >= 5:

                st.warning(
                    f"Moderate expected yield ({yield_result:.2f} Ton/Ha)."
                )

            else:

                st.error(
                    f"Low expected yield ({yield_result:.2f} Ton/Ha)."
                )

        else:

            st.info(
                "Please run Yield Prediction first."
            )

    st.divider()
    # ===============================
    # FINAL ADVICE
    # ===============================

    st.subheader("🎯 Final Recommendation")

    recommendations = []

    if irrigation_result == "Irrigation Required":
        recommendations.append(
            "🚰 Irrigation is recommended immediately."
        )

    # 
    if water_result is not None:

        if water_result > 50:

            recommendations.append(
                f"💧 Apply approximately {water_result:.2f} liters of water."
        )

    if disease_risk >= 70:
        recommendations.append(
            "🦠 High disease risk detected. Inspect crop and apply preventive treatment."
        )

    if pest_risk >= 70:
        recommendations.append(
            "🐛 High pest risk detected. Consider pest control measures."
        )

    if ndvi < 0.4:
        recommendations.append(
            "📈 NDVI is low. Crop health requires attention."
        )

    # if yield_result is not None and yield_result < 5:
    #     recommendations.append(
    #         "🌾 Expected yield is low. Improve nutrient and water management."
    #     )
    if yield_result is not None:

        if yield_result < 5:

            recommendations.append(
                "🌾 Expected yield is low."
        )

    if len(recommendations) == 0:
        st.success(
            "✅ Crop conditions appear healthy. Continue current management practices."
        )

    else:
        for rec in recommendations:
            st.info(rec)







# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""
<div class="footer-container">

<div class="footer-title">
🌱 Smart Agriculture Intelligence System
</div>

<div class="footer-text">
AI-Powered Crop Yield Prediction, Irrigation Management &
Water Requirement Forecasting
</div>

<div class="footer-tech">
🚰 Water Requirement Prediction |
💧 Irrigation Recommendation |
🌾 Yield Prediction |
📊 Smart Farming Insights
</div>

<div class="footer-tech">
Built using Streamlit, Scikit-Learn, Random Forest, XGBoost,
Pandas, NumPy and Machine Learning
</div>

<div class="footer-version">
© 2026 Smart Agriculture Project | Developed by Sourabh Patil
</div>

</div>
""", unsafe_allow_html=True)