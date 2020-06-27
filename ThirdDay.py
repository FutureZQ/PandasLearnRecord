import numpy as np
import pandas as pd

df=pd.read_excel('data.xlsx')

df1 = df.iloc[0:10,:]
df2 = df.iloc[15:20,:]

###################### Add ###########################
# add row 
df3 = pd.concat([df1,df2])

#table merge
t1 = pd.DataFrame(
	{
		"语文":[90,80,60,70],
		"数学":[100,100,60,59],
		"英语":[70,80,60,100]
	},index=['张三','李四','赵五','王二']
)

t2 =  pd.DataFrame(
	{
		"体育":[90,80,60,70],
		"化学":[100,100,60,59],
	},index=['张三','孙磊','赵五','韩梅梅']
)


# right_index and left_index indicate that the two table connect wiht index(Name)
df_out = pd.merge(left = t1, right = t2,left_index = True,right_index = True,how = 'left')
print(df_out)
print('left merge\n')


df_out = pd.merge(left = t1, right = t2,left_index = True,right_index = True,how = 'right')
print(df_out)
print('right merge\n')

df_out = pd.merge(left = t1, right = t2,left_index = True,right_index = True,how = 'inner')
print(df_out)
print('inner merge\n')


df_out = pd.merge(left = t1, right = t2,left_index = True,right_index = True,how = 'outer')
print(df_out)
print('outer merge\n')



############ Drop #############

df_noNaN = df_out.dropna(inplace = False)
print(df_noNaN)

df_noNaN = df_out.dropna(subset = ['体育'],inplace = False)
print(df_noNaN)


df_duplicate = pd.concat( [df_out,df_out.iloc[0:2] ])
print(df_duplicate)
print(df_duplicate.drop_duplicates(subset = ['语文'],inplace = False ,keep = 'last'))


############ Search #############

# top
df_sort = df_out.sort_values(['语文'],ascending = False) 
print(df_sort)


############ cut #############
df_process = df_out.fillna(0)
df_process['总分'] = df_process['语文'] + df_process['数学'] + df_process['英语'] + df_process['体育'] + df_process['化学']

print(df_process)

#Where property right mean [) or []
df_process['等级'] = pd.cut(x = df_process['总分'],bins = [0,100,200,300,400,500],right = False,labels = ['E','D','C','B','A'])

print(df_process)