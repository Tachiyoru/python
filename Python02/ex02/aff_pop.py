from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def convert_population(population):
    if population.endswith("M"):
        return float(population[:-1]) * 1_000_000
    elif population.endswith("k"):
        return float(population[:-1]) * 1_000
    else:
        return float(population)


def millions_formatter(x, pos):
    return f'{x / 1e6:.0f}M'


def aff_pop(data, country, c2):

    if country in data['country'].values and c2 in data['country'].values:
        res = data[data['country']==country].drop('country', axis=1).T
        res2 = data[data['country']==c2].drop('country', axis=1).T
        res = res.loc['1800':'2050']
        res2 = res2.loc['1800':'2050']
        res = res.squeeze().apply(convert_population)
        res2 = res2.squeeze().apply(convert_population)
        res.index = res.index.astype(int)
        res2.index = res2.index.astype(int)

        plt.figure(figsize=(8, 6))
        plt.plot(res, label=country)
        plt.plot(res2, label=c2)

        plt.title(f"{country} and {c2} Population comparison")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend([country, c2], loc='lower right')

        formatter = FuncFormatter(millions_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)

        plt.show()
    return


def main():
    data = load("population_total.csv")
    if data is not None:
        country = "France"
        country2 = "Belgium"
        aff_pop(data, country, country2)
    return


if __name__ == "__main__":
    main()