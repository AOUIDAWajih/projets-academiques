XGBoost Time Series Demand Forecasting
Overview
This repository contains a Jupyter Notebook (XGBoost_for_Time_Series_Dataset_DemandForecasting.ipynb) that demonstrates the use of the XGBoost algorithm for time series demand forecasting using the PJME hourly dataset. The notebook performs data preprocessing, model training, prediction, and evaluation, including visualization of actual vs. predicted values and error analysis.
Dataset
The dataset used is PJME_hourly.csv, which contains hourly energy consumption data (in megawatts, MW) for the PJME region. The data is indexed by datetime and includes a single target variable, PJME_MW.
Requirements
To run the notebook, ensure you have the following Python libraries installed:

pandas
numpy
matplotlib
seaborn
xgboost
scikit-learn

You can install these dependencies using pip:
pip install pandas numpy matplotlib seaborn xgboost scikit-learn

Additionally, the notebook references a utils module, which is assumed to contain helper functions for data processing or feature engineering. Ensure this module is available in the working directory or modify the notebook to remove or replace this dependency.
Notebook Structure

Imports and Setup:

Imports necessary libraries for data manipulation, visualization, and modeling.
Configures Matplotlib settings for consistent plot styling.


Data Loading and Preprocessing:

Loads the PJME_hourly.csv dataset from the ./input/ directory.
Sets the Datetime column as the index and converts it to a datetime format.


Data Exploration:

Displays the last few rows of the dataset to verify the data structure.


Visualization:

Plots actual vs. predicted energy consumption for July 2018, comparing the PJME_MW values with model predictions.


Model Evaluation:

Calculates the Root Mean Squared Error (RMSE) on the test set to evaluate model performance.
Analyzes prediction errors by computing the absolute error between actual and predicted values.
Groups errors by date and identifies the top 10 dates with the highest average errors.



Usage

Clone the Repository:
git clone <repository-url>
cd <repository-directory>


Prepare the Dataset:

Place the PJME_hourly.csv file in the ./input/ directory.
Ensure the utils module (if required) is available or modify the notebook accordingly.


Run the Notebook:

Open the notebook in Jupyter:jupyter notebook XGBoost_for_Time_Series_Dataset_DemandForecasting.ipynb


Execute the cells sequentially to load data, train the model, generate predictions, and visualize results.


Outputs:

A plot comparing actual and predicted energy consumption for July 2018.
RMSE score for the test set.
A list of the top 10 dates with the highest prediction errors.

