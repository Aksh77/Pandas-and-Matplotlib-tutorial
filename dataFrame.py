#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

#empty Series
df1 = pd.DataFrame()
print(df1)

#Data frame from list or list of lists
data2 = [['Alex',10],['Bob',12],['Clarke',13]]
df2 = pd.DataFrame(data2 ,columns=['Name','Age'])
print(df2)

#Data Frame from dictionary of ndArray/lists
data3 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df3 = pd.DataFrame(data3)
print(df3)

#Indexed Data Frame
data4 = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df4 = pd.DataFrame(data4, index=['r1','r2','r3','r4'])
print(df4)

#data frame from list of dictionaries
data5 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df5 = pd.DataFrame(data5, index=['first', 'second'], columns=['a', 'b', 'c'])
print(df5)

#Data frame from dictionary of Series
data6 = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df6 = pd.DataFrame(data6)
print(df6)
