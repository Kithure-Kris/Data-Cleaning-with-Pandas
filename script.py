import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

#Dealing with multiple files
files = glob.glob('states*.csv')
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

#Diagnose the data
print(us_census.head())
print(us_census.columns)
print(us_census.dtypes)

#String Parsing
us_census['Income'] = us_census['Income'].replace('[\$]', '', regex=True)
#Dtype conversion
us_census.Income = pd.to_numeric(us_census.Income)

#Splitting string by character
str_split = us_census.GenderPop.str.split('_')
us_census['MalePop'] = str_split.str.get(0)
us_census['FemalePop'] = str_split.str.get(1)
print(us_census.head())

us_census['MalePop'] = us_census['MalePop'].replace('(M)', '', regex=True)
us_census['MalePop'] = pd.to_numeric(us_census['MalePop'])
us_census['FemalePop'] = us_census['FemalePop'].replace('(F)', '', regex=True)
us_census['FemalePop'] = pd.to_numeric(us_census['FemalePop'])
print(us_census.head())
print(us_census.dtypes)

#Dealing with missing data
us_census['FemalePop'] = us_census['FemalePop'].fillna(us_census.TotalPop - us_census.MalePop)
print(us_census.FemalePop)

#Checking for Duplicates
duplicates = us_census.duplicated()
print (duplicates)
#Drop duplicates
us_census = us_census.drop_duplicates()

#Scatter Plot
plt.scatter(us_census.FemalePop, us_census.Income)
plt.show()