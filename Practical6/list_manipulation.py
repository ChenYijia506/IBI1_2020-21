import numpy as np #import numpy
gene_lengths = [9410,394141,4442,105338,19149,76779,126550,36296,842,15981] #the purpose of the following four comands is to create some variables, endow them with value and prepare for the calculation
a = np.array(gene_lengths)
exon_counts = [51,1142,42,216,25,650,32533,57,1,523]
b = np.array(exon_counts)
X = a/b #do the calculation to get average exon lengths
X = list(X) #As X is considered as 'numpy.ndarray' now, change X to a list
X.sort() #change X into a sorted list

import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib
n = 10 #set the total number of variables
score = X #import the sorted list of the average exon lengths in order to draw the boxplot
plt.boxplot(score,
            vert = True,
            whis = 1.5,
            patch_artist = False,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
            ) #draw the boxplot
plt.show() #print the boxplot
