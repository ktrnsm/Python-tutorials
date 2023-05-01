#*dreamer
import pandas as pd
import glob

path = 'C:/Users/Şebnem/Desktop/ruyada/'
all_files = glob.glob(path + '*.csv')

data_list = []

for filename in all_files:
    data = pd.read_csv(filename, skiprows=1)
    data_list.append(data)

combined_data = pd.concat(data_list)

combined_data.columns = ['Town/City', 'Time', 'Value']
combined_data['Time'] = pd.to_datetime(combined_data['Time'], format='%Y-%m-%dT%H')
combined_data.set_index('Time', inplace=True)
weekly_data = combined_data.resample('W').sum()
weekly_data.to_csv('C:/Users/Şebnem/Desktop/tutorials/dream_data')

