"""
This function takes in string (s) and returns the words in reverse order
"""

def reverseString(s):
    startSplice = len(s) -1
    stopSplice = startSplice
    for i=startSplice >= 0:
        if s[i] == ' ':
            print(s[startSplice:stopSplice], s[i])
            startSplice= i-1
        else:
            i-=1
            stopSplice = i


s = "This is a test"
reverseString(s)
