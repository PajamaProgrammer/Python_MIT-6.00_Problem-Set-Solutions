# MIT 6.00 - Intro to CS and Programming
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/index.htm
#
# Problem Set 3 (Part 2)
# Name: Pajama Programmer
# Date: 10-Nov-2015
# My solutions to problem 2 as described below

"""
Problem 2.
Write the function subStringMatchExact. This function takes two arguments:
a target string and a key string. It should return a tuple of the starting
points of matches of the key string in the target string, when indexing starts
at 0. Complete the definition for

def subStringMatchExact(target,key):

For example, subStringMatchExact("atgacatgcacaagtatgcat","atgc") would return
the tuple (5, 15). The file ps3_template.py includes some test strings that you
can use to test your function. In particular, we provide two target strings:

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

and four key strings:

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

Test your function on each combination of key and target string, as well as
other examples that you create.
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
def subStringMatchOneSub(key,target):
"""    """search for all locations of key in target, with one substitution""""""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
"""        



# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':

    #print(target1.find(key10))
    indices = subStringMatchExact(target1,key11)
    print(indices)






            



