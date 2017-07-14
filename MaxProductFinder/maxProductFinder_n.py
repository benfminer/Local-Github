"""
This takes an array of numbers and finds the max product of n numbers.
"""

def maxProductFinder(l,n):

    sortL = sorted(l)
    product = 1
    count = n
    index = 0
    print(sortL)

    while count >= 3:
        if abs(min(sortL)) > abs(max(sortL)):
            index = sortL.index(min(sortL))
            product *= sortL.pop(index)
            count--1
        else:
            index = sortL.index(max(sortL))
            product *= sortL.pop(index)
            count--1

    if product > 0:
        if (sortL[0] * sortL[1]) > sortL[len(sortL)- 2] * sortL[(len(sortL) - 3)]:
            product *= sortL[0]*sortL[1]
        else:
            product *= sortL[len(sortL)- 2]*sortL[(len(sortL) - 3)]
    else:
        index = sortL.index(min(sortL))
        product *= sortL.pop(index)
        index = sortL.index(max(sortL))
        product *= sortL.pop(index)

    return product


test = [-6, -8, 4, 2, 5, 3, -1, 9, 10]
print(maxProductFinder(test,5))
