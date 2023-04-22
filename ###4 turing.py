###4 turing

import pandas as pd

# Load the dataset
df=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")

# Calculate the height at the 99th percentile
tallest_1_percent_height = df['height'].quantile(q=0.99)

print(f"The height of the tallest 1% of people is {tallest_1_percent_height:.2f} cm.")