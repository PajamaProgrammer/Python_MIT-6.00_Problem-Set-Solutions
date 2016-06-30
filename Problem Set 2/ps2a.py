# Problem Set 2 (Part III)
# Name: Pajama Programmer
# Date: 28-Oct-2015
#

"""
Problem 3.
Write an iterative program that finds the largest number of McNuggets that cannot be bought in exact quantity.
Your program should print the answer in the following format (where the correct number is provided in place of <n>):
“Largest number of McNuggets that cannot be bought in exact quantity: <n>”

6a+9b+20c=nuggets
"""

def PrintNuggetFunction (nuggets):
    print ('I want to order Chicken McNuggets in packs of 6, 9, and 20 so that I have exactly', nuggets, 'nuggets')
    return

def PrintNuggetSolution (a, b, c, nuggets):
    print ('It takes', a, 'packs of 6,', b, 'packs of 9, and', c, 'packs of 20 Chicken McNuggets to =', nuggets)
    return

def FindNuggetSolution (nuggets):
    for c in range (0, nuggets):
        for b in range (0, nuggets):
            for a in range (0, nuggets):
                if (6*a + 9*b + 20*c == nuggets):
                     #PrintNuggetSolution (a, b, c, nuggets)
                     return 1
    return 0

#looking for largest value of nuggest that cannot be bought in packs of 6, 9, and 20
counter = 0
nuggets = 1

for n in range(6,100):
    if FindNuggetSolution(n) == 0:
        counter = 0
        nuggets = n
    else:
        counter +=1
        #print(counter)

    if counter == 6:
        break

print ("Largest number of McNuggets that cannot be bought in exact quantity:", nuggets )
    
