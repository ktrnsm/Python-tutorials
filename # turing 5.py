# turing 5
import pandas as pd

# Load the dataset
df=pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")

# Calculate the Spearman correlation coefficients
spearman_corr = df.corr(method='spearman')

# Sort the correlation matrix and find the highest coefficients
sorted_corr = spearman_corr.unstack().sort_values(ascending=False)
highest_corr = sorted_corr[sorted_corr != 1.0].head(1)

# Extract the feature names from the index of the correlation coefficient
feature_1, feature_2 = highest_corr.index[0]

print(f"The two features with the highest Spearman rank correlation are: {feature_1} and {feature_2}")