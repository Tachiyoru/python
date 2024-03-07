__doc__ = """This module contains functions for calculating
 Body Mass Index (BMI) and checking if BMI values exceed a given limit.

Functions:
- give_bmi(height: list[int | float], weight: list[int | float])
    -> list[int | float]:
        Calculate the BMI values based on given heights and weights,
        with the formula  BMI = weight / (height^2).

- apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    Determine whether the BMI values exceed the given limit.

Usage Example:
    from give_bmi import give_bmi, apply_limit
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
"""


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length")
    result = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError("Height and weight must be integers or floats")
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight must be positive values")
        bmi = w/(h**2)
        result.append(bmi)
    return result


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [b > limit for b in bmi]
