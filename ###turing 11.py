###turing 11
import pandas as pd

covid_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/covid_data.csv")
data=covid_data
# Calculate the death rate
data['death_rate'] = (data['new_deaths']* 1000000 / data['population']) 

# Sort the data frame by death rate in descending order
data = data.sort_values('death_rate', ascending=False)

# Select the location with the third highest death rate
third_highest_country = data.iloc[0:50]['location']

print(f"The country with the 3rd highest death rate is {third_highest_country}.")