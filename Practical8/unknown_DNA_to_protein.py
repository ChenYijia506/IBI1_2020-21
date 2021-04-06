import os
import re
#move to the directory which stores the fasta file
os.chdir('C:/Users/admin/Downloads/IBI/week 8')
#open and read the fasta file
f=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
f2=open('unknown_DNA_to_protein.fa','w')
lines=f.readlines()
#create new lists and a string to store extracted information
names=[]
seq=[]
DNA=''
protein_length=[]
#extract the names and DNA sequence of the unknown function genes
for i in range(len(lines)):
    if lines[i].startswith('>') and re.search(r'unknown function',lines[i]):
        name=str(re.findall(r'(>.+)_mRNA',lines[i]))
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
#import the codon table and translate the unknown function genes
for i in range(len(seq)):
    s=str(seq[i])
    protein=''
    table = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
 'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
 'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
 'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
    'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
 'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
 'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
 'TAT':'Y','TAC':'Y','TAA':'Y','TAG':'U',
 'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
 'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
 'GAT':'D','GAC':'D','GAA':'E','GAG':'E' 'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
 'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
 'AGT':'S','AGC':'S','AGA':'A','AGG':'R',
 'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}
    for x in range(0,len(seq[i])-2,3):
        protein=protein+table[s[x:x+3]]
#calculate the length of proteins
    l=len(protein)
    protein_length.append(l)
#put all the information together
x=''
for i in range(len(seq)):
    x=x+str(names[i])+' '+str(protein_length[i])+'\n'
f2.write(x)
f.close
f2.close
f2=open('unknown_DNA_to_protein.fa','r')
print(f2.read())

    

