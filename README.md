# 🛒 Superstore Sales Analysis using Python

## 📌 Project Overview
This project demonstrates an end-to-end **Exploratory Data Analysis (EDA)** workflow on a synthetically generated Superstore sales dataset using Python. The project covers **data generation, data cleaning, and in-depth analysis** to uncover meaningful business insights.

It is designed to strengthen practical knowledge of Python-based data analytics and real-world data preprocessing techniques.

---

## 🎯 Objectives
- Generate a realistic Superstore sales dataset using Python.
- Perform data cleaning and preprocessing on raw data.
- Conduct exploratory data analysis to discover patterns and trends.
- Visualize key insights for business decision-making.
- Gain hands-on experience with Python data analysis libraries.

---

## 🧰 Tech Stack
- **Python**
- **Pandas** – data manipulation & cleaning  
- **NumPy** – numerical computing  
- **Matplotlib** – data visualization  
- **Seaborn** – statistical visualization  
- **Jupyter Notebook** – interactive environment  

---

## 📂 Dataset
The dataset is synthetically generated using Python to simulate real-world Superstore sales data.

### Key Columns:
- Order ID  
- Order Date, Ship Date  
- Category, Sub-Category  
- Region, State  
- Sales, Quantity, Discount, Profit  

The generated dataset is saved as `superstore_data.csv`.

---

## 🧹 Data Cleaning & Preprocessing
The following steps were performed to ensure data quality:

- Removed duplicate records  
- Handled missing values using imputation or removal  
- Converted date columns to datetime format  
- Corrected data types for numerical fields  
- Treated outliers in Sales and Profit  
- Standardized text values (Category, Region, State)  
- Feature engineering (Month, Year from Order Date)  

📌 This ensured reliable and accurate analysis.

---

## 🔍 Exploratory Data Analysis (EDA)

### 1️⃣ Univariate Analysis
- Distribution of Sales, Profit, Quantity  
- Frequency of Categories and Regions  
- Histograms and count plots  

### 2️⃣ Bivariate Analysis
- Sales vs Profit  
- Discount vs Profit  
- Category vs Sales  
- Scatter plots and box plots  

### 3️⃣ Time Series Analysis
- Sales trends over time  
- Monthly and yearly aggregation  
- Seasonality analysis using line charts  

### 4️⃣ Category Analysis
- Sales and profit by Category and Sub-Category  
- Top and bottom performing product segments  

### 5️⃣ Regional Analysis
- Region-wise and state-wise sales and profit  
- Contribution of each region to total revenue  

---

## 📊 Key Insights
- Technology and Office Supplies contribute significantly to total sales.
- Higher discounts generally lead to lower profit margins.
- Sales show clear trends and seasonal patterns over time.
- Certain regions consistently outperform others.
- A small number of sub-categories drive the majority of profit.

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/krish-analytics/superstore-sales-analysis.git
