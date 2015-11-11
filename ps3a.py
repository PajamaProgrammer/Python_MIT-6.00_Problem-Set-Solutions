# MIT 6.00 - Intro to CS and Programming
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/index.htm
#
# Problem Set 3 (Part 1)
# Name: Pajama Programmer
# Date: 10-Nov-2015
# My solutions to Problem 1 as described below.

"""
Problem 1.
Write two functions, called

countSubStringMatch
and 
countSubStringMatchRecursive

that take two arguments, a key string and a target string.
These functions iteratively and recursively count the number of instances
of the key in the target string. You should complete definitions for

def countSubStringMatch(target,key):
and
def countSubStringMatchRecursive (target, key):

"""
from string import *

def countSubStringMatch(target,key):
    counter = 0
    index = 1

    while index > 0:
        index = target.find(key, index) + 1
        #print(index)
        if index:
            counter +=1
            
    return counter

def countSubStringMatchRecursive (target, key):
    index = target.find(key)
    #print(target)
    #print(key)

    if index < 0:
        #print('In the Base Case!')
        return 0
    else:
        count = countSubStringMatchRecursive (target[index+1:], key) + 1
        #print ('Return to Base Case, Count = ', count)
        return count
    



# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':
    s = "atgacatgcacaagtatgcat"
    k = "atgc"
    count = countSubStringMatch(s, k)
    print (count)


    count1 = countSubStringMatchRecursive(s, k)
    print (count1)
