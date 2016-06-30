# Problem Set 2 (Part 4)
# Name: Pajama Programmer
# Date: 28-Oct-2015
#
"""
Problem4.
Assume that the variable packages is bound to a tuple of length 3, the values of which specify
the sizes of the packages, ordered from smallest to largest. Write a program that uses
exhaustive search to find the largest number (less than 200) of McNuggets that cannot be bought
in exact quantity. We limit the number to be less than 200 (although this is an arbitrary choice)
because in some cases there is no largest value that cannot be bought in exact quantity, and we
don’t want to search forever. Please use ps2b_template.py to structure your code.
Have your code print out its result in the following format:
“Given package sizes <x>, <y>, and <z>, the largest number of McNuggets that cannot be bought in exact quantity is: <n>”
Test your program on a variety of choices, by changing the value for packages.
Include the case (6,9,20), as well as some other test cases of your own choosing.

"""

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (9,11,20)   # variable that contains package sizes

def PrintNuggetFunction (nuggets, x, y, z):
    print ('I want to order Chicken McNuggets in packs of', x, y, 'and', z, 'so that I have exactly', nuggets, 'nuggets')
    return

def PrintNuggetSolution (nuggets, x, y, z):
    print ('It takes', x, 'packs of 6,', y, 'packs of 9, and', z, 'packs of 20 Chicken McNuggets to =', nuggets)
    return

def FindNuggetSolution (nuggets, x, y, z):
    for c in range (0, nuggets):
        for b in range (0, nuggets):
            for a in range (0, nuggets):
                if (x*a + y*b + z*c == nuggets):
                     #PrintNuggetSolution (nuggets, x, y, z)
                     return 1
    return 0


x = packages[0]
y = packages[1]
z = packages[2]

for n in range(1, 200):   # only search for solutions up to size 200
    if FindNuggetSolution(n, x, y, z) == 0:
        counter = 0
        bestSoFar = n
    else:
        counter +=1
        #print(counter)

    if counter == x:
        break
    


print ('Given package sizes <', x,'>, <', y,'>, and <', z, '>, the largest number of McNuggets that cannot be bought in exact quantity is: ', bestSoFar, sep='')
