import pandas as pd

# This uses table1.csv and table2.csv

t1 = pd.read_csv("table1.csv")
t2 = pd.read_csv("table2.csv")
print("Printing both tables separately")
print("Table 1")
print(t1)
print()
print("Table 2")
print(t2)
print()

# Let us join the two tables with respect to user_id attribute. Like natural join.
m = pd.merge(t1, t2, on="user_id")  # join operation of t1 and t2 on the attribute user_id,
# you can also join on more than one attribute
# you can also do t1.merge(t2, on="user_id")
print()
print("Printing joined table")
print(m)
