__doc__ = """This module contains functions for calculating
 Body Mass Index (BMI) and checking if BMI values exceed a given limit.

Functions:
- give_bmi(height: list[int | float], weight: list[int | float])
    -> list[int | float]:
        Calculate the BMI values based on given heights and weights.

- apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    Determine whether the BMI values exceed the given limit.

Usage Example:
    heights = [170, 165, 180]  # in centimeters
    weights = [70, 55, 90]      # in kilograms
    bmi_values = give_bmi(heights, weights)
    limit = 25
    above_limit = apply_limit(bmi_values, limit)
    print("BMI values:", bmi_values)
    print("Above limit:", above_limit)
"""


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length")
    result = []

    return


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return
