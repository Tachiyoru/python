def slice_me(family: list, start: int, end: int) -> list:
    """This function takes as parameters a 2D array, prints its shape,
 and returns a truncated version of the array based on the provided
   start and end arguments. The function uses the slicing method
     to perform the truncation."""
    if not isinstance(family, list):
        raise ValueError("Input must be a list")
    if not family:
        raise ValueError("Input list is empty")
    sublist_length = len(family[0])
    if not all(len(sublist) == sublist_length for sublist in family):
        raise ValueError("Sublists must have the same length")
    print("My shape is:", (len(family), sublist_length))
    sliced_array = family[start:end:1]
    print("My new shape is:", (len(sliced_array), sublist_length))
    return sliced_array


def main():
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print("Original list is : ", family)
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
