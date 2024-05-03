import matplotlib.pyplot as plt
from load_csv import load


def draw_projection_for_year(year: str):
    """
    Draw a scatter plot of life expectancy vs GNP per capita for a given year.
    Args:
        year (str): The year for which the data will be plotted.
    Returns:
        None
    """
    data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")

    if data is not None and life_expectancy_data is not None:
        gnp_year = data[['country', year]]
        life_exp_year = life_expectancy_data[['country', year]]
        merged_data = gnp_year.merge(life_exp_year, on='country', how='inner')
        merged_data.columns = ['Country', 'GNP', 'Life Expectancy']

        plt.figure(figsize=(10, 6))
        plt.scatter(merged_data['GNP'], merged_data['Life Expectancy'])

        plt.title(f'Life Expectancy vs GNP for Year {year}')
        plt.xlabel('GNP per Capita')
        plt.xscale('log')
        plt.xticks([1000, 10000], ['1k', '10k'])
        plt.ylabel('Life Expectancy')

        plt.show()

    else:
        print("Unable to load one or both datasets.")


if (__name__ == "__main__"):
    draw_projection_for_year('1900')
