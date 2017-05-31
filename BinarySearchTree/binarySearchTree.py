"""
    Create binary search tree for a list of numbers.
"""

import statistics

l = sorted([19,8,33,15,71,12,64,39,41,89,14,56,48,77,25,93,51,46,70,86,9,78,68])



def binarySearchTree (l):
    print("The median of the list is " + str(statistics.median(l)))
    print("The length of the list is " + str(len(l)))
    for i in l:
        print(i)

binarySearchTree(l)
