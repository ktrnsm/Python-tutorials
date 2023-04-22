###turing 8
import pandas as pd
from scipy.stats import ttest_ind



# Load the cardio_base and cardio_alco datasets
cardio_base = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")
cardio_alco = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_alco.csv")

merged_df = pd.merge(cardio_base, cardio_alco, left_index=True, right_index=True)

df=merged_df

smokers_bp = df[df['smoke'] == 1]['ap_hi']
non_smokers_bp = df[df['smoke'] == 0]['ap_hi']
t_stat, p_val = ttest_ind(smokers_bp, non_smokers_bp)

if p_val < 0.05:
    print("Smokers have higher blood pressure than non-smokers with 95% confidence.")
else:
    print("Smokers do not have higher blood pressure than non-smokers.")