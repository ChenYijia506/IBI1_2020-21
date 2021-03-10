# What does this piece of code do?
# Answer:This code chooses a number from 1 to 100 randomly. If the number chosen is bigger than 50, then keep running the loop. If the number is smaller or equals to 50, then print the number. 

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil


p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False

print(n)
