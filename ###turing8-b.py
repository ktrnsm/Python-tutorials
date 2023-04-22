###turing8-b

import pandas as pd
from scipy.stats import chi2_contingency

cardio_base = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")
cardio_alco = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_alco.csv")

merged_df = pd.merge(cardio_base, cardio_alco, left_index=True, right_index=True)

df=merged_df

smokers_cholesterol = df[df['smoke'] == 1]['cholesterol']
non_smokers_cholesterol = df[df['smoke'] == 0]['cholesterol']

contingency_table = pd.crosstab(df['smoke'], df['cholesterol'])

chi2_stat, p_val, _, _ = chi2_contingency(contingency_table)

if p_val < 0.05:
    print("Smokers have higher cholesterol level than non-smokers with 95% confidence.")
else:
    print("Smokers do not have higher cholesterol level than non-smokers.")