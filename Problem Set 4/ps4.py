# MIT 6.00 - Intro to CS and Programming
# http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/index.htm
# Problem Set 4
# Name: Pajama Programmer
# Date: 24-Nov-2015

#
# Problem 1
#
"""
End of year 1
F[0] = salary * save * 0.01
End of year 2
F[1] = F[0] * (1 + 0.01 * growthRate) + salary * save * 0.01
End of year 3
F[2] = F[1] * (1 + 0.01 * growthRate) + salary * save * 0.01
"""
def nestEggFixed(salary, save, growthRate, years):
    nestEgg = []
    savings = salary*save*0.01
    growth = 1 + 0.01 * growthRate

    if (years < 2):
        nestEgg = [savings]
        #print("In the base Case. Starting Nest Egg =", nestEgg) 
        return nestEgg

    nestEgg = nestEggFixed(salary, save, growthRate, years-1) + [savings]
    #print("After", years, "years:")
    growth *= nestEgg[years-2]
    nestEgg[years-1] += growth
    #print(nestEgg)
  
    return nestEgg
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """

def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.

#
# Problem 2
#
"""
End of year 1
F[0] = salary * save * 0.01
End of year 2
F[1] = F[0] * (1 + 0.01 * growthRate) + salary * save * 0.01
End of year 3
F[2] = F[1] * (1 + 0.01 * growthRate) + salary * save * 0.01
"""
def nestEggVariable(salary, save, growthRates):
    years = len(growthRates)
    #print(years)
    nestEgg = [salary * save * 0.01]
    
    for i in range(1,years):
        #print(i)
        nestEgg += [nestEgg[i-1]*(1 + 0.01 * growthRates[i]) + nestEgg[0]]
    return nestEgg
    
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#
"""
Retirement fundEnd of year 1
F[0] = savings * (1 + 0.01 * growthRates[0]) – expenses
End of year 2
F[1] = F[0] * (1 + 0.01 * growthRates[1]) – expenses
End of year 3
F[2] = F[1] * (1 + 0.01 * growthRates[2]) – expenses
"""
def postRetirement(savings, growthRates, expenses):
    years = len(growthRates)
    #print(years)
    nestEgg = [savings*(1 + 0.01 * growthRates[0]) - expenses]
    
    for i in range(1,years):
        #print(i)
        nestEgg += [nestEgg[i-1]*(1 + 0.01 * growthRates[i]) - expenses]
    return nestEgg
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    preYears = len(preRetireGrowthRates)
    pre = nestEggVariable(salary, save, preRetireGrowthRates)
    print (pre)
    
    postYears = len(postRetireGrowthRates)
    
    high = pre[preYears-1]
    low = 0
    #epsilon = 4000
    for i in range (1000):    #limiting the number of serches with a for loop
        guess = (high + low)/2
        post = postRetirement(pre[preYears-1], postRetireGrowthRates, guess)[postYears-1]
        print ("Iteration:",i,"high:",high,"low:",low,"guess:",guess,"Leftover:",post)
        if post < epsilon and post > -epsilon:
            break
        if post < 0:
            high = guess
        else:
            low = guess
        
    
    return guess
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print (expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
