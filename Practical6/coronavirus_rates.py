frequency = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924} #make a frequency dictionary containing the information described in the table of the guidance

import matplotlib.pyplot as plt #import matplotlib 
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK' #name the labels shown in the pie chart
sizes = [29862124, 11285861, 11205972, 4360823, 4234924] #import the data shown in the table
explode = (0, 0, 0, 0, 0) 
plt.title('Total number of COVID-19 infections in five countries') #set the title of the pie chart
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90) #set relative parameters
plt.axis('equal')
plt.show() #print the pie chart
import numpy as np #import numpy
N = 5 #set the number of the columns
ind = np.arange(N)
sizes = (29862124, 11285861, 11205972, 4360823, 4234924) #import the total cases of five countries
Std = (2, 3, 4, 1, 2)
width = 0.35 
plt.title('frequency table for the total number of infections in five countries') #set the title of the bar chart
plt.xlabel('country') #set the x label
plt.ylabel('Frequency') #set the y label
plt.xticks(ind, ('USA', 'India', 'Brazil', 'Russia', 'UK')) #set the names of columns
p1 = plt.bar(ind, sizes, width, yerr=Std) #draw the bar chart
plt.show() #print the bar chart
