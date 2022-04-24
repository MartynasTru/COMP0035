
# Imports
from matplotlib.legend import Legend
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Closing all the windows before opening new ones
plt.close("all")

# Opening file from the CourseWork1 folder
df = pd.read_csv('PreparedDataWithAreas.csv')

#North East
graph_ne = df[['Year', 'North East']]
graph_ne.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in North East')
plt.savefig('results/NorthEast.png', bbox_inches = 'tight')

#Nort West
graph_nw = df[['Year', 'North West']]
graph_nw.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in North West')
plt.savefig('results/NorthWest.png', bbox_inches = 'tight')

#Yorkshire and the Humber
graph_york = df[['Year', 'Yorkshire and The Humber']]
graph_york.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in Yorkshire and The Humber')
plt.savefig('results/YorkshireHumber.png', bbox_inches = 'tight')

#East Midlands
graph_em = df[['Year', 'East Midlands']]
graph_em.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in East Midlands')
plt.savefig('results/EastMidlands.png', bbox_inches = 'tight')

#West Midlands
graph_wm = df[['Year', 'West Midlands']]
graph_wm.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in West Midlands')
plt.savefig('results/WestMidlands.png', bbox_inches = 'tight')

#East
graph_east = df[['Year', 'East']]
graph_east.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in East')
plt.savefig('results/East.png', bbox_inches = 'tight')

# London
graph_london = df[['Year', 'London']]
graph_london.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in London')
plt.savefig('results/London.png', bbox_inches = 'tight')

# South East
graph_se = df[['Year', 'South East']]
graph_se.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in South East')
plt.savefig('results/SouthEast.png', bbox_inches = 'tight')

# South West
graph_sw = df[['Year', 'South West']]
graph_sw.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in South West')
plt.savefig('results/SouthWest.png', bbox_inches = 'tight')

# England
graph_eng = df[['Year', 'England']]
graph_eng.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in Endland')
plt.savefig('results/England.png', bbox_inches = 'tight')

#Wales
graph_wales = df[['Year', 'Wales']]
graph_wales.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in Wales')
plt.savefig('results/Wales.png', bbox_inches = 'tight')

# Scotland
graph_sc = df[['Year', 'Scotland']]
graph_sc.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in Scotland')
plt.savefig('results/Scotland.png', bbox_inches = 'tight')

#Great Britain
graph_gb = df[['Year', 'Great Britain']]
graph_gb.plot()
plt.xlabel('Measure Points')
plt.ylabel('Number of Licenses')
plt.title('Car licensing in Great Britain')
plt.savefig('results/GreatBritain.png', bbox_inches = 'tight')
#plt.show()


# Drawing all the areas that i have data about and saving plotted graphs 
# in a folder 'results'. 











