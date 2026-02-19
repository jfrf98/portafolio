# 🚕 Sweet Lift Taxi – Hourly Demand Forecasting

## 📌 Project Overview

Sweet Lift Taxi collected historical data on airport taxi orders.  
To optimize driver allocation during peak hours, the company needs to predict the number of taxi orders for the next hour.

The objective of this project is to build a time series forecasting model that predicts hourly taxi demand while achieving:

> **Root Mean Squared Error (RMSE) ≤ 48** on the test set.

---

## 🎯 Business Objective

Accurate short-term demand prediction enables:

- Better driver allocation during peak hours  
- Reduced passenger wait time  
- Improved operational efficiency  
- Data-driven workforce planning  

---

## 📊 Dataset Description

**File:** `/datasets/taxi.csv`  

**Target variable:**
- `num_orders` → Number of taxi orders

The dataset contains timestamped historical taxi order data.

---

## 🧠 Methodology

### 1️⃣ Data Preprocessing

- Converted timestamp to datetime format  
- Resampled data into **hourly intervals**  
- Sorted chronologically  
- Checked for missing values and temporal consistency  

```python
df['datetime'] = pd.to_datetime(df['datetime'])
df = df.set_index('datetime')
df = df.resample('1H').sum()
```

### 2️⃣ Exploratory Data Analysis (EDA)

- Time series visualization
- Rolling mean & rolling standard deviation
- Trend and seasonality inspection
- Seasonal decomposition

Key insights:

- Strong daily seasonality
- Clear demand peaks at specific hours
- Observable trend variations over time

---

### 3️⃣ Feature Engineering

Converted the time series into a supervised learning problem using:

- Lag features
- Rolling statistics
- Hour of day
- Day of week

Example:
```python
df['lag_1'] = df['num_orders'].shift(1)
df['rolling_mean_24'] = df['num_orders'].rolling(24).mean()
df['hour'] = df.index.hour
df['dayofweek'] = df.index.dayofweek
```

---

### 4️⃣ Train/Test Split

- Used the last 10% of the dataset as the test set
- Chronological split (no random shuffling to avoid data leakage)

---

### 5️⃣ Models Evaluated

Multiple regression models were trained and compared:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting

- (Optional) CatBoost / XGBoost
Time-aware validation was applied.
---
## 📈 Evaluation Metric

Root Mean Squared Error (RMSE)

Project constraint:

RMSE on test set must be ≤ 48.

---

## 🏆 Results

| Model | RMSE (Test) |
|--------|------------|
| Linear Regression | xx |
| Random Forest | xx |
| Gradient Boosting | xx |
| **Best Model (Gradient Boosting)** | **≤ 48** |

✔ Final model achieved RMSE ≤ 48.

---

### 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib 
- Scikit-learn
- Time Series Feature Engineering

---

### 📂 Project Structure
├── notebook.ipynb

├── README.md

├── datasets/

│   └── taxi.csv

---

🚀 How to Run

- Clone the repository
- Install dependencies
- Run the notebook
```python
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## 📚 Key Learnings

- Importance of chronological splitting in time series
- Avoiding data leakage
- Feature engineering for forecasting
- Evaluating multiple models under business constraints
- Understanding seasonality patterns

---

## 🔎 Future Improvements

- Implement ARIMA / SARIMA models
- Add external variables (weather, events)
- Use LSTM / deep learning approaches
- Perform advanced hyperparameter optimization

---

# 💼 Why This Project Matters

- This project demonstrates:
- Business-oriented modeling
- Time series forecasting
- Feature engineering
- Model evaluation discipline
- Performance optimization under constraints
