import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/admin/Desktop/IBI1_2020-21/Practical7")
covid_data = pd.read_csv("full_data.csv") #line 1-6: the code for importing the .csv file
covid_data.iloc[0:12:2,0:5] #the code for showing all columns, and every second row between (and including) 0 and 10
Afghanistan = [] #create a list
for i in range(0,7996):
if covid_data.iloc[i,1]=="Afghanistan":
Afghanistan.append(True)
else: Afghanistan.append(False) #use Boolean to endow the variables with True or False
covid_data.loc[Afghanistan,"total_cases"] #print all the rows whose column of location is Afghanistan
covid_data[covid_data.location == "World"] #the code to compute the mean and median of new cases for the entire world
world_new_cases = covid_data.iloc[7880:7972,[0,2]]
world_new_cases.describe()
world_new_cases = covid_data.loc[7880:7971,"new_cases"] #create a new object for following manipulation
n = 92 #import the total number of variables
plt.xlabel('world') #the following three lines are to label the plot
plt.ylabel('world new cases')
plt.title('boxplot of new cases worldwide')
plt.boxplot(world_new_cases, #the code to create a boxplot of new cases worldwide
	    vert = True,
	    whis = 1.5,
	    patch_artist = False,
	    meanline = True,
	    showcaps = True,
	    showfliers = True,
	    notch = False
	    )
plt.show()
world_dates = covid_data.loc[7880:7971,"date"] #create a new object for following manipulation
world_new_cases = covid_data.loc[7880:7971,"new_cases"]
plt.xlabel('dates') #the following three lines are to label the plot
plt.ylabel('world new cases')
plt.title('new cases worldwide over time')
plt.plot(world_dates, world_new_cases, 'b+') #the code to plot new cases worldwide
plt.xticks(range(0,92,7)) #codes to make the plot more clear
plt.xticks(rotation=40)
plt.show()
world_new_deaths = covid_data.loc[7880:7971,"new_deaths"] #the code to plot new deaths worldwide
plt.xlabel('dates') #the following three lines are to label the plot
plt.ylabel('world new deaths')
plt.title('new deaths worldwide over time')
plt.plot(world_dates, world_new_new_deaths, 'ro') #the code to plot new deaths worldwide
plt.xticks(range(0,92,7)) #codes to make the plot more clear
plt.xticks(rotation=40)
plt.show()
Spain_dates = covid_data.loc[6720:6811,"date"] #the code to answer the question stated in the file question.txt
Spain_newcases = covid_data.loc[6720:6811,"new_cases"] #the following two lines are to create new objects for manipulation
Spain_totalcases = covid_data.loc[6720:6811,"total_cases"]
plt.xlabel('date') #the following three lines are to label the plot
plt.ylabel('infected number')
plt.title('new cases and total cases in Spain')
plt.plot(Spain_dates,Spain_newcases,'b+', label = "new cases") #the codes to create a plot to answer the question stated in the file question.txt
plt.plot(Spain_dates,Spain_totalcases,'ro', label = "total cases")
plt.legend(loc=(1,1)) #make a legend to make the plot more clear
plt.xticks(range(0,92,7)) #codes to make the plot more clear
plt.xticks(rotation=40)
plt.show()
