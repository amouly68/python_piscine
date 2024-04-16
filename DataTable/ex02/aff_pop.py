from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter


def million_formatter(x, pos):
    """
    Add 'M' to the end of the number
    """
    return f"{int(x)}M"


def main():
    dataset = load("population_total.csv")
    comp = dataset[(dataset['country'] == 'France') |
                   (dataset['country'] == 'Belgium')]
    comp_transposed = comp.transpose()
    comp_transposed.reset_index(inplace=True)
    comp_transposed.columns = comp_transposed.iloc[0]
    comp = comp_transposed[1:].copy()
    comp = comp.rename(columns={'country': 'year'})
    comp['Belgium'] = pd.to_numeric(comp['Belgium'].str.replace('M', ''))
    comp['France'] = pd.to_numeric(comp['France'].str.replace('M', ''))
    comp['year'] = pd.to_numeric(comp['year'])
    comp = comp[comp['year'] <= 2050]
    comp.tail()

    plt.plot(comp['year'].values, comp['Belgium'].values, label='Belgium')
    plt.plot(comp['year'].values, comp['France'].values,
             label='France', color='green')

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xlim(1790, 2060)
    plt.xticks(range(1800, 2050, 40))
    formatter = FuncFormatter(million_formatter)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.yticks(range(20, 61, 20))

    plt.title('Population Projections')
    plt.legend(loc='lower right')

    plt.show()


if __name__ == "__main__":
    main()
