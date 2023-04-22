#turing 3


import pandas as pd

# Load the dataset
df=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")
# Calculate the percentage of smokers in each gender group

smokers_by_gender = df.groupby('gender')['smoke'].mean()

print(f"The percentage of smokers among men is {smokers_by_gender[2]*100:.2f}%, while the percentage of smokers among women is {smokers_by_gender[1]*100:.2f}%.")
