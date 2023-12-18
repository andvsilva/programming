import pandas as pd
import feather

df = pd.read_csv('HR_COM1.CSV')
df.head()

print("saving the file format feather...")
# this is important to do before save in feather format.
df = df.reset_index(drop=True) 
df.to_feather('HR_COM1.ftr')