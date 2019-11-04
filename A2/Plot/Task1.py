"""Plotting a graph of plenty.data to satisfy Task 1 of Assignment 2 for TGIS"""

# load useful modules
from matplotlib import pyplot
# load my own module which loads data from file into x and y
from Load.loaddata import loadData

# Exception used to handle file not found errors, a likely possible error when reusing code for other datasets

try:
    # use the loadData function to read a data file
    x, y = loadData('../plenty.data')
except FileNotFoundError as e:
    print(e)
else:
    """Standard plot created by matplotlib"""
    # choose data to plot
    pyplot.plot(x, y)
    # add plot details
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.title('Plot of plenty.data')
    # show plot
    pyplot.show()

    """Alternative plot with some different styling"""
    # creates subplots and fills under the x, y line with transparent green
    fig, ax = pyplot.subplots()
    ax.fill(x, y, 'g', alpha=0.2)
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.title('Plot of plenty.data')
    pyplot.show()

