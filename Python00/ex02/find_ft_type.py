def all_thing_is_obj(obj: any) -> int:
    if isinstance(obj, list):
        print("List :", type(obj))
    elif isinstance(obj, tuple):
        print("Tuple :", type(obj))
    elif isinstance(obj, set):
        print("Set :", type(obj))
    elif isinstance(obj, dict):
        print("Dict :", type(obj))
    elif isinstance(obj, str):
        print(f"{obj} is in the kitchen :", type(obj))
    else:
        print("Type not found")
    return 42


# def main():
#     ft_list = ["Hello", "tata!"]
#     ft_tuple = ("Hello", "toto!")
#     ft_set = {"Hello", "tutu!"}
#     ft_dict = {"Hello" : "titi!"}
#     all_thing_is_obj(ft_list)
#     all_thing_is_obj(ft_tuple)
#     all_thing_is_obj(ft_set)
#     all_thing_is_obj(ft_dict)
#     all_thing_is_obj("Brian")
#     all_thing_is_obj("Toto")
#     print(all_thing_is_obj(10))

# if __name__ == "__main__":
#     main()