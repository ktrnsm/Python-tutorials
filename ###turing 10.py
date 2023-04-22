###turing 10
import pandas as pd
import numpy as np

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
covid_data = pd.read_csv("C:/Users/Şebnem/Desktop/tutorials/data/covid_data.csv")
data=covid_data

italy_data = data[(data.location == 'Italy') & (data.date >= '2020-02-28') & (data.date <= '2020-03-20')]

def exponential_func(x, a, b):
    return a * np.exp(b * x)

x = np.arange(len(italy_data))
y = italy_data.new_cases.cumsum()
popt, pcov = curve_fit(exponential_func, x, y)

plt.plot(x, y, label='Actual Data')
plt.plot(x, exponential_func(x, *popt), label='Fitted Curve')
plt.legend()
plt.show()

actual_cases = italy_data[italy_data.date == '2020-03-20'].new_cases.cumsum().values[0]
fitted_cases = exponential_func(len(x)-1, *popt)
difference = actual_cases - fitted_cases
print("Difference between actual cases and fitted curve on 2020-03-20:", difference)