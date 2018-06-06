import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

#*******************Column Operations*******************************

#Selecting a column
print ("\nSelecting a column:")
print(df['one'])

#Adding a new column
print ("\nAdding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)
print ("\nAdding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print(df)

#Deleting a column
print ("\nDeleting the first column using DEL function:")
del df['one']
print(df)

# using pop function
print ("\nDeleting another column using POP function:")
df.pop('two')
print(df)

#***********************Row Operations*******************************

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print("\n\n", df)

#Selecting a Row by label
print("\nSelecting a Row by label")
print(df.loc['b'])

#Selecting a Row by integer location
print("\nSelecting a Row by integer location")
print(df.iloc[2])

#Slice rows
print("\nSlice row 2-4")
print(df[2:4])

#Append rows
print("\nAppend row e")
df2 = pd.DataFrame({'one' : 5, 'two': 5}, index = ['e'])
df = df.append(df2)
print(df)

#Deleting row
print("\nDelete row d")
df = df.drop('d')
print(df)
