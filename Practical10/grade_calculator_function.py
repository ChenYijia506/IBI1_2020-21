#grade calculator function
a = input("student name:") #the following four lines allow users to input their information
b = input("grade for code portfolio:")
c = input("grade for poster ICA:")
d = input("grade for final exam:")
def final_grade(a,b,c,d): #define a function to calculate the total grade
    return 'The total grade of '+a+' is '+str(int(b)*0.4+int(c)*0.3+int(d)*0.3)
#the example used to test this function is name=Chen Yijia, grade for code=98, grade for poster=95 and grade for final=90
print(final_grade(a,b,c,d)) #print out the result

#another version of grade calculator function
def final_grade(name,code, poster,final): #define a function to calculate the total grade
    return 'The total grade of '+name+' is '+str(int(code)*0.4+int(poster)*0.3+int(final)*0.3)
name = 'Chen Yijia' #use an example to test the function
code = 98
poster = 95
final = 90
print(final_grade(name,code, poster,final)) #print the result
