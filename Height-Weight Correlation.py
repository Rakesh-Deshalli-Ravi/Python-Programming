# Name: Rakesh Deshalli Ravi
# Date: 8 Nov 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: 
# Assignment 0902: Height-Weight Correlation

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a CSV file
def read_data(file_path):
    """
    Read data from a CSV file using Pandas.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.
    """
    data = pd.read_csv(file_path)
    return data

# Function to separate data for male and female subjects
def separate_data_by_sex(data):
    """
    Separate the data into male and female subjects based on the 'Sex' column.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        pd.DataFrame, pd.DataFrame: Dataframes for male and female subjects.
    """
    male_data = data[data['Sex'] == 'Male']
    female_data = data[data['Sex'] == 'Female']
    return male_data, female_data

# Function to plot (height, weight) points for male and female subjects
def plot_height_weight_points(male_data, female_data):
    """
    Plot the (height, weight) points for male and female subjects.

    Args:
        male_data (pd.DataFrame): Data for male subjects.
        female_data (pd.DataFrame): Data for female subjects.
    """
    plt.scatter(male_data['Height'], male_data['Weight'], label='Male', color='blue', alpha=0.5)
    plt.scatter(female_data['Height'], female_data['Weight'], label='Female', color='deeppink', alpha=0.5)

# Function to plot the fitted regression line
def plot_regression_line(data):
    """
    Plot the fitted regression line.

    Args:
        data (pd.DataFrame): The input data.
    """
    x_values = np.linspace(data['Height'].min(), data['Height'].max(), 100)
    y_values = 0.28 * x_values + 23.2
    plt.plot(x_values, y_values, label='Regression Line', color='green')

# Function to define and plot bounds for height and weight variables
def plot_bounds(data):
    """
    Define and plot bounds for height and weight variables.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        float, float, float, float: Lower and upper bounds for height and weight.
    """
    height_mean = data['Height'].mean()
    height_std = data['Height'].std()
    weight_mean = data['Weight'].mean()
    weight_std = data['Weight'].std()

    height_lower_bound = height_mean - 2.5 * height_std
    height_upper_bound = height_mean + 2.5 * height_std
    weight_lower_bound = weight_mean - 2.5 * weight_std
    weight_upper_bound = weight_mean + 2.5 * weight_std

    plt.axvline(height_lower_bound, color='purple', linestyle='dashed', label='Height Bound')
    plt.axvline(height_upper_bound, color='purple', linestyle='dashed')
    plt.axhline(weight_lower_bound, color='orange', linestyle='dashed', label='Weight Bound')
    plt.axhline(weight_upper_bound, color='orange', linestyle='dashed')

    return height_lower_bound, height_upper_bound, weight_lower_bound, weight_upper_bound

# Function to detect and mark outliers
def detect_and_mark_outliers(data, height_lower_bound, height_upper_bound, weight_lower_bound, weight_upper_bound):
    """
    Detect and mark outliers in the data based on the defined bounds.

    Args:
        data (pd.DataFrame): The input data.
        height_lower_bound (float): Lower bound for height.
        height_upper_bound (float): Upper bound for height.
        weight_lower_bound (float): Lower bound for weight.
        weight_upper_bound (float): Upper bound for weight.
    """
    outliers = data[
        ((data['Height'] < height_lower_bound) | (data['Height'] > height_upper_bound)) &
        ((data['Weight'] < weight_lower_bound) | (data['Weight'] > weight_upper_bound))
    ]

    for index, row in outliers.iterrows():
        plt.text(row['Height'], row['Weight'], 'Outlier', fontsize=10, color='Black')

# Function to label axes and add a legend
def label_axes_and_legend():
    """
    Label the axes and add a legend to the plot.
    """
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.title('Correlation between Height and Weight')
    plt.legend()
    plt.grid(True)

# Main function to create the plot
if __name__ == "__main__":
    # Step 1: Read the data using Pandas
    data = read_data("Heights_and_Weights.csv")

    # Step 2: Separate data by sex
    male_data, female_data = separate_data_by_sex(data)

    # Step 3: Plot (height, weight) points
    plt.figure(figsize=(10, 6))
    plot_height_weight_points(male_data, female_data)

    # Step 4: Plot the regression line
    plot_regression_line(data)

    # Step 5: Plot bounds for height and weight
    height_lower_bound, height_upper_bound, weight_lower_bound, weight_upper_bound = plot_bounds(data)

    # Step 6: Detect and mark outliers
    detect_and_mark_outliers(data, height_lower_bound, height_upper_bound, weight_lower_bound, weight_upper_bound)

    # Step 7: Label axes and add a legend
    label_axes_and_legend()

    # Step 8: Show the plot
    plt.show()


