#turing 2

import pandas as pd

# Load the dataset
df=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")

# Calculate age in years rounded down
df['age'] = (df['age'] / 365).astype(int)

# Create a new column indicating if the person is over 50 or not
df['over_50'] = (df['age'] > 50).astype(int)

# Calculate mean cholesterol levels for those over 50 and those under 50
mean_cholesterol = df.groupby('over_50')['cholesterol'].mean()

# Calculate the percentage difference in mean cholesterol levels
percent_diff = ((mean_cholesterol[1] - mean_cholesterol[0]) / mean_cholesterol[0]) * 100

print(f"The mean cholesterol level for those under 50 is {mean_cholesterol[0]:.2f} mg/dl, while the mean cholesterol level for those over 50 is {mean_cholesterol[1]:.2f} mg/dl.")
print(f"The percentage difference in mean cholesterol levels between those over 50 and those under 50 is {percent_diff:.2f}%.")


