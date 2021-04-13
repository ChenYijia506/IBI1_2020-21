#define r = 1.2 n = 84
#for loops in range(1,6):
#Multiply
#multiplying()
#How many loops completed?
#If less than 5: keep multiplying
#If 5: DONE!
#if(loops == 5):
#done()

#Define the variables we need to use to calculate.
r = 1.2
n = 84
#Create a loop to calculate how the number of people infected increases.
for i in range(1,6):
  n = n + n*r
#Print how many peple get infected after 5 rounds. Since the number of people is discrete variale, we need to change n into an integer.
if type(n) == int:
  print(n)
else:
  print(int(n)+1)
