from load_csv import load
import matplotlib.pyplot as plt

def main():
    dataset = load("life_expectancy_years.csv")
    dataset.head()
    france_data = dataset[dataset['country'] == 'France']
    france_data_transposed = france_data.transpose()
    #drop the first row
    france_data = france_data_transposed[1:].copy()
    france_data.columns = france_data_transposed.iloc[0]
    #rename the first column
    france_data.rename(columns={france_data.columns[0]: 'Expectancy'}, inplace=True)
    france_data.reset_index(inplace=True)
    france_data.rename(columns={'index': 'Year'}, inplace=True)



    plt.plot(france_data['Year'].values, france_data['Expectancy'].values, label='France')
    plt.title('France Life Expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(france_data['Year'].values[::40])
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 100, 10))
    # plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()