#Project Euler Problem 2
previous_fibi = 1
current_fibi = 1
even_fibi_sum = 0

while current_fibi <= 4000000:
	if current_fibi % 2 == 0:
		even_fibi_sum += current_fibi
	dummy_fibi = current_fibi
	current_fibi = current_fibi + previous_fibi
	previous_fibi = dummy_fibi

print(even_fibi_sum)

#Not a big fan of these variable names, but hopefully you get what I am doing here. 
