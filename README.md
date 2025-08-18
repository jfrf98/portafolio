# 📊 Video Game Sales Analysis (2016 Dataset)

## 📌 Description
This project analyzes a historical dataset of video game sales up to 2016, including information such as platform, genre, user and critic scores, ESRB ratings, and global sales by region.  
The goal is to identify patterns and key characteristics that can help **predict the commercial success of video games** and guide **marketing strategies for 2017**.

---

## 🎯 Objective
- Clean and prepare the dataset for analysis.  
- Explore sales trends by **year, platform, and genre**.  
- Perform **statistical hypothesis testing** to validate insights.  
- Evaluate correlations between **critic/user scores and sales**.  
- Visualize data to support decision-making and highlight business opportunities.  

---

## 🛠️ Development & Tools
The analysis was developed in **Python**, using **Jupyter Notebook**.  

**Libraries used**:
- **pandas** → data manipulation and cleaning  
- **numpy** → numerical operations  
- **scipy.stats** → hypothesis testing and statistical analysis  
- **matplotlib** → data visualization  

**Main steps**:
1. **Data Cleaning**: handling missing values, correcting data types, removing duplicates.  
2. **Feature Engineering**: creating a `total_sales` column by summing regional sales.  
3. **Exploratory Data Analysis (EDA)**: trends in sales over time, by platform and by genre.  
4. **Visualization**: bar charts, boxplots, and scatterplots to show key patterns.  
5. **Hypothesis Testing**: statistical validation of differences in user vs. critic scores across platforms.  

---

## 📈 Key Insights
- Peak of global sales occurred in **2008**, driven by platforms such as **PS2, Wii, and Xbox 360**.  
- Top 5 genres in terms of sales: **Action, Sports, Shooter, Role-Playing, and Racing**.  
- **North America** consistently shows the highest sales across platforms and genres.  
- Correlations between **scores and sales** are weak, suggesting that reviews alone don’t determine commercial success.  

---

## 📂 Repository Structure
```
Proyecto-Sprint6.py   # Main analysis script
README.md             # Project documentation
/datasets/games.csv   # Dataset used (not included here)
```

---

## 🚀 Next Steps
- Train predictive models (classification/regression) to forecast sales success.  
- Expand analysis with more recent datasets.  
- Automate report generation with interactive dashboards (Streamlit).  
