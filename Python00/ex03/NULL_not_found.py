def NULL_not_found(obj: any) -> int:
    if obj is None:
        print("Nothing: None", type(obj))
    elif isinstance(obj, float):
        print("Cheese: nan", type(obj))
    elif obj == 0 and not isinstance(obj, bool):
        print("Zero:", obj, type(obj))
    elif isinstance(obj, str) and obj == '':
        print("Empty:", type(obj))
    elif isinstance(obj, bool):
        print("Fake:", obj, type(obj))
    else:
        print("Type not Found")
        return 1
    return 0


def main():
    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))


if __name__ == "__main__":
    main()
