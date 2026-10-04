# 🍔 Food Delivery Price Inflation Analysis

An end-to-end data analytics project that analyzes the difference between dine-in food prices and food delivery app prices across restaurants, cities, cuisines, and delivery platforms.

The project includes data cleaning, exploratory data analysis, visualization, Power BI dashboarding, and an interactive Streamlit web application.

---

## 🌐 Live Demo

🚀 **Live Streamlit Dashboard:**  
https://food-delivery-price-inflation.streamlit.app/

---

## 📌 Project Overview

Food delivery platforms often charge customers more than the original dine-in price of the same food item.

This project analyzes:

- Dine-in vs. app prices
- Price inflation on food delivery platforms
- Platform-wise price differences
- City-wise price inflation
- Cuisine-wise price trends
- Discounts shown to customers
- Actual discount impact
- Restaurants/items with significant price inflation

The goal is to identify pricing patterns and provide useful business insights for restaurants, customers, and food delivery platforms.

---

## 🎯 Objectives

1. Clean and prepare the raw food delivery dataset.
2. Calculate price inflation between dine-in and app prices.
3. Perform exploratory data analysis.
4. Identify platform-wise and city-wise inflation patterns.
5. Analyze discounts and their relationship with inflation.
6. Build visual dashboards.
7. Create an interactive Streamlit web application.
8. Generate actionable business recommendations.

---

## 📂 Project Structure

```text
Food_Delivery_Price_Inflation/
│
├── app.py
├── requirements.txt
│
├── .streamlit/
│   └── config.toml
│
├── Task1/
│   ├── data_cleaning.py
│   ├── food_delivery_price_inflation_raw.csv
│   ├── food_delivery_price_inflation_cleaned.csv
│   ├── data_dictionary.md
│   └── README.md
│
├── Task2/
│   ├── task_2_eda.py
│   ├── task_2_insights.txt
│   ├── platform_wise_inflation.png
│   ├── city_wise_inflation.png
│   └── README.md
│
├── Task3/
│   ├── task_3_dashboard.pbix
│   ├── task_3_insights.txt
│   └── README.md
│
├── Task4/
│
└── Task5/
