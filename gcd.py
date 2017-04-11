from random *

'''
This definition takes 2 numbers and finds the greatest common denomenator.
It will return the GCD(Greatest Common Denomenator)
'''

def gcd(x,y):
    while max(x,y)%min(x,y) != 0:
        x = min(x,y)
        y = max(x,y)%min(x,y)
    return max(x,y)%min(x,y)

x = random()
y = random()

print('The greatest common denomenator of ', x, ' and ', y, ' is ', gcd(x,y), '.'
