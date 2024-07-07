# Second Hand Car Price Prediction Using Machine Learning

Welcome to the Second Hand Car Price Prediction project! This project aims to predict the prices of used cars using various machine learning algorithms. By analyzing different features of the cars, the model can provide accurate price predictions, which can be useful for buyers, sellers, and dealers.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Data Preprocessing](#data-preprocessing)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)


## Project Overview

In this project, we explore various machine learning techniques to predict the prices of second-hand cars. The goal is to build a model that can accurately estimate the value of a used car based on its features such as age, mileage, brand, model, etc.

## Dataset

The dataset used for this project contains various features of second-hand cars, including:

- **V id**
- **On Road Old Price (in rupees)**
- **On Road Now Price (in rupees)**
- **Years**
- **Kilometers Driven**
- **Rating (1 to 5)**
- **Condition (1 to 10)**
- **Economy (km/l)**
- **Top Speed (km/h)**
- **Horsepower (hp)**
- **Torque (Nm)**
- **Current price**

## Features

- **Exploratory Data Analysis (EDA)**: Understand the data distribution and identify patterns.
- **Data Preprocessing**: Handle missing values, encode categorical variables, and scale numerical features.
- **Feature Engineering**: Create new features or modify existing ones to improve model performance.
- **Model Selection**: Compare different machine learning algorithms such as Linear Regression, Decision Trees, Random Forest, and more.
- **Hyperparameter Tuning**: Optimize model parameters for better performance.
- **Model Evaluation**: Assess the model using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.

## Data Preprocessing

Data preprocessing steps include:

- Handling missing values
- Encoding categorical variables
- Scaling numerical features
- Splitting the data into training and testing sets

## Modeling

The following machine learning models were implemented and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## Evaluation

Models were evaluated using the following metrics:

- Mean Absolute Error (RMSE)
- Mean Squared Error (MSE)
- r2 Score

## Results

The best-performing model was the **Linear Regression**, which provided the most accurate price predictions based on the evaluation metrics.


## Usage

To use the model to predict car prices, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Abul-Khair/SECOND-HAND-CAR-PRICE-PREDICTION-USING-MACHINE-LEARNING.git
   ```

2. Navigate to the project directory:
   ```bash
   cd SECOND-HAND-CAR-PRICE-PREDICTION-USING-MACHINE-LEARNING
   ```

3. Run the Jupyter Notebook or Python script to train the model and make predictions.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.
