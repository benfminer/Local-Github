"""
This takes an array of numbers and finds the max product of 3 numbers.
"""

def maxProductFinder(l):

    sortL = sorted(l)
    product = 0
    print(sortL)
    product += max(sortL)
    print(product)
    print(sortL[0] * sortL[1])

    print(sortL)
    if (sortL[0] * sortL[1]) > sortL[len(sortL)- 2] * sortL[(len(sortL) - 3)]:
        product *= sortL[0]*sortL[1]
    else:
        product *= sortL[len(sortL)- 2]*sortL[(len(sortL) - 3)]
    return product

test = [-6, -8, 4, 2, 5, 3, -1, 9, 10]
print(maxProductFinder(test))
