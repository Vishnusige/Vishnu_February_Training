# Assignment 4: Supervised Learning - Housing Price Prediction

## Project Overview
This project implements three supervised learning regression models to predict median house values using the California Housing dataset.

## Directory Structure
- `dataset/`: Contains the `california_housing_test.csv` file.
- `notebook/`: Contains the `ml_models.ipynb` implementation.
- `venv/`: Isolated virtual environment (excluded via .gitignore).

## Implementation Details
1. **Data Preprocessing**: Handled missing values, removed duplicates, and treated outliers using the IQR method.
2. **Feature Engineering**: Dropped irrelevant coordinate data and applied `StandardScaler`.
3. **Models Trained**: Linear Regression, Decision Tree, and Random Forest Regressor.
4. **Evaluation**: Evaluated using Mean Absolute Error (MAE) and R-squared ($R^2$).

## Results
The **Random Forest Regressor** provided the highest accuracy, demonstrating its strength in capturing complex patterns in the housing data.