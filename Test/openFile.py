from io import *
from urllib import *

'''
This is a test of opening and reading from files.
'''
f = open('TestFile.txt', 'r+')

for l in f:
    print(l)

f.write('I just added this line.')

for l in f:
    print(l)

urlopen('https://www.google.com')
