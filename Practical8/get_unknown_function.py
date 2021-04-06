import os
import pandas as pd
import re
#move to the directory which store the fasta file
os.chdir('C:/Users/admin/Downloads/IBI/week 8')
#read the fasta file
f=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
f2=open('unknown_function.fa','w')
lines=f.readlines()
#create new lists and a string to store the extracted information
names=[]
seq=[]
DNA=''
#extract the names and DNA sequence of unknown function genes
for i in range(len(lines)):
    if lines[i].startswith('>') and re.search(r'unknown function',lines[i]):
        name=re.findall(r'(>.+)_mRNA',lines[i])
        names.append(name)
    elif lines[i-1].startswith('>') and re.search(r'unknown function',lines[i-1]):
        DNA=''
        for j in range(i,len(lines)):
            if lines[j].startswith('>'):
                break
            else:
                line=re.sub('\n','',lines[j])
                DNA=DNA+line
        seq.append(DNA)
length=[]
#calculate the length of DNA of the unknown function genes
for i in range(len(seq)):
    l=len(seq[i])
    length.append(l)

#put all the information together
x=''
for i in range(len(seq)):
    x=x+str(names[i])+' '+str(length[i])+'\n'+str(seq[i])+'\n'
f2.write(x)
f.close()
f2.close()
f2=open('unknown_function.fa','r')
print(f2.read())
f2.close()
