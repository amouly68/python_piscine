from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns

# def main():
dataset = load("population_total.csv")
dataset.head()

comp = dataset[(dataset['country'] == 'France') | (dataset['country'] == 'Belgium')]
comp.head()
comp_transposed = comp.transpose()
comp_transposed.head()
comp_transposed.reset_index(inplace=True)
comp_transposed.head()
comp_transposed.columns = comp_transposed.iloc[0]
comp_transposed.head()
comp = comp_transposed[1:].copy()
comp.head()
comp = comp.rename(columns={'country' : 'year'})
comp.head()
comp.set_index('year', inplace=True)
comp.head()
comp


sns.lineplot(data=comp)

plt.plot(comp['year'].values, comp['Belgium'].values, label='Belgium')
plt.plot(comp['year'].values, comp['France'].values, label='France')

plt.xlabel('Year')
plt.ylabel('Population')
plt.xlim(1800, 2040)
plt.xticks(range(1800, 2040, 40))
plt.title('Population Projections')
plt.legend()

plt.show()


if __name__ == "__main__":
    main()