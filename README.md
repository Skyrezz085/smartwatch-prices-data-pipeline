# **Smartwatch Features & Price Analysis ⌚📈**

An end-to-end pipeline project for analyzing smartwatch specifications and pricing trends using PostgreSQL, Apache Airflow, Elasticsearch, and Kibana.

## **Introduction 💼**

Wearable technology continues to grow, with smartwatches leading the charge thanks to features like health tracking, connectivity, and sleek designs. This project aims to analyze smartwatch data to understand the factors that influence pricing and popularity among different brands.

## **Project Objectives 🎯**

The purpose of this project is to:

- Explore key specifications that impact smartwatch pricing.
- Provide insights into brand positioning in the market.
- Guide consumers and vendors with data-backed recommendations.

## **Problem Breakdown 🔍**

1. What is the price distribution of smartwatches across different brands?
2. How do features like GPS, NFC, or heart rate monitoring influence price?
3. Which display types or sizes are most common?
4. Is there a correlation between battery life and price?
5. How do connectivity types (Bluetooth, Wi-Fi, LTE) relate to pricing?
6. Which brands dominate the mid-range or premium price segments?

## **Dataset Overview 📂**

Sourced from [Kaggle](https://www.kaggle.com/datasets/rkiattisak/smart-watch-prices), this dataset contains key attributes for analyzing pricing trends in the wearable tech market.

### **Table Overview**

| No | Column Name                 | Description                                                      |
|----|-----------------------------|------------------------------------------------------------------|
| 1  | Brand                       | Brand of the smartwatch (e.g., Apple, Samsung, Fitbit)           |
| 2  | Model                       | Model name                                                       |
| 3  | Operating System            | OS used (e.g., WatchOS, WearOS, RTOS)                            |
| 4  | Connectivity                | Connectivity options (e.g., Bluetooth, LTE, Wi-Fi)               |
| 5  | Display Type                | Type of screen (e.g., AMOLED, LCD, OLED)                         |
| 6  | Display Size (inches)       | Diagonal size of the display in inches                           |
| 7  | Resolution                  | Screen resolution (e.g., 320x320, 360x360)                        |
| 8  | Water Resistance (meters)   | Depth in meters for water resistance                             |
| 9  | Battery Life (days)         | Battery life in days                                             |
| 10 | Heart Rate Monitor          | Indicates presence of heart rate sensor                          |
| 11 | GPS                         | Indicates whether GPS is supported                               |
| 12 | NFC                         | Indicates presence of Near Field Communication (NFC)             |
| 13 | Price (USD)                 | Price of the smartwatch in US dollars                            |

## **Methodology 🔧**

1. **Initial Load to PostgreSQL**: Data is stored in a relational database for structured querying.
2. **ETL via Apache Airflow**: DAGs manage data cleaning, formatting, and transformation processes.
3. **Validation and Quality Checks**: Cleaning includes standardizing price and numerical values.
4. **Indexing in Elasticsearch**: Enables full-text search and fast aggregations.
5. **Kibana Visualization**: Dashboards display pricing distributions, feature trends, and brand insights.

## **Conclusion 📊**

- **Pricing Trends**: Brands like Apple and Garmin dominate premium pricing, while Amazfit and Xiaomi cater to budget segments.
- **Feature Influence**: Watches with GPS and NFC tend to have higher prices.
- **Battery Life**: Longer battery life is more common in fitness-focused devices.
- **Display Insights**: AMOLED displays are frequent among mid to high-end models.
- **Water Resistance**: Most models offer some level of water protection, typically 30–50 meters.

## **Recommendations 💡**

1. **Product Positioning**: Emphasize high-value specs (GPS, AMOLED, water resistance) for mid-range segments.
2. **Brand Benchmarking**: Use market data to align product pricing with competitors.
3. **Battery Optimization**: Increase battery life for value-smartwatches to compete better.
4. **Consumer Education**: Highlight feature-to-price advantages clearly in marketing.
5. **Feature Bundling**: Promote models that offer GPS + NFC as premium lifestyle choices.

## **Dependencies 📚**

- **Database**: PostgreSQL  
- **ETL Tool**: Apache Airflow  
- **Search Engine**: Elasticsearch  
- **Visualization Tool**: Kibana  

### **Libraries Used 🛠️**

- Pandas  
- GreatExpectation  
- Elasticsearch  
- Apache Airflow  

## Author 👨‍💻  
Reza Syadewo  
LinkedIn: [Reza Syadewo](https://www.linkedin.com/in/reza-syadewo-b5801421b/)