from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns


def main():
    expectancy = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    expectancy.set_index('country', inplace=True)
    expectancy_1900 = expectancy['1900']
    income.set_index('country', inplace=True)
    income_1900 = income['1900']
    data_1900 = pd.concat([expectancy_1900, income_1900],
                          axis=1, keys=['Life Expectancy', 'Income'])
    data_1900 = data_1900.dropna()

    # avec seaborn
    # ax = sns.scatterplot(x='Income', y='Life Expectancy', data=data_1900)
    # ax.set(xscale="log")
    # ax.set_xlim(300, 11000)
    # ax.set_xticks([300, 1000, 10000])
    # ax.set_xticklabels(['300', '1K', '10K'])
    # plt.title('1900')
    # plt.xlabel('Gross domestic product')
    # plt.ylabel('Life Expectancy')
    # plt.show()

    # avec plt
    plt.scatter(data_1900['Income'], data_1900['Life Expectancy'],
                c='blue')  # alpha pour la transparence
    plt.xscale('log')
    plt.xlim(300, 11000)
    plt.xticks([300, 1000, 10000], ['300', '1K', '10K'])
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.show()


if __name__ == "__main__":
    main()
