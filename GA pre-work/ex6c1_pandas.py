import pandas as pd

#load file1.csv as a DataFrame and print the result to screen
data = pd.read_csv('file1.csv')
print(data)
print()

#select only those rows where col1 is greater than 3 and print to screen
print(data[data.col1 > 3])
print()

#select only those rows where col3 is False and print to screen
print(data[data.col3 == False])
print()

#load file2.csv as a DataFrame object and print it to screen
data2 = pd.read_csv('file3.csv')
print(data2)

#left join data and data2 on col2, keeping all of data's values and print
#the resulting DataFrame to the screen
left_join_data = data.merge(data2, on="col2", how="left")
print(left_join_data)

#right join data and data2 on col2, keeping all of data2's values
right_join_data = data.merge(data2, on='col2', how='right')
print(right_join_data)
