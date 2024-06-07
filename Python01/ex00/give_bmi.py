def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI values based on given heights and weights,
        with the formula  BMI = weight / (height^2)."""
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
    """Determine whether the BMI values exceed the given limit."""
    return [b > limit for b in bmi]


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print(type(e).__name__ + ":", e)


if __name__ == "__main__":
    main()
