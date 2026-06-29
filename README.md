# 🌱 Smart Irrigation System using Machine Learning

## 📌 Project Overview

The **Smart Irrigation System** is a Machine Learning-based web application that helps farmers make intelligent irrigation decisions using environmental, soil, and crop parameters.

The application predicts:

* 💧 Whether irrigation is required
* 🚰 Water quantity required (Liters)
* 🌾 Crop yield prediction
* 📊 Interactive insights dashboard
* 💡 Smart farming recommendations

The project aims to improve water efficiency, reduce water wastage, and increase agricultural productivity through data-driven decision making.

---

# 🚀 Features

✅ Irrigation Requirement Prediction

* Predicts whether irrigation is required based on current environmental conditions.

---

✅ Water Quantity Prediction

* Estimates the required water quantity in liters using soil and weather conditions.

---

✅ Yield Prediction

* Predicts expected crop yield using crop, soil, and climatic parameters.

---

✅ Smart Recommendations

Provides recommendations based on:

* Water Requirement
* Crop Water Stress
* Disease Risk
* Pest Risk
* NDVI Analysis
* Yield Prediction
* Irrigation Status

---

✅ Insights Dashboard

Interactive visualizations including:

* Feature Importance
* Soil Moisture vs Water Requirement
* Crop Distribution
* Average Water Requirement
* Average Yield
* NDVI Analysis

---

# 🧠 Machine Learning Models Used

| Prediction Task           | Algorithm Used           |
| ------------------------- | ------------------------ |
| Irrigation Required       | Random Forest Classifier |
| Water Quantity Prediction | Random Forest Regressor  |
| Yield Prediction          | Random Forest Regressor  |

Other algorithms evaluated during model selection:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

Random Forest was selected because it provided the best performance and reduced overfitting.

---

# 📂 Project Structure

```text
Smart-Irrigation-System
│
├── app
│   ├── app.py
│   ├── prediction.py
│   └── test_prediction.py
│
├── Data
│   ├── Raw
│   └── Processed
│
├── models
│   └── water_feature_importance.csv
│
├── notebooks
│   ├── EDA
│   ├── Feature Engineering
│   ├── Irrigation Model
│   ├── Water Quantity Model
│   └── Yield Prediction Model
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠 Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Matplotlib
* Plotly
* Streamlit

### Machine Learning

* Random Forest
* Decision Tree
* Logistic Regression

### Development Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

# 📊 Dataset

The dataset contains farm, crop, soil, and environmental parameters including:

* Temperature
* Humidity
* Rainfall
* Forecast Rainfall
* Soil Moisture
* Soil Temperature
* Soil pH
* Nitrogen
* Phosphorus
* Potassium
* Organic Matter
* NDVI
* Crop Health Index
* Disease Risk
* Pest Risk
* Water Quantity Required
* Yield Prediction
* Irrigation Required

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/sourabh1432/Smart-Irrigation-System.git
```

Open the project

```bash
cd Smart-Irrigation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

# 📈 Model Performance

### Irrigation Prediction

* Random Forest Classifier
* High Accuracy
* Good Precision and Recall

---

### Water Quantity Prediction

* Random Forest Regressor
* High R² Score
* Low Mean Absolute Error
* Low RMSE

---

### Yield Prediction

* Random Forest Regressor
* High Prediction Accuracy
* Good Generalization Performance

---

---

# 🔮 Future Enhancements

* Weather API Integration
* IoT Sensor Integration
* Live Soil Moisture Monitoring
* Mobile Application
* Cloud Deployment
* SMS Notifications
* Automatic Irrigation Control
* Satellite Data Integration

---

# 🎯 Project Objectives

* Improve irrigation efficiency
* Reduce water wastage
* Increase crop productivity
* Support data-driven farming
* Promote sustainable agriculture

---

# 👨‍💻 Author

**Sourabh Patil**

Machine Learning & Software Testing Enthusiast

### Skills

* Machine Learning
* Python
* Streamlit
* Random Forest
* Selenium
* Playwright
* API Testing
* SQL

GitHub:

https://github.com/sourabh1432

---

# ⭐ If you found this project useful, please consider giving it a star.
