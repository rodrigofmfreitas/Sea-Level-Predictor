import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r"D:\digof\Documents\git\learning-python\boilerplate-sea-level-predictor\epa-sea-level.csv")
    #df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    linear_regression = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    xreg = pd.Series([i for i in range(1880, 2051)])
    yreg = linear_regression.slope * xreg + linear_regression.intercept
    plt.plot(xreg, yreg, "r")

    # Create second line of best fit
    newdf = df[(df["Year"] >= 2000)]
    linear_regression_the_2nd = linregress(newdf["Year"], newdf["CSIRO Adjusted Sea Level"])
    xreg2 = pd.Series([i for i in range(2000, 2051)])
    yreg2 = linear_regression_the_2nd.slope * xreg2 + linear_regression_the_2nd.intercept
    plt.plot(xreg2, yreg2, "purple")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()