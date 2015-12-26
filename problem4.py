#Project Euler Problem 4
largest_pal = 0
for x in range(999, 100, -1): #range seemed like the cleanest way to do this. 
    for y in range(x, 100, -1):#working from the largest 3 digit and moving backwards. 
        pal = x * y
        if pal > largest_pal:
            s = str(x * y) #flip to a string so we can check if this is really a palindrome
            if s == s[::-1]:
                 largest_pal = x * y
print largest_pal
