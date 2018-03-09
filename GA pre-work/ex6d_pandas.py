import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([[.25,"w",60], [-.9,"x",20], [.2,"y",700], [.6,"z",350]]), columns=["A","B","C"])
df1 = pd.DataFrame([[.25,"w",60], [-.9,"x",20], [.2,"y",700], [.6,"z",350]], columns=["A","B","C"])

print(df)
print(df.shape)
print(df.dtypes)                # Every column is type object

#df["A"] = pd.to_numeric(df.A)   # Convert column A to numeric --> float
df["A"] = pd.to_numeric(df.A)
df["C"] = pd.to_numeric(df.C)   # Convert column C to numeric --> int
print(df.dtypes)
df["A"] = df.A.astype('str')    # Convert column A to a string
df["C"] = df.C.astype('float64') # Convert column C to a float
print(df.dtypes)

print("\n\n\n")

df = pd.DataFrame(np.array([[10.4,"w",60], [30.7,"x",20], [70.5,"y",70], [30.7,"z",35]]), columns=["A","B","C"])
df["A"] = df.A.astype('float64') # Correct data types
df["C"] = df.C.astype('int64')  # Correct data types
print(df)
print(df.C.mean())               # Print the mean of column C
print(df.mean())

print("\n\n\n")

df1 = pd.DataFrame(np.array([[10.4,"w",60], [30.7,"x",np.NaN], [70.5,"y",70], [30.7,"z",35]]), columns=["A","B","C"])
df1["A"] = df1.A.astype('float64') # Correct data types
df1["C"] = pd.to_numeric(df1.C, errors = 'coerce') # Correct data types
print(df1)
print(df1.dtypes)
print(df1.count())
print(df1.C.value_counts())
print(df1.describe())

print("\n\n\n")
print("\n\n\n")

print("The Split-Apply-Combine Paradigm")

df = pd.DataFrame([["Europe", "UK", 100000], ["Europe", "DE", 20000], ["Africa", "Kenya", 40000], ["Africa", "Morocco", 20000], ["Africa", "Chad", 10000]], columns=["Continent","Country","Pageviews"])
print(df)
print(df.dtypes)
print(f"Average number of page views is: {df.Pageviews.mean()}")

print(df.groupby('Continent').Pageviews.mean())
print(df.groupby('Continent').Pageviews.median())
print(df.groupby('Continent').Pageviews.sum())
print(df.groupby('Continent').Pageviews.min())
print(df.groupby('Continent').Pageviews.max())
print(df.groupby('Continent').describe())

print("\n\n\n")
print("\n\n\n")

print("Now, for pivot tables!")
print(f"DF: \n {df}")
print(df.groupby('Continent').Pageviews.mean())

# Group by Continent and calculate the mean for each column in the DF
print(pd.pivot_table(df, columns="Continent", aggfunc=[np.mean]))
# Group by continent and count the non-NaNs for each column
print(pd.pivot_table(df, columns="Continent", aggfunc=[len]))
# Group by continent and sum each column
print(pd.pivot_table(df, columns="Continent", aggfunc=[sum]))
print(pd.pivot_table(df, columns="Continent", aggfunc=[np.std]))
