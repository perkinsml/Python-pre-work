import pandas as pd

#a_series = pd.Series([10, 20, 30], index = [2012, 2013, 2014])
a_series = pd.Series([10, 20, 30, 40])
a_series.name = "My first Pandas series"
print(a_series)
print(type(a_series))

b_series = pd.Series(["Italy", "Thailand", "New Zealand", "Iceland"], index = ['A', 'B', 'C', 'D'])
#b_series = pd.Series(["Italy", "Thailand", "New Zealand", "Iceland"])
b_series.name = "My favourite countries"
print(b_series)


a_df = pd.DataFrame({'Countries' : b_series, 'Trips': [6, 4, 2, 1]})
a_df.name = "Countries with number of trips"
print(a_df.name)
print(a_df)
print(type(a_df))

#load file1.csv as a DataFrame and print the result to screen
data = pd.read_csv('file1.csv')
print(data)

#print just the first few rows using .head()
print(data.head())

#examine data to see what types its columns are
print(data.dtypes)

#check the object's type
print(type(data))

#load file2.csv as a Series object and print it to screen
data2 = pd.read_csv('file2.csv', squeeze = True)
print(data2)

#check data2's type
print(type(data2))
