###########################################################
### step  1 - loading dataset, preprocessing dataset
# 
# Add description for this code.
# Author: Your name here
# Contact me: name@email.com
###########################################################

# libraries for this project
import pandas as pd
import sys
import itertools
from collections import Counter
import numpy as np
import gc # Garbage Collector interface
import time
from icecream import ic # Never use print() to debug again, ic a high level for debug
import snoop # print the lines of code being executed in a function/ great feature very useful to debug :)
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

import toolkit as tool # see the file toolkit.py for more info
import feather

from icecream import ic

# Get start time 
start_time = time.time()

print('**********************************************')
print('Cleaning the dataset...')
print('**********************************************')

df = pd.read_csv('../datasets/HR_COM1.CSV')
print(f"Shape dataset Full:.........observations/rows: {df.shape[0]} and columns: {df.shape[1]}")

df['dept'] = df['dept'].astype('category')
df['salary'] = df['salary'].astype('category')

df = df.rename(columns={'satisfaction_level': 'satisfaction', 
                        'last_evaluation': 'evaluation',
                        'number_project': 'projectCount',
                        'average_montly_hours': 'averageMonthlyHours',
                        'time_spend_company': 'yearsAtCompany',
                        'Work_accident': 'workAccident',
                        'promotion_last_5years': 'promotion',
                        'sales' : 'dept',
                        'left' : 'turnover'
                        })

ic(df)
ic(df['dept'].value_counts(normalize=True).map('{:.2%}'.format))

# drop ID employeer
df = df.drop(columns=['Emp ID'])
#le = preprocessing.LabelEncoder()

#df['dept'] = le.fit_transform(df.dept.values)
#df['salary'] = le.fit_transform(df.salary.values)

ic(df)

# Save DataFrame to CSV without index
df.to_csv('../datasets/HR_COM1_cleaned.csv', index=False)

# time of execution in minutes
time_exec_min = round( (time.time() - start_time)/60, 4)

print(f'time of execution (preprocessing): {time_exec_min} minutes')
print("the preprocessing is done.")
print("The next step is to do the modeling.")
print("All Done. :)")