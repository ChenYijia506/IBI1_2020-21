frequency = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924} #make a frequency dictionary containing the information described in the table of the guidance

import matplotlib.pyplot as plt #import matplotlib 
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK' #name the labels shown in the pie chart
sizes = [29862124, 11285861, 11205972, 4360823, 4234924] #import the data shown in the table
explode = (0, 0, 0, 0, 0) 
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90) #set relative parameters
plt.axis('equal')
plt.show() #print the pie chart
