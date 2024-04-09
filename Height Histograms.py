# Name: Rakesh Deshalli Ravi
# Date: 8 Nov 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link: https://youtu.be/eLnrqRme2CI
# Assignment 0901: Height Histograms

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetch_and_segment_data():
    """
    This function is responsible for importing the dataset from a CSV and categorizing it based on gender.
    
    Returns:
    - data_males: Data subset for males.
    - data_females: Data subset for females.
    """
    # Import dataset
    dataset = pd.read_csv("Heights_and_Weights.csv")
    
    # Split dataset by gender
    data_males = dataset[dataset['Sex'] == 'Male']
    data_females = dataset[dataset['Sex'] == 'Female']
    
    return data_males, data_females

def compute_stats(data_males, data_females):
    """
    Computes statistical measures such as average and most frequent values for heights.
    
    Parameters:
    - data_males: Data subset for males.
    - data_females: Data subset for females.
    
    Returns:
    - Dictionary of computed statistics.
    """
    # Calculate averages
    avg_height_male = np.mean(data_males['Height'])
    avg_height_female = np.mean(data_females['Height'])

    # Determine histograms' range
    range_hist = (min(data_males['Height'].min(), data_females['Height'].min()), max(data_males['Height'].max(), data_females['Height'].max()))
    bins_count = 20

    # Generate histograms for height data
    hist_males, edges_males = np.histogram(data_males['Height'], bins=bins_count, range=range_hist, density=True)
    hist_females, edges_females = np.histogram(data_females['Height'], bins=bins_count, range=range_hist, density=True)

    # Estimate the mode from the histograms
    mode_height_male = edges_males[np.argmax(hist_males)]
    mode_height_female = edges_females[np.argmax(hist_females)]
    
    return {
        'avg_height_male': avg_height_male,
        'avg_height_female': avg_height_female,
        'mode_height_male': mode_height_male,
        'mode_height_female': mode_height_female
    }


def display_height_distributions(data_males, data_females, computed_stats):
    """
    Generates histogram visualizations for the distributions of male and female heights.
    
    Parameters:
    - data_males: Data subset for males.
    - data_females: Data subset for females.
    - computed_stats: Statistics dictionary.
    """
    # Establish the histogram's boundaries
    boundary_low = min(data_males['Height'].min(), data_females['Height'].min())
    boundary_high = max(data_males['Height'].max(), data_females['Height'].max())
    hist_range = (boundary_low, boundary_high)
    
    bin_specification = 20

    plt.figure(figsize=(10, 5))

    # Male height distribution
    plt.hist(data_males['Height'], bins=bin_specification, range=hist_range, density=True, color='skyblue', alpha=0.8, label='Heights of Males')
    # Female height distribution
    plt.hist(data_females['Height'], bins=bin_specification, range=hist_range, density=True, color='orange', alpha=0.6, label='Heights of Females')

    # Add lines for the statistical measures
    plt.axvline(computed_stats['avg_height_male'], color='navy', linestyle='--', linewidth=2, label=f'Average Male Height: {computed_stats["avg_height_male"]:.2f} cm')
    plt.axvline(computed_stats['avg_height_female'], color='red', linestyle='--', linewidth=2, label=f'Average Female Height: {computed_stats["avg_height_female"]:.2f} cm')
    plt.axvline(computed_stats['mode_height_male'], color='navy', linestyle=':', linewidth=2, label=f'Mode of Male Height: {computed_stats["mode_height_male"]:.2f} cm')
    plt.axvline(computed_stats['mode_height_female'], color='red', linestyle=':', linewidth=2, label=f'Mode of Female Height: {computed_stats["mode_height_female"]:.2f} cm')

    # Customize the plot
    plt.title('Comparison of Height Distributions')
    plt.xlabel('Height in centimeters')
    plt.ylabel('Desnity')

    plt.legend(loc='best')
    plt.show()

def hist_area_calculation(complete_data):
    """
    Computes the integral of the height distribution histogram.

    Parameters:
    - complete_data: Combined dataset.

    Returns:
    - Total area under the histogram.
    """
    # Determine histogram data
    height_counts, bin_dividers = np.histogram(complete_data['Height'], bins=20, density=True)

    # Calculate the widths of histogram bins
    bin_width = np.diff(bin_dividers)

    # Compute the total area
    total_area = np.sum(height_counts * bin_width)
    
    return total_area


if __name__ == "__main__":
    # Obtain and sort the data
    data_males, data_females = fetch_and_segment_data()
    
    # Compute the required statistics
    computed_stats = compute_stats(data_males, data_females)

    # Combine male and female data, then calculate the histogram area
    complete_data = pd.concat([data_males, data_females])
    histogram_area = hist_area_calculation(complete_data)
    print(f"The integrated area of the histogram for the dataset is: {histogram_area}")
    
    # Generate and display histograms
    display_height_distributions(data_males, data_females, computed_stats)


