"""Load white spaced numeric 2D data into numpy arrays"""

# load useful modules
import numpy
from matplotlib import pyplot

__all__ = ['loadData']
# make discoverable from all

"""Create module that can be reused for importing data of similar type"""


def loadData(fname):
    # fname holding variable allowing file to be input when function run
    # create empty lists to later append data
    x = []
    y = []
    inFile = open(fname, 'r')
    # open file as read only and attribute to inFile
    # loop to read a line of the file at a time
    for line in inFile.readlines():
        # split by white space to return a list of strings
        # append the first string to x and all other strings to y
        line = line.split()
        x.append(line[0])
        y.append(line[1:])
    # output x and y arrays converted to float
    inFile.close()
    return numpy.array(x, dtype=float), numpy.array(y, dtype=float)

# when loadData function is run as part of loaddata.py module then the below code is run
# if function run as part of another module then below code is not run


if __name__ == '__main__':
    # use the loadData function to read a data file and print the x and y function outputs
    x, y = loadData('plenty.data')
    print(x, y)
