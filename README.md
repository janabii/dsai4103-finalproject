# Predicting Residential Property Value Growth in London
## A Business Analytics Final Project

### DSAI4103 | Ahmed Al Janabi, 60300347 | Dr. Elyor Kodirov

## Business Problem
Accurately estimating property prices is essential for real estate agencies, investors, and buyers operating in the London housing market. Property values are influenced by a combination of factors, including location, property size, type, and historical transaction data, making accurate pricing a complex and data-intensive task.

My motivation for this project comes from a personal curiosity and interest in the real estate market. This interest developed further when I traveled to London, where I observed how active and data-driven the property market is. This experience encouraged me to explore how property prices are determined and what factors have the greatest impact on valuation.

Additionally, coming from Doha, where publicly available real estate data is relatively limited, I was particularly interested in working with a market like London where richer datasets are accessible. This provided an opportunity to explore real estate analytics in a way that is not as easily possible in my local context.

This project aims to develop a machine learning model that predicts residential property prices based on these features, while also identifying the key factors that drive property valuation. The results will support better pricing decisions and provide insights into the most influential variables affecting property prices.

## Project Objectives

The objectives of this project are:

1. Analyze the key factors influencing residential property sale prices in London.
2. Prepare, clean, and structure the dataset for predictive modeling.
3. Organize the raw data into three business-focused tables representing property characteristics, market estimates, and transaction history.
4. Engineer meaningful features from property, location, and valuation-related data.
5. Build and compare machine learning models for predicting actual sale prices.
6. Interpret model behavior using SHAP explainability techniques.
7. Evaluate model performance across different property types, tenure groups, energy ratings, and geographic areas.
8. Present the main findings through an interactive dashboard.

## Dataset Description

The dataset used in this project contains residential property records from London, including property characteristics, location details, historical transaction data, and estimated pricing information.

To better align the dataset with the project requirements and improve the business structure of the analysis, the original raw dataset was separated into three tables:


1.   Table 1: Property Profile
    This table describes what the property is, including features such as address-related information, outcode, latitude, longitude, bedrooms, bathrooms, living rooms, floor area, tenure, property type, and current energy rating.

2.   Table 2: Market Estimates
    This table represents what the market estimates the property to be worth, including current rent estimates, current sale estimates, estimate ranges, and confidence levels.

3. Table 3: Transaction History
    This table contains the actual recorded historical transaction outcome, including sale date, historical sale price, and price change information.


The dataset includes multiple types of features:



*   property characteristics: number of bedrooms, bathrooms, living rooms, and floor area
*   location information: outcode, latitude, and longitude
*   property details: property type, tenure, and energy rating
*   market estimate data: estimated current sale price, rent estimates, and estimate confidence level
*   transaction history data: historical sale price and related change values


The target variable selected for this project is:
*history_price*

This variable represents the actual recorded sale price of a property, making it the most suitable target for a regression task. Unlike estimated prices, it reflects the real transaction outcome and therefore provides a stronger basis for predictive modeling and performance evaluation.

the dataset provides a broad view of the factors that influence residential property valuation, making it suitable for building predictive models, analyzing pricing behavior, and generating business insights.
