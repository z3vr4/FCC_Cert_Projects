# Certification Project Requirements:
# - get csv file in three ways - (done, see input_ask() function inside main function)
#   - uploading it from local computer
#   - getting URL from user input
#   - putting the URL in the code
# - Use the Pandas library to save the .csv as a dataframe - (done, see input_ask() function inside main function)
# - Print headings and first two rows - (done, see display_options() function, DispChoice match/case case "1")
# - Store the column names as a list - (done, see show_table_indexes() function col_names variable)
# - Choose one or two columns and convert the data to Numpy arrays (see note 1)
# - Display data as a scatter plot line graph (done, see display_options, DispChoice match/case cases "2" and "3")
# - Be able to do this for diferent column combinations, and interpret the graphs (done, although "interpret the graphs" is somewhat vague, see note 2)

  # Note 1: currently, the option to analyze in depth is used on a single column at a time for convenience
  # as there would be a lot of data at the same time if it was used on two columns at the same time (which could be done)
  # However, this requirement is also met in the "Two Column Graph" option/code, as it converts the data into numpy arrays
  # in order to work with them and graph them

  # Note 2: for graph interpretation, I'll take the Simple Moving Average of the last third of values and compare it to
  # the mean of the entire column. That should be a somewhat decent interpretation without getting too complex.

# CSV URL for testing
# https://people.sc.fsu.edu/~jburkardt/data/csv/faithful.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
import io
import sys

# Main Function.
def DataGraphExplorer():
  table = None

  # File selection code module
  def input_ask():
    nonlocal table
    FileSel = input("Choose a file selection method by inputting the corresponding number.\n1 - Local file upload \n2 - URL file uploading \n3 - Use an URL manually entered in the code\n",)
    match FileSel:
      case "1":
        # upload CSV from computer
        updfile = files.upload()
        filnam = next(iter(updfile))
        table = pd.read_csv(io.BytesIO(updfile[filnam]))
      case "2":
        # upload from URL
        FileURL = input("Please enter your file's URL:\n")
        FileURL = FileURL.replace(" ","")
        table = pd.read_csv(FileURL)

      case "3":
        # manually insert URL into code
        FileURL = " This is where your file's URL should be "
        table = pd.read_csv(FileURL)
      case _:
        print("It seems you tried to enter a non recognized value. Please input either '1', '2' or '3' without quotes.")
        return input_ask()

  def show_table_indexes():
    nonlocal table
    col_names = table.columns
    print("\nYour file has the following column headers (listed by index number):")
    for index, col in enumerate(col_names):
        print(index, col)

  def display_options():
    nonlocal table
    col_names = table.columns
    DispChoice = input("\nChoose an operation to perform by inputting the corresponding number.\n1 - Print headers and first two rows.\n2 - Select a single column to analyze and graph.\n3 - Select two columns to graph\n0 - Exit program\n",)
    match DispChoice:
      case "1": # Display two rows
        print(table.head(2))
        display_options()

      case "2": # Single Column Analysis
        # Column Selection and value printing
        colIndex = int(input("Please input the index of the column you want to analyze:\n"))
        colIndexStr = col_names[colIndex]
        ColNumpy = table[colIndexStr].to_numpy()
        # Mean and Median print. This used to calculate it with written code but turns numpy has functions for that, so I'll use those and save some variables I guess.
        print("\nThe mean of the values is: ",np.mean(ColNumpy),"\nThe median of the values is: ",np.median(ColNumpy))
        # Min / Max print code
        print("The lowest value in the column is:",ColNumpy.min(),", The highest value is:",ColNumpy.max())
        # Simple Moving Average code and trend interpretation
        period = int(len(ColNumpy)/3)
        sma = np.convolve(ColNumpy, np.ones((period,))/period, mode='valid')
        print("The Simple Moving Average of the last third of data entries in the column is:",sma[-1])
        if sma[-1] > (np.mean(ColNumpy) + np.mean(ColNumpy/10)):
          print("Given a 10% Relative Threshold (margin of error), the data in this column has an upward trend")
        if sma[-1] < (np.mean(ColNumpy) + np.mean(ColNumpy/10)):
          print("Given a 10% Relative Threshold (margin of error), the data in this column has an downward trend")
        if sma[-1] > (np.mean(ColNumpy) + np.mean(ColNumpy/10)) and sma[-1] > (np.mean(ColNumpy) + np.mean(ColNumpy/10)):
          print("Given a 10% Relative Threshold (margin of error), the data has no clear trend")
        # Print Entire Column Values, sorted and unsorted.
        print_column_yn = input("Print the column values sorted and unsorted? (Might take some space)\nEnter y / n\n")
        match print_column_yn:
          case "y":
            ColMedian = np.copy(ColNumpy)
            ColMedian.sort()
            print("The chosen column has the following values:\n",ColNumpy,"\nSorted, these values are:\n",ColMedian)
          case _:
            pass
        # Graphing code
        graph_or_dots = input("Select line graph or scatter plot:\n1 - Scatter\n2 - Line\n")
        match graph_or_dots:
          case "1":
            graph_string = "ro"
          case "2":
            graph_string = ""
          case _:
            print("Unrecognized input. Will graph as a line.")
            graph_string = ""
        x = np.arange(len(ColNumpy))  # this generates an array of numbers equal to the indices of the chosen column, which will be used as the X axis on the graph. In retrospect, I could've used the "Index" column the CSV probably has.
        plt.plot(x, ColNumpy, graph_string)
        plt.xlabel("Values")
        plt.ylabel(col_names[colIndex])
        plt.show()
        return display_options()
      case "3": # Two Column Graph
        # Column X Selection
        colIndexX = int(input("Please input the index of the column you want to take as your X axis (it is recommended you use the index column for this):\n"))
        colIndexStrX = col_names[colIndexX]
        ColNumpyX = table[colIndexStrX].to_numpy()
        # Column Y Selection
        colIndexY = int(input("Please input the index of the column you want to take as your Y axis:\n"))
        colIndexStrY = col_names[colIndexY]
        ColNumpyY = table[colIndexStrY].to_numpy()
        # Graphing code
        graph_or_dots = input("Select line graph or scatter plot:\n1 - Scatter\n2 - Line\n")
        match graph_or_dots:
          case "1":
            graph_string = "ro"
          case "2":
            graph_string = ""
          case _:
            print("Unrecognized input. Will graph as a line.")
            graph_string = ""
        plt.plot(ColNumpyX, ColNumpyY, graph_string)
        plt.xlabel(col_names[colIndexX])
        plt.ylabel(col_names[colIndexY])
        plt.show()
        print("For a more in-depth analysis of a column, please select the 'Select a single column to analyze and graph' option of the menu")
        return display_options()
      case "0":
        exit()
        pass # in case the sys.exit() messes up.
      case _:
        print("It seems you have entered a wrong option. Please input either '1', '2' or '3' without quotes.")
        return display_options()

  input_ask()
  show_table_indexes()
  display_options()



DataGraphExplorer()
