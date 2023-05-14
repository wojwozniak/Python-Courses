# FCC Course: Scientific Computing with Python
# Project: Sea Level Predictor
# Author: Wojciech Woźniak
# Finished 14/05/2023


# Imports
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


# Main function
def draw_plot():

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',
                     float_precision='legacy', dtype='float64')

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope, intercept, c, d, e = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"])

    x_extended = np.arange(1880, 2050)

    plt.plot(x_extended, intercept + slope*x_extended, "r")
    # Create second line of best fit
    df_cut = df.loc[(df["Year"] >= 2000)]

    slope2, intercept2, c, d, e = linregress(
        df_cut["Year"], df_cut["CSIRO Adjusted Sea Level"])

    plt.plot(x_extended, intercept2 + slope2*x_extended, "r")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
