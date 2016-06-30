# Problem Set 1
# Name: Rebecca Owen
# Date: 19-Oct-2015
# MIT OCW 6.000 Introduction to Computer Science and Programming 
#
# This program will compute all the primes from 2 to a user inputed number n
# The program will then sum the logarithms of all primes from 2 to n.
# And then display the sum of logs, n, and the ratio of the sums to n

from math import *

            #A prime number (or a prime) is a natural number greater than 1
            #that has no positive divisors other than 1 and itself. A natural
            #number greater than 1 that is not a prime number is called a composite number.

n = int(input('Please enter a positive interger > 2: '))

             
prime = 2   #The number 2 is the first prime number
sumoflogs = log(prime)


testnumber = 3

if n==2 :
    print ('I found all primes less than:', n)
    print ('Sum of Logs of Primes from 2 to',n,'=', sumoflogs)
    print ('Ratio is', sumoflogs/n)
    

prime +=1   #The number 3 is the second prime number
sumoflogs += log(prime)
if n==3 or n==4:
    print ('I found all primes less than:', n)
    print ('Sum of Logs of Primes from 2 to',n,'=', sumoflogs)
    print ('Ratio is', sumoflogs/n)

prime += 2

while prime <= n :
    
    while testnumber <= prime :
        if testnumber == prime :
            sumoflogs += log(prime)
            testnumber = 3
            break

        if prime%testnumber : #could be prime, generate next test number
            testnumber +=2
        elif (prime%testnumber == 0) and (testnumber < prime) : #can't be prime...
            testnumber = 3
            break
    prime += 2

print ('I found all primes less than:', n)
print ('Sum of Logs of Primes from 2 to',n,'=', sumoflogs)
print ('Ratio is', sumoflogs/n)
    
        
        
