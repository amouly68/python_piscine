from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter
import seaborn as sns

expectancy = load("life_expectancy_years.csv")
income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
expectancy.head()
expectancy.set_index('country', inplace=True)
expectancy.head()
expectancy_1900 = expectancy['1900']
expectancy_1900.head()
income.set_index('country', inplace=True)
income_1900 = income['1900']
income_1900.head()
data_1900 = pd.concat([expectancy_1900, income_1900], axis=1, keys=['Life Expectancy', 'Income'])
data_1900.head()
data_1900 = data_1900.dropna()
data_1900.head()
plt.scatter(data_1900['Income'], data_1900['Life Expectancy'], c='blue')  # alpha pour la transparence
plt.title('1900')
plt.xlabel('Gross domestic product')
plt.xscale('log')
plt.xlim(300, 11000)
plt.xticks([300, 1000, 10000], ['300', '1K', '10K'])
plt.ylabel('Life Expectancy')
plt.show()