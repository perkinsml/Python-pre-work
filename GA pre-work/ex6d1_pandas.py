import pandas as pd

#load file6d.csv as a DataFrame and print the result to screen
data = pd.read_csv('file6d.csv')
print(data)
print()

#get overall sense of data by getting numeric summary info of numeric columns using .describe()
print(data.describe())

#get distribution of non-numeric columns using .value_counts() on col2 and col3
print(data.col2.value_counts())
print(data.col3.value_counts())

print("\n\n\n")

#get the mean of col1 grouped by col2
print(data.groupby('col2').col1.mean())
print(data.groupby('col2')['col1'].mean())

#get the mean of col1 grouped by col3
print(data.groupby('col3').col1.mean())

#pivot data into a new table where col2 is the index,
#col3's values are the individual columns, and the average value in
#col1 is the value in each cell
pivot_data = pd.pivot_table(data, index=["col2"], values=["col1"], columns=["col3"], aggfunc='mean', fill_value=0)
print(pivot_data)
