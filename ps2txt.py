# Problem Set 2 (Part I\II)
# Name: Pajama Programmer
# Date: 28-Oct-2015
#

"""
Problem 1.

Show that it is possible to buy exactly 50, 51, 52, 53, 54, and 55 McNuggets,
by finding solutions to the Diophantine equation.

You can solve this in your head, using paper and pencil, or writing a program.
However you chose to solve this problem, list the combinations of 6, 9 and 20
packs of McNuggets you need to buy in order to get each of the exact amounts.

Given that it is possible to buy sets of 50, 51, 52, 53, 54 or 55 McNuggets by
combinations of 6, 9 and 20 packs, show that it is possible to buy 56, 57,…,
65 McNuggets. In other words, show how, given solutions for 50-55, one can
derive solutions for 56-65.

6a+9b+20c=nuggets
"""
"""
This program will iteratively provide the all possible combinations of 6, 9, and 20,
such that 6a+9b+20c = n where 50 <= n <= 65

Because the smallest pack is 6, once there are six consecutive solutions for n
(such that 6a+9b+20c=n), then it is possible derive solutions for all consecutive values for n.
This can be done by simply adding a pack of 6 to a previous solution:
50 + 6 = 56, 51 + 6 = 57, 52 + 6 = 58, 53 + 6 = 59, 54 + 6 = 60, 55 + 6 = 61, , 56 + 6 = 62.....
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
                     PrintNuggetSolution (a, b, c, nuggets)
    return

for i in range(50,65):
    PrintNuggetFunction(i)
    FindNuggetSolution(i)
    
