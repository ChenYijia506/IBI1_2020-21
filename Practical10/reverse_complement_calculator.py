#reverse complement calculator
def complement(s):
    letters=list(s)
    complementary=''
    for i in range(0,len(letters)):
        table={'A':'T','T':'A','G':'C','C':'G','a':'T','t':'A','g':'C','c':'G'}
        if letters[i] in table:
            complementary=complementary+table[letters[i]]
    print(complementary)
def revcomplement(s): #define a function of reverse complement calculator
    letters=list(s) #change the DNA string into a list
    revcomplementary='' #create a new string to store information
    for i in range(0,len(letters)): #create a loop to calculate the reverse complement strand
        table={'A':'T','T':'A','G':'C','C':'G','a':'T','t':'A','c':'G','g':'C'} #import the translation table
        if letters[len(letters)-i-1] in table: #translate from the last base of the origin DNA strand
            revcomplementary=revcomplementary+table[letters[len(letters)-i-1]]
    print(revcomplementary) #print the reverse complement strand
s='AGGCTAgCcAT' #use an example to test the function
complement(s)
revcomplement(s)
