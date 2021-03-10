#for loops in range(3,14):
#Add
#adding()
#Sequence
#sequencing()
#How many loops completed?
#If less than 13: keep adding and sequencing
#If 13: DONE!
#if(loops == 13):
#done()

#Define the first and second terms of fibonacci sequence.
X = 1
print("第1项是"， X）
Y = 1
print("第2项是", Y)
#Create a loop to calculate the other terms of the sequence.
for i in range(3,14):
Z = X + Y
X = Y
Y = Z
#Then print the terms of the sequence.
print("第", i, "项是", Z)
