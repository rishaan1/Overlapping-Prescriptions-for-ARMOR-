#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.DataFrame(columns=['Ingredient','start date', 'end date'], data=[['B', '10-20-2018', '10-30-2018'],['A', '10-15-2018', '10-25-2018']])
df["Days"] = df.apply(lambda row: pd.date_range(start=row["start date"], end=row["end date"], freq="D"), axis=1)

#df['end date'] = pd.to_datetime(df['end date'])

table = dict()
for _, row in df.iterrows():
    for i in pd.date_range(start=row["start date"], end=row["end date"], freq="D"):
        if not i in table:
            table[i] = [row['Ingredient']]
        else:
            table[i].append(row['Ingredient'])

table = sorted(list(table.items()), key = lambda x:x[0])

print(table)
i = 0
result = pd.DataFrame(columns=['Regimen', 'end date'])
prev_ingredient = table[0][1]
start_date = table[0][0]
while (i < len(table)):
    if table[i][1] != prev_ingredient:
        result.loc[start_date] = ['+'.join(prev_ingredient), table[i-1][0]]
        #print(result)
        prev_ingredient = table[i][1]
        start_date = table[i][0]
    
    i+=1
result.loc[start_date] = ['+'.join(prev_ingredient), table[i-1][0]]
  
print(result)     
    
    
#test = df.groupby('Ingredient')['Days'].apply(list).to_dict()
#print(test)
print("\n")
print("\n")
print("\n")
#for key in test.keys():
    #print(key)
     
df2 = pd.DataFrame(columns=['Regimen','start date', 'end date'], data=[['A', '10-15-2018', '10-19-2018'], ['A+B', '10-20-2018', '10-25-2018'], ['B', '10-26-2018', '10-30-2018']])


#print(df2)


# In[ ]:




