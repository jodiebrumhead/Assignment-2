"""Plotting a map of natural_neighbourhoods.dat to satisfy Task 2 of Assignment 2 for TGIS"""

# load useful modules
from matplotlib import pyplot
# load my own module and function
from Load.Task2 import loadPolyData

# Exception used to handle file not found errors, a likely possible error when reusing code for other datasets
try:
    # use the loadPolyData function to read a data file
    metadata, a_dict, baddata, baddatacount = loadPolyData('../natural_neighbourhoods.dat')
except FileNotFoundError as e:
    print(e)
else:
    # loop to plot coordinates for each key in the dictionary
    for key in a_dict.keys():
        figure = pyplot.plot(a_dict[key][0], a_dict[key][1])
        # add plot details
        pyplot.xlabel('X')
        pyplot.ylabel('Y')
        pyplot.grid(b=True, color='k', alpha=0.5, linestyle='-')
        pyplot.title('Natural Neighbourhoods of Edinburgh')
    # show plot
    pyplot.show()



# cartopy and labels....
