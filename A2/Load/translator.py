"""Create dictionary to use for translating strings. Allows brackets and new line notification to be removed"""

"""While this is slightly over engineered for the use case of Task 2, this allows creates a flexible module which 
can be modified and/or reused for other use cases

"""

__all__ = ['transtable']
# make discoverable from all

def transtable():
    table1 = str.maketrans(dict.fromkeys("()\n[]"))
    return table1

if __name__ == '__main__':
    print(transtable())