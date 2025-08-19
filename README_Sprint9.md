# 📊 Sprint 9 - User Behavior Analysis

## 📌 Description
This project analyzes user behavior data to identify patterns in **music streaming consumption**.  
The dataset contains information on user activity such as day of the week, city, and number of tracks played.  
The objective is to test hypotheses about differences in user activity across **days and cities**, and generate insights that could help improve product strategy.

---

## 🎯 Objectives
- Explore and clean the dataset (handle missing values and duplicates).  
- Investigate user activity by **day of the week**.  
- Compare user activity between different **cities**.  
- Test hypotheses using statistical methods to validate whether user behavior differs significantly across groups.  
- Draw conclusions and provide actionable recommendations.  

---

## 🛠️ Development & Tools
The project was developed in **Python** using **Jupyter Notebook**.  

**Libraries used**:
- **pandas** → data manipulation and cleaning  
- **numpy** → numerical calculations  
- **matplotlib** → visualizations  
- **scipy.stats** → hypothesis testing  

**Main steps**:
1. **Data Preprocessing**: handled missing values and duplicates.  
2. **Exploratory Data Analysis (EDA)**: analyzed activity by day and city.  
3. **Hypothesis Testing**:  
   - H₀: User activity is the same across weekdays and weekends.  
   - H₁: User activity differs between weekdays and weekends.  
   - H₀: User activity does not differ across cities.  
   - H₁: User activity differs across cities.  
4. **Visualization**: created bar charts and summaries to support insights.  

---

## 📈 Key Insights
- Activity levels differ significantly between **weekdays and weekends**.  
- User behavior also shows **differences across cities**, confirming that geography influences listening patterns.  
- The analysis provides evidence to adjust **recommendations and marketing strategies** based on time and location.  

---

## 📂 Repository Structure
```
Srpint 9.ipynb         # Main analysis notebook
README.md              # Project documentation
/datasets/             # Dataset used (not included here)
```

---

## 🚀 Next Steps
- Extend the analysis to include **genre preferences** by day and city.  
- Build **predictive models** to forecast user activity.  
- Create **dashboards** (e.g., with Streamlit or Power BI) for real-time monitoring.  
