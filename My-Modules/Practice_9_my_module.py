
# 1. an Example of How to Import a Module :
print('Imported Practice_9_my_module...')

test = 'Test String'


def find_index(to_search, target):
    '''Find the Index of a Value in a Sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    
    return -1
# * We want to use this Function in other Modules Or Scripts, So What we gonna do is Import this.

