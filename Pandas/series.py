#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

#empty Series
s1 = pd.Series()
print(s1)

#Series from ndArray
data2 = np.array(['a','b','c','d'])
s2 = pd.Series(data2)
print(s2)

#Series with index defined
data3 = np.array(['a','b','c','d'])
index3 = [100,101,102,103]
s3 = pd.Series(data3, index3)
print(s3)

#Series from dictionary
data4 = {'a' : 0., 'b' : 1., 'c' : 2.}
s4 = pd.Series(data4)
print(s4)
index5 = ['a', 'b', 'c', 'd']
s5 = pd.Series(data4, index5)
print(s5)

#Series from Scalar
s6 = pd.Series(5, index=[0, 1, 2, 3])
print(s6)

#retrieving data
print(s2[0])            #by default index
print(s3[101])          #by defined index
print(s4[:3])           #by slicing array
print(s5['a'])          #by key
print(s4[['a','b']])    #by list of indices/keys
