###turing 6
import pandas as pd
import numpy as np

# Load the dataset
df=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")

# Calculate the mean and standard deviation of height
height_mean = df['height'].mean()
height_std = df['height'].std()

# Calculate the threshold for being more than 2 standard deviations away from the mean
threshold = height_mean + 2 * height_std

# Calculate the percentage of people who are more than 2 standard deviations away from the mean
percent_over_threshold = 100 * np.mean(df['height'] > threshold)

print(f"{percent_over_threshold:.2f}% of people are more than 2 standard deviations away from the average height.")
