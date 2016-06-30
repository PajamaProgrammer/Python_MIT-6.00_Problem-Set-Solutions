# MIT 6.00, Problem Set 8, Intelligent Course Advisor
# Name: Pajama Programmer
# Date: 2-Jun-2016
#
# At an institute of higher education that shall be nameless, it used to be the
# case that a human advisor would help each student formulate a list of subjects
# that would meet the student’s objectives. However, because of financial troubles,
# the Institute has decided to replace human advisors with software. Given the
# amount of work a student wants to do, the program returns a list of subjects that
# maximizes the amount of value.
#
# The goal of this problem set is to implement a dynamic programming algorithm and
# learn how to pass functions as arguments. 
#
#

import time

SUBJECT_TESTFILE = "subjectsTest.txt"
SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    inputFile = open(filename)
    d = dict()
    for line in inputFile:
        subject, value, work = line.strip().split(',')
        d[subject] = (int(value),int(work))
    return d
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = list(subjects.keys())
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)

#printSubjects(loadSubjects(SUBJECT_FILENAME))
    
def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    d = dict()  #create return dictionary

    #Get a sorted list of all subjects
    subNames = sorted(subjects.keys())

    #Will iterate until all subjects are removed from the list
    while len(subNames) > 0 and maxWork != 0:
        #Assign first element in list as max value
        maxSub = subNames[0]
        maxTup = subjects[maxSub]

        #iterate through each available subject
        for subject in subNames:

            #update max value if a bigger comparator is found
            if comparator(subjects[subject], maxTup):
                maxTup = subjects[subject]
                maxSub = subject

        #remove max value from list   
        subNames.remove(maxSub)

        #if there is work still available,
        if (maxWork - maxTup[WORK]) > -1:
            d[maxSub] = maxTup              #then add max value to return dictionary 
            maxWork -= maxTup[WORK]         #and decrement available work

    #return dictionary        
    return d

#catalog = loadSubjects(SUBJECT_TESTFILE)
catalog = loadSubjects(SUBJECT_FILENAME)
#printSubjects(catalog)
print("Greedy Advisor - Value")
printSubjects(greedyAdvisor(catalog, 30, cmpValue))
print("Greedy Advisor - Work")
printSubjects(greedyAdvisor(catalog, 30, cmpWork))
print("Greedy Advisor - Ratio")
printSubjects(greedyAdvisor(catalog, 30, cmpRatio))

    
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

##print("Brute Force Advisor")
##printSubjects(bruteForceAdvisor(catalog, 5))  
#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    for n in range(1, 201):
        print("Brute Force:",n, "hour")
        
        start_time = time.time()
        course_list = bruteForceAdvisor(catalog, n)
        end_time = time.time() - start_time
        printSubjects(course_list)
        print("Time:",end_time, "Seconds\n")
        if (end_time > 5):  #5 seconds is enough for me...
            return
        

#bruteForceTime()

# Problem 3 Observations
# ======================
#
##Brute Force: 1 hour
##Course	Value	Work
##======	====	=====
##7.17	10	1
##
##Total Value:	10
##Total Work:	1
##
##Time: 0.002000093460083008 Seconds
##
##Brute Force: 2 hour
##Course	Value	Work
##======	====	=====
##6.00	10	1
##7.17	10	1
##
##Total Value:	20
##Total Work:	2
##
##Time: 0.012000799179077148 Seconds
##
##Brute Force: 3 hour
##Course	Value	Work
##======	====	=====
##15.01	7	1
##6.00	10	1
##7.17	10	1
##
##Total Value:	27
##Total Work:	3
##
##Time: 0.057003021240234375 Seconds
##
##Brute Force: 4 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##6.00	10	1
##7.17	10	1
##
##Total Value:	34
##Total Work:	4
##
##Time: 0.23501348495483398 Seconds
##
##Brute Force: 5 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##6.00	10	1
##7.00	7	1
##7.17	10	1
##
##Total Value:	41
##Total Work:	5
##
##Time: 0.8300473690032959 Seconds
##
##Brute Force: 6 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##6.00	10	1
##7.00	7	1
##7.16	7	1
##7.17	10	1
##
##Total Value:	48
##Total Work:	6
##
##Time: 2.6841535568237305 Seconds
##
##Brute Force: 7 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##24.12	6	1
##6.00	10	1
##7.00	7	1
##7.16	7	1
##7.17	10	1
##
##Total Value:	54
##Total Work:	7
##
##Time: 8.243471622467041 Seconds
#
# Problem 4: Subject Selection By Dynamic Programming
#

def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # PSEUDOCODE
    # create list of work/values
    # start index at end of list,
    #
    # calculate branch with_i
    # calculate branch without_i
    # return max branch

    memo = {}
    #Get list of subjects and corresponding work/value tuples
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    ##print(nameList)
    ##print(tupleList)
    #Get optimal course list that maximizes value
    v, course_list = dpAdvisorHelper(tupleList, len(tupleList)-1, maxWork, memo)
    ##for key in memo.keys():
    ##    print(key,":",memo[key])
    #Convert course list to dictionary and return dictionary
    d = {}
    for course in course_list:
        d[nameList[course]] = tupleList[course]
    return d
    
def dpAdvisorHelper(work_value, i, availWork, memo, space=""):
    """
    work_value - is a list of tuples
    i - represents an index to a corresponding subject.
        - Subject i has work of work_value[i][WORK] and value work_value[i][VALUE]
    availWork - represents the amount of work still available
    memo - used to keep track of previously computed branches. The key of memo is tuple (i, availWork) which maps to tuple of (value, [course_list])
    space - optional for printing/debugging

    This function acts like a binary tree, at each index i, the function will calculate the value without_i and with_i.
    Then return the branch with the maximum value 
    """
    #print(space, i, availWork)
    try:
        #Check if computation has been done before
        return memo[(i, availWork)]
    except KeyError:
        #Base Case when i == 0, functions starts at the end of list and works back to start of list
        if i==0:
            if work_value[i][WORK] <= availWork:
                memo[(i, availWork)] = work_value[i][VALUE], [i]
                return work_value[i][VALUE], [i]
            else:
                memo[(i, availWork)] = 0, []
                return 0, []

        #Check Yes/No Branches
        no_i, no_list = dpAdvisorHelper(work_value, i-1, availWork, memo, space + "NO\t")
        
        if work_value[i][WORK] > availWork:
            memo[(i, availWork)] = no_i, no_list
            return no_i, no_list
        else:
            yes_i, yes_list = dpAdvisorHelper(work_value, i-1, availWork-work_value[i][WORK], memo, space +"YES\t")
            yes_i += work_value[i][VALUE]
            
        #print(space, i, no_i, availWork, space, i, yes_i, availWork)
        if yes_i > no_i:
            i_value = yes_i
            i_list = yes_list + [i]
        else:
            i_value = no_i
            i_list = no_list

        #print(space+"RESULT", i, i_value, availWork)       
        memo[(i, availWork)] = i_value, i_list

        return i_value, i_list

print("Dynamic Programming Advisor")
printSubjects(dpAdvisor(catalog, 30))      
    
#
# Problem 5: Performance Comparison
#

def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    for n in range(1, 8):
        print("Dynamic Programming:",n, "hour")
        
        start_time = time.time()
        course_list = dpAdvisor(catalog, n)
        end_time = time.time() - start_time
        printSubjects(course_list)
        print("Time:",end_time, "Seconds\n")
        if (end_time > 5):  #5 seconds is enough for me...
            return

#dpTime()
# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.
#
##Dynamic Programming: 1 hour
##Course	Value	Work
##======	====	=====
##7.17	10	1
##
##Total Value:	10
##Total Work:	1
##
##Time: 0.003000020980834961 Seconds
##
##Dynamic Programming: 2 hour
##Course	Value	Work
##======	====	=====
##6.00	10	1
##7.17	10	1
##
##Total Value:	20
##Total Work:	2
##
##Time: 0.002000093460083008 Seconds
##
##Dynamic Programming: 3 hour
##Course	Value	Work
##======	====	=====
##15.01	7	1
##6.00	10	1
##7.17	10	1
##
##Total Value:	27
##Total Work:	3
##
##Time: 0.0030002593994140625 Seconds
##
##Dynamic Programming: 4 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##6.00	10	1
##7.17	10	1
##
##Total Value:	34
##Total Work:	4
##
##Time: 0.00500035285949707 Seconds
##
##Dynamic Programming: 5 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##6.00	10	1
##7.00	7	1
##7.17	10	1
##
##Total Value:	41
##Total Work:	5
##
##Time: 0.007000446319580078 Seconds
##
##Dynamic Programming: 6 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##6.00	10	1
##7.00	7	1
##7.16	7	1
##7.17	10	1
##
##Total Value:	48
##Total Work:	6
##
##Time: 0.008000373840332031 Seconds
##
##Dynamic Programming: 7 hour
##Course	Value	Work
##======	====	=====
##12.04	7	1
##15.01	7	1
##24.12	6	1
##6.00	10	1
##7.00	7	1
##7.16	7	1
##7.17	10	1
##
##Total Value:	54
##Total Work:	7
##
##Time: 0.008000373840332031 Seconds


