###turing 9
import pandas as pd
covid_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/covid_data.csv")
df=covid_data

df = df[df['location'].isin(['Germany', 'Italy'])]

# pivot the table to create a new dataset with columns for Germany and Italy and date as index
df_new = df.pivot(index='date', columns='location', values='new_cases').reset_index()

# rename the columns
df_new.columns = ['date', 'Germany', 'Italy']

# print the new dataset
print(df_new)