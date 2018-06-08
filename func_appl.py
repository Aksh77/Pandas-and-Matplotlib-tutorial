import pandas as pd
import numpy as np

#Create dict with random numbers
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
s = pd.Series(np.random.randn(4))
print("DataFrame -")
print(df)
print("\nSeries -")
print(s)

#Table level Application - pipe()
print("\nTable level Application; add 2 to all elements -")
print(df.pipe(lambda x:x+2))

#Row or Column wise application - apply()
print("\nColumn wise max-min values -")
print(df.apply(lambda x: x.max() - x.min()))    #Default axis 0
print("\nRow wise mean-")
print(df.apply(np.mean, axis=1))

#Element wise application - applymap() and map()
print("\nElement wise Application on DataFrame; multiple each Element by 100 -")
print(df.applymap(lambda x:x*100))
print("\nElement wise Application on Series; multiple each Element by 10 -")
print(s.map(lambda x:x*10))
