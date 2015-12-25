#Project Euler Problem 4
largest_pal = 0
for a in xrange(999, 100, -1): #xrange seemed like the cleanest way to do this. 
    for b in xrange(a, 100, -1):#working from the largest 3 digit and moving backwards. 
        pal = a * b
        if pal > largest_pal:
            s = str(a * b) #flip to a string so we can check if this is really a palindrome
            if s == s[::-1]:
                 largest_pal = a * b
print largest_pal