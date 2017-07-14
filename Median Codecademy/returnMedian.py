"""
This program takes a list of numbers and returns the median  value.
"""

def returnMedian(l):
    orderL = sorted(l)
    n = len(l)/2
    print(n)
    print(orderL)

    if (len(l)/2) == 0:
        return((orderL[int(n)]+orderL[int(n+1)])/2.0)
    else:
        return(orderL[int(n)])

print(returnMedian([5,10,-3,7,9]))
print(returnMedian([6,10,2,5,9,3,10,12,18,-3]))
