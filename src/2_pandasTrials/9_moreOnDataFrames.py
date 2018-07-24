import pandas as pd
from datetime import datetime

# uses international-airline-passengers.csv

# dont pass in the header argument in read_csv() as by default, pandas reads the header
# also we want to skip the three last rows, therefore skipfooter=3
# skipfooter does not work with the default engine which is in C, therefore we use engine in "python"
df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
print(df.columns)  # shows the column names, let's rename it
print("Renaming column names")
df.columns = ["month", "passengers"]

print("New column names are ")
print(df.columns)

print("Printing only passengers ie 2nd column")
print(df['passengers'])
print()
# alternative method
print(df.passengers)
# this would not have worked if the column name had spaces in it as it will not be a valid identifier

# add a new column of ones to the data
df['ones'] = 1

# checking if it worked by using head()
print(df.head())

# What if we want to put a new column with it's value a derived value from the rest of the table?
# For that we use the apply function

# example
# df['c1c2'] = df.apply(lambda row: row['x1'] * row['x2'], axis=1)
# axis is specified since it should happen across row instead of column
# you can use a defined function instead of a lambda as well

# def get_interaction(row):
#     return row['x1'] * row['x2'] # where x1 and x2 are the column names
#
# df['x1x2'] = df.apply(get_interaction, axis=1)

# Testing datetime
# print(datetime.strptime("1857-01", "%Y-%m"))  # Yeah, it works

df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
print(df.head())
