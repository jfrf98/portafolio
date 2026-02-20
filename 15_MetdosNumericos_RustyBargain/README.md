# 🚗 Rusty Bargain – Used Car Price Prediction

## 📌 Project Overview

Rusty Bargain is a second-hand car marketplace developing an application that allows users to quickly estimate the market value of their vehicles.

Using historical listings, technical specifications, equipment versions, and pricing data, this project builds and compares multiple machine learning models to predict the market price of used cars.

The objective is not only to maximize predictive accuracy but also to evaluate:

- Prediction quality
- Training time
- Inference speed

---

## 🎯 Business Objective

The model must:

- Accurately estimate vehicle market value
- Provide fast predictions within the mobile application
- Maintain reasonable training time for periodic model updates

Performance is evaluated using **RMSE (Root Mean Squared Error)**.

---

## 📊 Dataset Description

**File:** `data/car_data.csv`

### Features

- **DateCrawled** — Date when the profile was downloaded  
- **VehicleType** — Vehicle body type  
- **RegistrationYear** — Registration year  
- **Gearbox** — Transmission type  
- **Power** — Horsepower (CV)  
- **Model** — Vehicle model  
- **Mileage** — Mileage (km)  
- **RegistrationMonth** — Registration month  
- **FuelType** — Fuel type  
- **Brand** — Vehicle brand  
- **NotRepaired** — Whether vehicle was repaired  
- **DateCreated** — Profile creation date  
- **NumberOfPictures** — Number of pictures  
- **PostalCode** — Owner postal code  
- **LastSeen** — Last user activity date  

### Target Variable

- **Price** — Vehicle price (EUR)

---

## 🧹 Data Preprocessing

- Removed missing or unrealistic values  
- Filtered out extreme outliers (invalid registration years, unrealistic prices)  
- Handled categorical variables appropriately  
- Compared encoding strategies depending on model type  
- Split dataset into training and testing sets  

---

## 🤖 Models Implemented

### 1️⃣ Linear Regression (Sanity Check)

- Baseline model  
- Used to validate preprocessing and feature pipeline  
- Ensures boosting models outperform a simple linear approach  

---

### 2️⃣ Decision Tree Regressor

- Hyperparameter tuning  
- Evaluated overfitting behavior  
- Compared training speed vs predictive performance  

---

### 3️⃣ Random Forest Regressor

- Hyperparameter optimization  
- Improved generalization  
- Balanced bias-variance tradeoff  

---

### 4️⃣ LightGBM (Gradient Boosting)

- Tuned parameters:
  - `n_estimators`
  - `learning_rate`
  - `max_depth`
- Evaluated computational efficiency  
- Compared against classical tree-based models  

---

### 5️⃣ (Optional) XGBoost / CatBoost

- Compared encoding strategies  
- Evaluated computational tradeoffs  
- Analyzed performance differences  

---

## 📈 Model Evaluation

Models were evaluated using:

- **RMSE (Root Mean Squared Error)**
- Training time
- Prediction time

Example timing in Jupyter:

```python
%%time
model.fit(X_train, y_train)
```
---
## 🏆 Results Summary

### Resultados – Comparación por RMSE mas bajo

| Modelo | Tiempo | RMSE Train | RMSE Test |
|--------|--------|------------|------------|
| Bosque Aleatorio (n_estimators = 100 \| depth = …) | 219.69 | 1041.61 | 1625.77 |
| Bosque Aleatorio (n_estimators = 50 \| depth = 20) | 108.98 | 1047.25 | 1629.97 |
| LightGBM (num_leaves = 60 \| learning_rate = 0.1) | 4.70 | 1585.07 | 1654.84 |
| LightGBM (num_leaves = 60 \| learning_rate = 0.05) | 5.29 | 1664.61 | 1705.09 |
| LightGBM (num_leaves = 30 \| learning_rate = 0.1) | 3.71 | 1669.72 | 1706.37 |


### Resultados – Comparación por tiempo de procesamiento mas bajo

| Modelo | Tiempo | RMSE Train | RMSE Test |
|--------|--------|------------|------------|
| LightGBM (num_leaves = 30 \| learning_rate = 0.1) | 3.71 | 1669.72 | 1706.37 |
| LightGBM (num_leaves = 30 \| learning_rate = 0.05) | 4.00 | 1749.93 | 1772.25 |
| Árbol de Decisión (max_depth = 5) | 4.16 | 2485.78 | 2491.73 |
| LightGBM (num_leaves = 60 \| learning_rate = 0.1) | 4.70 | 1585.07 | 1654.84 |
| LightGBM (num_leaves = 60 \| learning_rate = 0.05) | 5.29 | 1664.61 | 1705.09 |


LightGBM achieved the best balance between accuracy and computational efficiency.

NOTE: **RMSE (Root Mean Squared Error)** measures the average prediction error of a regression model.  
Lower RMSE indicates better accuracy.  

In this project, RMSE represents the average difference (in euros) between predicted and actual car prices.


---

## 🔎 Key Insights

- Linear Regression served as a sanity check.
- Tree-based models handled non-linear relationships better.
- Random Forest improved predictive stability.
- Gradient Boosting provided superior performance.
- Encoding strategy significantly impacted results.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 📌 Future Improvements

- Advanced hyperparameter optimization (Optuna)
- Model explainability (SHAP values)
- Feature importance analysis
- Deployment as an API
- Model monitoring and retraining strategy

---

## 💡 Project Highlights

- This project demonstrates:
- Structured model comparison
- Performance benchmarking (accuracy vs speed)
- Hyperparameter tuning
- Business-oriented evaluation
- Reproducible ML workflow
