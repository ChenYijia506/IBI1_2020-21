import os
os.chdir('E:/IBI/week 14') #move to the directory where the xml file is located
import re
from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("go_obo.xml") #open the xml file
collection = DOMTree.documentElement #extract the elements in the xml file 
Term = collection.getElementsByTagName("term") #extract the terms
DNA=[] #the following four codes are created to store new information
RNA=[]
Protein=[]
Carbohydrate=[]

for term in Term:
    defstr=term.getElementsByTagName("defstr")[0] #get the information in the "defstr" element
    text=defstr.childNodes[0].data #store the information as string
    ids=term.getElementsByTagName("id")[0] #get the information in the "id" element
    id1=ids.childNodes[0].data #store the information as string
    if re.findall(r'DNA',text): #the following four "if" loops are to store all the id of DNA/RNA/protein/carbohydrate-related genes into the corresponding lists
        DNA.append(id1)
    if re.findall(r'RNA',text):
        RNA.append(id1)
    if re.findall(r'protein',text):
        Protein.append(id1)
    if re.findall(r'carbohydrate',text):
        Carbohydrate.append(id1)

isa=collection.getElementsByTagName("is_a") #extract the "is_a" elements
def childNodes_calculator(x): #create a function
    global count #create two variables which will be changed while running the loop to store new information
    global number
    count=0 #create a variable for judgement
    childNodes=[] #create a list to store new information
    for k in range(0,isa.length):
        for i in x:
            if i==isa[k].childNodes[0].data: #if the id of the "is_a" element is the same as the id of DNA/RNA/protein/carbohydrate-related gene, there will be one childNode
                count+=1
                number+=1
                childNodes.append(isa[k].parentNode.childNodes[1]) #change the childNodes list for further searching for childNodes
    print(number)
    if count!=0: #search for childNodes of the next or further levels
        x=childNodes
        childNodes_calculator(x)
    if count==0:
        return number

number=0 #the followings are assignment statements
childNodes_calculator(DNA)
dna=number

childNodes_calculator(RNA)
rna=number

childNodes_calculator(Protein)
protein=number

childNodes_calculator(Carbohydrate)
carbohydrate=number

print("The number of childNodes for DNA-related genes is "+str(dna)+".") #the following four codes are to print out the result

print("The number of childNodes for RNA-related genes is "+str(rna)+".")

print("The number of childNodes for protein-related genes is "+str(protein)+".")

print("The number of childNodes for carbohydrate-related genes is "+str(carbohydrate)+".")

import matplotlib.pyplot as plt
labels = 'DNA','RNA','Protein','Carbohydrate' #define the labels of the pie chart
sizes = [dna,rna,protein,carbohydrate] #assignment statement
explode=(0,0,0,0) #no part of the pie chart will be away from the center
plt.title('The number of childNodes for DNA-related, RNA-related, protein-related and carbohydrate-related genes') #define the title of the pie chart
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%', #define relative parametres
        shadow= False, startangle=90)
plt.axis('equal')
plt.show() #print out the pie chart
