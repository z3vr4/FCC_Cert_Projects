# "Display a "wall" with random height and location. Player has to move sliders to adjust a parabolic path to clear the wall"
# Code meant to be run on Google Colab
%matplotlib inline
from ipywidgets import interactive
import numpy as np
import math
import matplotlib.pyplot as plt
import random as rd

wallvals = [rd.randint(5,12),rd.randint(5,12)]
# Define the graphing function
def f(a,b,c):
    xvar = 20
    points = 10*(40)
    x = np.linspace(0,xvar,points)

    plt.axis([0,xvar,0,xvar]) # window size
    plt.plot([0,xvar],[0,0],'b') # x axis
    plt.plot([0,0],[0,xvar], 'b') # y axis

    # plot wall
    plt.plot([wallvals[0],wallvals[0]],[wallvals[1],0],"b")
    x = np.linspace(-10, 10, 1000)

    # parabola function
    y1 = a*x**2 + b*x + c
    plt.plot(x, y1)

    # Determine projectile landing
    d = b**2 - 4*a*c
    if d>=0:
        root_2 = (-b - math.sqrt(d))/(2*a)
        plt.plot([root_2],[0], 'ro')

    # Set the equation as the title
    h1 = str(a) + "x**2 + " + str(b) + "x + " + str(c)
    plt.title(h1)

    plt.show()

# Set up the sliders
interactive_plot = interactive(f,a=(-6,-0.1),b=(1,35), c=(-9,9))
interactive_plot
