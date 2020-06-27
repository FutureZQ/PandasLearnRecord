import numpy as np
import pandas as pd

# target of today is to run some basic command
# It Seem there are same intreasting feature in Series
df = pd.DataFrame({"工资": [10, 20, 30, 40],
                   "水平": [3, 1, 2, 2],
                   "非空测试": pd.Series([0, 1, 3])}, index=[0, 1, 2, 3])

# A simple select the first
df_head = df.head(1)

# Add a colum （it must have the same len with other colum
# expect with Series or single object which one will broadcast to whole line）
df['New'] = 1

# add one row
newrow = df[1:2][:]
print(pd.concat([df, newrow]))

# delete the colum
df.drop('New', axis=1, inplace=True)

# delete the row
df.drop(3, axis=0, inplace=True)


print(df)

# select the data
df_select = df[['工资', '水平']]
print(df_select)


# Same simple example to change the colum data
df['能力比']= (df['工资']+1) / (df['水平'] + 1)
print(df.head())


#same method to deal with Date
print(pd.to_datetime('2020-08-09'))

print(df['能力比'][1])
