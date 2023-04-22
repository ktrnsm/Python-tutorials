import pandas as pd
df=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")

# Calculate age in years rounded down
df['age'] = (df['age'] / 365).astype(int)

# Calculate average weight by age group
age_weight = df.groupby('age')['weight'].mean()

# Find the age group with the highest average weight
max_age = age_weight.idxmax()

# Find the age group with the lowest average weight
min_age = age_weight.idxmin()

# Calculate the weight difference between the two age groups
weight_diff = age_weight[max_age] - age_weight[min_age]

# Calculate the percentage difference relative to the average weight of the age group with the lowest weight
percent_diff = (weight_diff / age_weight[min_age]) * 100

print(f"The age group with the highest average weight ({age_weight[max_age]:.2f} kg) is {max_age} years old, while the age group with the lowest weight ({age_weight[min_age]:.2f} kg) is {min_age} years old.")
print(f"The weight difference between the two age groups is {weight_diff:.2f} kg.")
print(f"This represents a {percent_diff:.2f}% increase relative to the average weight of the age group with the lowest weight.")

