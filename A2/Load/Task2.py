"""load polygon coordinates and 1 associated attribute from badly formatted .dat file to a dictionary: list of lists
structure

"""

# load useful modules
# load my own module which creates a dictionary to translates unwanted characters to ""
from Load.translator import transtable

__all__ = ['loadPolyData']
# make discoverable from all

"""Create module that can be reused for importing data of similar type"""


def loadPolyData(fname1):
    # fname1 holding variable allowing file to be input when function run
    # create blank lists, variable and dictionary for populating later
    metadata = []
    x = []
    y = []
    a_dict = {}
    baddata = []
    baddatacount = 0
    # open file as read only and attribute to file
    # loop to read a line of the file at a time
    file = open(fname1, 'r')
    for line in file.readlines():
        if line[0] == '#':
            # # identifies metadata therefore appended to metadata list as important information to retain
            metadata.append(line.strip('\n'))
        elif line[0].isalpha():
            # alpha identifies names of natural neighbourhoods and therefore is assigned to key
            line = line.translate(transtable())
            key = line
        elif line[0] == '(':
            # ( identifies data therefore removes brackets, splits by comma and converts to float
            line = line.translate(transtable())
            line = line.split(', ')
            x.append(float(line[0]))
            y.append(float(line[1]))
        elif line == "\n":
            # empty line identifies end of data and therefore triggers variables x, y and key to update dictionary
            a_dict.update({key: [x, y]})
            x = []
            y = []
            # reset x and y to empty lists so no coordinates from previous key remain
        else:
            baddatacount = baddatacount + 1
            # count the number of times else: continue is used i.e. the amount of bad data
            baddata.append(key)
            # append key to identify where bad data occurs
            continue
            # Acts as exception as allows programme to continue where otherwise it would error
            # Errors should not pass silently unless explicitly silenced - Zen of Python
        file.close()
    return metadata, a_dict, baddata, baddatacount

# when loadData function is run as part of Plot.py module then the below code is run
# if function run as part of another module then below code is not run


if __name__ == '__main__':
    # use the loadPolyData function to read a data file
    metadata, a_dict, baddata, baddatacount = loadPolyData('../natural_neighbourhoods.dat')
    # print titles and associated data using loops to separate onto new lines
    print('Natural Neighbourhoods')
    for j in a_dict.keys():
        print(j, sep='/n')
    # print formatted bad data results
    print(f'Bad data = {baddata} Total = {baddatacount}')
    print('Metadata')
    for i in metadata:
        print(i, len(i), sep='/n')
