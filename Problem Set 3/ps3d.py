# MIT 6.00 - Intro to CS and Programming
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/index.htm
#
# Problem Set 3 (Part 4)
# Name: Pajama Programmer
# Date: 11-Nov-2015
# My solutions to problem 4 as described below

"""
Problem 4.

Write a function, called subStringMatchExactlyOneSub which takes two arguments:
a target string and a key string. This function should return a tuple of all
starting points of matches of the key to the target, such that at exactly one
element of the key is incorrectly matched to the target. Complete the definition

def subStringMatchExactlyOneSub(target,key):

"""
from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

# target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def subStringMatchExact(target,key):
    index = ()
    
    i = 0
    while i > -1:
        i = target.find(key, i)
        #print(i)
        if i > -1:
            index = index + (i,)
            i += 1
            
    return index

    
### the following procedure you will use in Problem 3
"""
n - a tuple representing starting points for the first substring
k - a tuple representing starting points for the second substring
m - length of the first substring

The function should return a tuple of all members of the first
tuple (n) for which there is an element in the second tuple (k) such
that n+m+1 = k, where m is the length of the first substring.
"""
def constrainedMatchPair(n,k,m):

    xTuple = ()

    for i in range (len(n)):
        for j in range (len(k)):
            if (n[i] + m + 1 == k[j]):
                xTuple += (n[i],)
    
    return xTuple


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print ('breaking key',key,'into',key1, '&', key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print ('match1',match1)
        print ('match2',match2)
        print ('possible matches for',key1, '&', key2,'start at',filtered)
    return allAnswers
      
def subStringMatchExactlyOneSub(target,key):
    
    allAnswers = subStringMatchOneSub(key,target)
    exactMatch = subStringMatchExact(target,key)

    oneSub = ()
    flag = 0
    #print('A possible matches',allAnswers)
    #print('Exact Matches', exactMatch)

    for i in range (len(allAnswers)):
        for j in range (len(exactMatch)):
            if (allAnswers[i] == exactMatch[j]):
                flag = 1 
                break

        if flag == 1: flag = 0
        else: oneSub += (allAnswers[i],)
    print('possible matches for', key, 'that allow for one incorrect element',oneSub)
    return oneSub


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':

    #print(target1.find(key10))
    #indices = subStringMatchExact(target1,key11)
    #print(indices)

    print('Target:', target2)
    print('Key:', key12)
    subStringMatchExactlyOneSub(target2, key12)
