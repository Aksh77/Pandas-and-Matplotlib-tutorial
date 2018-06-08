import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
print (df)

#Sum of values
print("\nSum values -")
print(df.sum())

#Mean value
print("\nMean values -")
print(df.mean())

#Standard Deviation -
print("\nStandard Deviations -")
print(df.std())

#Summarize numeric Data
print("\nSummary of numeric data - ")
print(df.describe(include='number'))
#print(df.describe()) Default value of include is number

#Summarise string Data
print("\nSummary of string data -")
print(df.describe(include='object'))

#Summarise all Data
print("\nFull summary -")
print(df.describe(include='all'))
