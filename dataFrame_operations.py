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
