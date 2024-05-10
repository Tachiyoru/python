import numpy as np


def ft_statistics(*args: any, **kwargs: any) -> None:
    """take in *args a quantity of unknown number and print the Mean, Median,
    Quartile (25% and 75%), Standard Deviation and Variance
    according to the **kwargs"""
    if not args:
        return print("No arguments")
    if not all(isinstance(arg, (int, float)) for arg in args):
        return print("All arguments must be of type int or float")
    if not kwargs:
        return print("No kwargs")
    kwarg = ("mean", "median", "quartile", "std", "var")
    if not all(key in kwarg for key in kwargs.values()):
        return print(f"Allowed kwargs are: {kwarg}")
    data = np.array(args)
    if 'mean' in kwargs.values():
        print(f"Mean: {np.mean(data)}")
    if 'median' in kwargs.values():
        print(f"Median: {np.median(data)}")
    if 'quartile' in kwargs.values():
        print(f"Quartile: {np.percentile(data, [25, 75])}")
    if 'std' in kwargs.values():
        print(f"Std: {np.std(data)}")
    if 'var' in kwargs.values():
        print(f"Var: {np.var(data)}")


def main():
    ft_statistics(1, 42, 360, 11, 64, to="mean", tu="median", ta="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ej="heheh", ejd="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
