import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
  
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
  
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8,8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')
  
    # Create first line of best fit
    # calculate linregress
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # creating line of best fit, from first year to 2050
    line_fit_1 = []
    for val in np.arange(df['Year'].min(), 2051):
        y = slope * val + intercept
        line_fit_1.append(y)
    ax.plot(np.arange(df['Year'].min(),2051),line_fit_1,'r')

    # Create subdataframe to graph off of for second line of best fit
    df_2k = df[df['Year'] >= 2000]

    # Create second line of best fit
    # calculate linregress
    slope, intercept, r_value, p_value, std_err = linregress(df_2k['Year'], df_2k['CSIRO Adjusted Sea Level'])
    # creating second line of best fit, from year 2000 to 2050
    line_fit_2 = []
    for val in np.arange(df_2k['Year'].min(), 2051):
        y = slope * val + intercept
        line_fit_2.append(y)
    ax.plot(np.arange(df_2k['Year'].min(),2051),line_fit_2,'g')
  
  
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title('Rise in Sea Level')
