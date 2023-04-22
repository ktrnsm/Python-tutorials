###turing 12
import pandas as pd

covid_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/covid_data.csv")
data=covid_data
# Calculate death rate
data['death_rate'] = data['new_deaths'] / data['population'] * 1e6

# Identify countries with population over 65 years old
data['over_65'] = data['aged_65_older_percent'].astype(bool) & (data['aged_65_older_percent'] > 20)

# Identify countries with death rate over 50 per million inhabitants
data['high_death_rate'] = data.loc[data['population'].notnull() & data['death_rate'].notnull(), 'death_rate'] > 50

# Calculate precision, recall, and F1 score
true_positives = len(data.loc[data['over_65'] & data['high_death_rate']])
false_positives = len(data.loc[~data['over_65'] & data['high_death_rate'].notna()])
false_negatives = len(data.loc[data['over_65'] & (data['high_death_rate'].isna() | ~data['high_death_rate'].fillna(False))])

# Prevent division by zero error
if true_positives + false_positives == 0:
    precision = 0
else:
    precision = true_positives / (true_positives + false_positives)

# Prevent division by zero error
if true_positives + false_negatives == 0:
    recall = 0
else:
    recall = true_positives / (true_positives + false_negatives)

# Prevent division by zero error
if precision + recall == 0:
    f1_score = 0
else:
    f1_score = 2 * precision * recall / (precision + recall)

# Print the results
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 score: {f1_score:.2f}')