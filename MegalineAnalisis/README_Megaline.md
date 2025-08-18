# 📞 Megaline Plans Analysis

## 📌 Description
This project analyzes customer behavior and revenue in **Megaline**, a telecom operator offering two prepaid plans: **Surf** and **Ultimate**.  
The goal is to determine which plan is more profitable by exploring user activity, calculating revenue, and testing statistical hypotheses.

---

## 🎯 Objective
- Explore and clean user activity data (calls, messages, internet usage).  
- Calculate **monthly revenue** per customer for each plan.  
- Compare average revenue between the **Surf** and **Ultimate** plans.  
- Perform **hypothesis testing** to evaluate whether one plan generates significantly more revenue than the other.  
- Provide **recommendations** for the company’s commercial strategy.  

---

## 🛠️ Development & Tools
The analysis was developed in **Python** using **Jupyter Notebook**.  

**Libraries used**:
- **pandas** → data cleaning and manipulation  
- **numpy** → numerical calculations  
- **matplotlib** → data visualization  
- **scipy.stats** → hypothesis testing  

**Main steps**:
1. **Data Preprocessing**: handled missing values, converted data types, and aggregated usage per month.  
2. **Feature Engineering**: computed monthly revenue considering plan fees and overage charges.  
3. **Exploratory Data Analysis (EDA)**: explored distributions of calls, internet usage, and messages.  
4. **Revenue Analysis**: calculated mean and variance of monthly revenue for both plans.  
5. **Hypothesis Testing**: used **t-tests** to compare average revenues across plans and regions.  

---

## 📈 Key Insights
- **Surf** users tend to exceed plan limits, generating more overage charges, making it often **more profitable** despite a lower fixed fee.  
- **Ultimate** users usually stay within plan limits, leading to stable but lower additional revenue.  
- Statistical tests showed significant differences in average revenue between Surf and Ultimate.  
- No statistically significant difference was found in revenue across different regions.  

---

## 📂 Repository Structure
```
MegalineAnalisys.ipynb   # Main analysis notebook
README.md                # Project documentation
/datasets/               # Datasets used (not included here)
```

---

## 🚀 Next Steps
- Extend the analysis to include **customer segmentation** based on behavior.  
- Apply **predictive modeling** to classify new customers into the most profitable plan.  
- Build interactive **dashboards** (e.g., with Streamlit or Power BI) for real-time monitoring of plan performance.  
