import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"], marker="o", color="blue", label="Data")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])

    # Create second line of best fit
    years = np.linspace(data["Year"].min(), 2050, 100)
    predicted_sea_level = slope * years + intercept
    plt.plot(years, predicted_sea_level, color="red", label="Line of Best Fit (Entire Dataset)")
    data_after_2000 = data[data["Year"] >= 2000]
    slope_after_2000, intercept_after_2000, _, _, _ = linregress(data_after_2000["Year"], data_after_2000["CSIRO Adjusted Sea Level"])
    predicted_sea_level_after_2000 = slope_after_2000 * years + intercept_after_2000
    plt.plot(years, predicted_sea_level_after_2000, color="green", label="Line of Best Fit (Since 2000)")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()