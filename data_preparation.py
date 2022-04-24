
import pandas as pd
import openpyxl as op

# Opening the file
df = pd.read_excel('DataPointsWithAreas.xlsx', sheet_name='VEH0104a_All',
skiprows=6)

# Selecting just the needed columns out of other 14
# Can re-select by adding/removing comments at the areas
df = df.loc[:, ["Year", 
"North East", 
"North West",
"Yorkshire and The Humber",
"East Midlands",
"West Midlands",
"East",
"London",
"South East",
"South West",
"England",
"Wales",
"Scotland",
"Great Britain",
]]


# Removing rows that contain links or any other irrelevant information
df = df.drop(labels = [67,68,69,70,71,72,73], axis = 0)
# Removing any blans rows that are left. Small removal of data wont have affect on wide DataFrame
df = df.dropna()

# Print the first 65 rows of data
print(df.head(65))

# Print the column labels
print(df.columns)

# Print the column labels and data types
print(df.info(verbose=True))

#Saving the file to .csv format
# I have decided to work with csv files because it can be easily looked through
# at IDE. Moreover, data exploration code was written for .xslx, however,
# it contained errors that i was only able to solve through changing format of 
# file to the .csv. In addition to this it can be seen on GitHub which makes it 
# easier to quickly look at and assess.
df.to_csv('PreparedDataWithAreas.csv', encoding='utf-8', index=False)

#Re-checking how the output looks in the end
print(df)







