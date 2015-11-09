# Problem Set 1
# Name: Pajama Programmer
# Date: 19-Oct-2015
# MIT OCW 6.000 Introduction to Computer Science and Programming 
#
# This program will compute the 1000th prime number and print it to the screen

odd = 1     #A prime number (or a prime) is a natural number greater than 1
            #that has no positive divisors other than 1 and itself. A natural
            #number greater than 1 that is not a prime number is called a composite number.

prime = 2   #The number 2 is the first prime number
counter = 1
testnumber = 3

#print (prime)
#print (' ')
prime +=1   #The number 3 is the second prime number
counter +=1
#print (prime)
#print (' ')

while counter < 1000 :
    prime += 2; #Generate possible Prime - Will only consider odd numbers

    #print ('Is ',prime,' a prime?')
    while testnumber <= prime :

        if testnumber == prime :
            counter += 1
            testnumber = 3
            #print ('Prime :',prime)
            break
        #print ('Test Number ',testnumber)

        if prime%testnumber : #could be prime, generate next test number
            testnumber +=2
        elif (prime%testnumber == 0) and (testnumber < prime) : #can't be prime...
            testnumber = 3
            break

print ('The 1000th prime number is :',prime) 

    
        
        
