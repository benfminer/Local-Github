'''
Creates program to find all prime factors of number (n)
then summs results.
'''

def primeFactor(n):
    total = 0
    while n >3:
        if n%2 == 0:
            total += 2
            n = n/2
            primeFactor(n)
        else:
            divisor = 3
            while n%divisor != 0:
                divisor += 2
            total += divisor
            n = n/divisor
            primeFactor(n)
    print(totoal)

n = int(input("Please Enter number: "))
primeFactor(n)
