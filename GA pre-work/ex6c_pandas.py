import numpy as np
import pandas as pd

#df = pd.DataFrame(np.array([.25,10,600], [-0.9,40,200], [0.4,70,800], [0.8,50,300]), columns=["A","B","C"])
#df = pd.DataFrame(np.array([0.25,10,600], [-0.9,40,200], [0.4,70,800], [0.8, 50, 300]), columns=["A", "B", "C"])

#df = pd.DataFrame({"A": [0.25,10,600], "B": [-0.9,40,200], "C":[0.4,70,800], "D": [0.8, 50, 300]})
df = pd.DataFrame(np.array([[0.25,10,600], [-0.9,40,200], [0.4,70,800], [0.8, 50, 300]]), columns=["A", "B", "C"], index=[40,50,60,70])

print(df)               # Print the whole DF
print(df.dtypes)
print("\n\n")
print(df["B"])
print(df[["B"]])
print(df[["A","C"]])    # Print columns A and C by passing a list of column names
print(df.B)             # Print column B of df, by accessing the attribute
print(df.B[1:3])        # Print rows 1 and 2 of column B
print(df[1:3])          # Print rows 1 and 2
print(df.iloc[1])       # Print row 1
print(df.iloc[2:])      # Print rows 2 through to the end of the DF
print(df.iloc[1:3,1:])  # Print rows 1 and 2, and columns 1 through to the end of the DF
print(df.loc[50])       # Print row with index 50
print("\n\n\n")
print(df)               # Print df
print(df["A"] > 0)      # Print True or False for values of column A > 0
print(df[df["A"] > 0])  # Print subset of df i.e. data in df where value in column A > 0
print(df[df.A > 0])
print("\n\n\n")

#Split the df above at column B
dfa = df.iloc[:, :1]
dfa1 = df.iloc[:, 1:]
print(dfa)
print(dfa1)
print("\n\n\n")

#Split the df above at row 2
dfb = df.iloc[:2, :]
dfb1 = df.iloc[2:, :]
print(dfb)
print(dfb1)
print("\n\n\n")

df["D"] = [10, 20.0, 30, 40]
print(df)

df = df[["A", "C"]]     # Assign df to a the subset of data in columns A and C
print(df)
df.sort_values(by="A")
print(df)
df.sort_values(by="A", inplace = True)  # Sort df by column A inplace (i.e. modify df itself)
print(df)



print("\n\n\n")
# Create a new df with NaN
df2 = pd.DataFrame(np.array([[np.NaN,np.NaN,6.0], [-0.9,4.0,2], [0.4,np.NaN,0], [0.8, 5, 3]]), columns=["A", "B", "C"])
print(df2)
print(df2.dropna())         # Return data with rows that do no have NaN
print(df2)                  # df2 remains unchanged
df2.dropna(inplace = True)  # Drop data with rows containing NaN inplace and update df2
print(df2)

print("\n\n\n")

# Create df and add date to it
print("Joining DFs")
a_series = pd.Series(["Italy", "Thailand", "New Zealand", "Iceland"], index = ['A', 'B', 'C', 'D'])
df = pd.DataFrame({'Country' : a_series, 'Trips': [6, 4, 2, 1]})
print(df)
df['Expensive'] = [True, False, False, True]    # Add column to df
print(df)

df2 = pd.DataFrame(np.array([['USA', 8, True], ['Spain', 3, False]]), columns = ['Country', 'Trips', 'Expensive'])
print(df2)

print(f"DF1: \n{df} \nand DF2 \n{df2}")
print("\nAppending DF1 and DF2, by adding rows with the same column names")
print(df.append(df2))


df3 = pd.DataFrame(np.array([['Rome', 'Hot'], ['Bangkok', 'Tropical'], ['Auckland', 'Cool'], ['Reykavijc', 'Cold']]), columns = ['Capital', 'Climate'], index = ['A', 'B', 'C', 'D'])
print(df3)
print("\nAppending DF and DF3 by adding columns")
print(pd.concat([df, df3], axis = 1))


print("\n\n\n")
#df1 = pd.DataFrame(np.array([['Europe', 'UK', 100000], ['Europe', 'DE', 20000], ['Africa', 'Kenya', 40000], ['Africa', 'Morocco', 20000], ['Africa', 'Chad', 10000]]), columns=['Continent', 'Country', 'Pageviews'])
df1 = pd.DataFrame([['Europe', 'UK', 100000], ['Europe', 'DE', 20000], ['Africa', 'Kenya', 40000], ['Africa', 'Morocco', 20000], ['Africa', 'Chad', 10000]], columns=['Continent', 'Country', 'Pageviews'])
capitals = pd.DataFrame(np.array([['UK', 'London'], ['DE', 'Berlin'], ['Kenya', 'Nairobi'], ['Chad', 'N\'Djamena'], ['Italy', 'Rome']]), columns=['Country', 'Capital'])
print(df1)
print(capitals)
new_df = df1.join(capitals.set_index('Country'), on='Country')
print(new_df)

capitals = capitals.set_index('Country')
new_df1 = df1.join(capitals, on='Country')
print(new_df1)

print(new_df[new_df['Continent'] == 'Africa'])
print(new_df[new_df['Pageviews'] >= 10000])
print(new_df[(new_df['Continent'] == 'Africa') & (new_df['Pageviews'] > 10000)])
