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
