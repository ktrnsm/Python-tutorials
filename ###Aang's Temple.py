###Aang's Temple
import numpy as np
import pandas as pd

# Define the number of rows for the dataset
num_rows = 250

# Define the range and distribution of values for each variable
avg_temp = np.random.normal(20, 10, num_rows) # mean=20, std=10
altitude = np.random.uniform(0, 5000, num_rows) # range from 0 to 5000 meters
landform = np.random.choice(['mountain', 'valley', 'plateau', 'glacier', 'hill', 'loess', 'plain', 'desert'], size=num_rows)
avg_pressure = np.random.normal(1013, 100, num_rows) # mean=1013 hPa, std=100 hPa
surface_area = np.random.uniform(100, 10000, num_rows) # range from 100 to 10000 km^2
suitable_for_temple = np.random.choice(['Yes', 'No'], size=num_rows, p=[0.8, 0.2])

# Create a dataframe to store the data
data = pd.DataFrame({
    'Average Temperature': avg_temp,
    'Altitude': altitude,
    'Landform': landform,
    'Average Pressure': avg_pressure,
    'Surface Area': surface_area,
    'Suitable for Temple': suitable_for_temple
})

# Check the first few rows of the dataset
print(data.head())

