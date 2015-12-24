#Project Euler Problem 3
#I wrote this as a function so it could be easily used later. 
def largest_prime_factor(n):
	i = 2 #Starting at 2 makes sense here. 
	while i * i <= n: #The largest prime factor can't be larger than the sqr root of n. This checks for that. 
		if n % i:
			i += 1
		else: 
			n //= i
	return n

print largest_prime_factor(600851475143)