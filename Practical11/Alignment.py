import os 
import pandas as pd
import re
os.chdir('C:/Users/admin/Downloads/IBI/week 11') #move to the directory which stores the offered fasta files
f1=open('SOD2_human.fa') # the following three codes open the fasta files
f2=open('SOD2_mouse.fa')
f3=open('RandomSeq.fa')
line1=f1.readlines() #the following three codes read the fasta files perspectively
line2=f2.readlines()
line3=f3.readlines()
SOD2_human='' #create three strings to store the sequences
SOD2_mouse=''
randomseq=''
for j in range(len(line1)): #extract the SOD2_human sequence from the fasta file and put it into the string
    if line1[j-1].startswith('>'):
        human=re.sub('\n','',line1[j])
        SOD2_human=SOD2_human+human
for j in range(len(line2)): #extract the SOD2_mouse sequence from the fasta file and put it into the string
    if line2[j-1].startswith('>'):
        mouse=re.sub('\n','',line2[j])
        SOD2_mouse=SOD2_mouse+mouse
for j in range(len(line3)): #extract the random sequence from the fasta file and put it into the string
    if line3[j-1].startswith('>'):
        random=re.sub('\n','',line3[j])
        randomseq=randomseq+random
print("The sequence of SOD2_human is "+SOD2_human+".")
print("The sequence of SOD2_mouse is "+(SOD2_mouse)+".")
print("The sequence of RandomSeq is "+(randomseq)+".")
edit_distance1 = 0 #creat new variables to store the number of different amino acids
edit_distance2 = 0
edit_distance3 = 0
score1 = 0 #create new variables to store the BLOSUM62 scores
score2 = 0
score3 = 0
print("The first comparison is human-mouse. The second comparison is human-random. The third comparison is mouse-random.")

amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*'] #The matrix is from https://blog.csdn.net/laixiangwei/article/details/105831376.
blosum = [
[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
[-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
[-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
[-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
[-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
[-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
[-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
[-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
[ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
[ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
[-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
]



for i in range(len(SOD2_human)):
    if SOD2_human[i]!=SOD2_mouse[i]: #calculate the number of different amino acids
        edit_distance1+=1 
    index1=amino.index(SOD2_human[i]) #calculate the BLOSUM62 score
    index2=amino.index(SOD2_mouse[i])
    score1=score1+blosum[index1][index2] 
percent1 = 1-edit_distance1/len(SOD2_human) #calculate the identity percentage
print("There are "+str(len(SOD2_human)-edit_distance1)+" identical amino acids in the first comparison.") #print out the results
print("The identity percentage of first comparison is "+str("%.2f%%"% (percent1*100))+".")
print("The alignment score of the first comparison is "+str(score1)+".")

for k in range(len(SOD2_human)):
    if SOD2_human[k]!=randomseq[k]: #calculate the number of different amino acids
        edit_distance2+=1
    index1=amino.index(SOD2_human[k]) #calculate the BLOSUM62 score
    index2=amino.index(randomseq[k])
    score2=score2+blosum[index1][index2]
percent2 = 1-edit_distance2/len(SOD2_human)
print("There are "+str(len(SOD2_human)-edit_distance2)+" identical amino acids in the second comparison.")#print out the results
print("The identity percentage of second comparison is "+str("%.2f%%"% (percent2*100))+".")
print("The alignment score of the second comparison is "+str(score2)+".")
for h in range(len(SOD2_mouse)):
    if SOD2_mouse[h]!=randomseq[h]: #calculate the number of different amino acids
        edit_distance3+=1
    index1=amino.index(SOD2_mouse[h]) #calculate the BLOSUM62 score
    index2=amino.index(randomseq[h])
    score3=score3+blosum[index1][index2]
percent3 = 1-edit_distance3/len(SOD2_mouse)#calculate the identity percentage
print("There are "+str(len(SOD2_mouse)-edit_distance3)+" identical amino acids in the third comparison.")#print out the results
print("The identity percentage of third comparison is "+str("%.2f%%"% (percent3*100))+".")
print("The alignment score of the third comparison is "+str(score3)+".")

