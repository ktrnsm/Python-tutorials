###turing 7
import pandas as pd

# Load the cardio_base and cardio_alco datasets
cardio_base = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_base.csv")
cardio_alco = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/cardio_alco.csv")

merged_df = pd.merge(cardio_base, cardio_alco, left_index=True, right_index=True)

# Filter the dataset to include only individuals over 50 years old
over_50 = merged_df[merged_df['age'] > 50]

# Extract the "alco" column from the filtered dataset
alcohol_consumption = over_50['alco']

# Calculate the proportion of individuals who consume alcohol
proportion = alcohol_consumption.sum() / len(alcohol_consumption)

# Convert the proportion to a percentage
percentage = round(proportion * 100, 2)

# Print the result
print(f"The percentage of the population over 50 years old that consume alcohol is {percentage}%.")
