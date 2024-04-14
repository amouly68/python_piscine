from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns

df = load("life_expectancy_years.csv")

df = df.transpose()
df.columns = df.iloc[0]
df.head()
df = df[1:]
df.head()
