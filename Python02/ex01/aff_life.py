from load_csv import load
import matplotlib.pyplot as plt


def aff_life(data, country):
    """Display the information arranged in a graph."""
    res = data[data['country'].str.contains(country)]
    years = [int(year) for year in res.keys() if year != "country"]
    values = [res[str(year)] for year in years]
    plt.figure(figsize=(8, 6))
    plt.plot(years, values, marker='', linestyle='solid')
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.grid(True)
    plt.show()
    return


def main():
    try:
        data = load("life_expectancy_years.csv")
        country = "France"
        aff_life(data, country)
        return
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
