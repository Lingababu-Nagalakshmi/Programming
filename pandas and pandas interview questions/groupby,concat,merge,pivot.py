#How to Read .csv data
#comma seperated value

import pandas as pd

df = pd.read_csv(r"C:\Users\ASUS\Desktop\Programming\Place_for_supported_files_for_coading\enq.csv")
print(df)


print(df.head())

print(df.head(3))

print(df.tail(3))

print(df[2:8:2])

print(df.columns)

print(df.shape)

print(df['Name'])

print(df[['Name','City']])

r,c = df.shape
print('Rows = :',r,' Columns = :',c)


print(type(df))

print(type(df['Name']))

print(df[['Fee','Name']])



print(df['Fee'] [df['Fee'] >=100])

