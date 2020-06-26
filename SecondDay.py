import numpy as np
import pandas as pd

df = pd.DataFrame({"工资": [10, 20, 30, 40],
                   "水平": [3, 1, 2, 2],
                   "非空测试": pd.Series([0, 1, 3])}, index=[0, 1, 2, 3])

# It seem that the method use [] to cut the data has some limitation
# It can't be ues to cut date discontinue
# print(df[:][0,2])

# The Method to cut data with [row,colnum]
print(df.iloc[:,[0,2]])

print(df.loc['工资':'非空测试',:]) # loc can use key

# #condition select
print( df.loc[df['水平'].isin([2,3]),:] )

# the different condition need ()
print(df.loc[
    (df['工资'] > 10) & 
	(df['水平'].isin([2, 3]))
	, :])
