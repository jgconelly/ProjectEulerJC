#Project Euler Problem 5
import sys #Importing sys to use the maxint function

def smallestDivisors(n):
    divisors = [x for x in range(1, (n+1))]  #Finds all divisors using range. 
    for i in xrange(2520, sys.maxint, n): 
        if (all(i%x == 0 for x in divisors)): #Using all to iterate through and check if the number is actually divisible by all those numbers.
            return i

print (smallestDivisors(20))