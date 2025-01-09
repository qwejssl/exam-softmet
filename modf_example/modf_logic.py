import math

def split_fractional_part(value):
    """
    Splits the fractional and integer parts of a given number using math.modf.

    Returns a tuple of:
    (fractional_part, integer_part)
    """
    fractional, integer = math.modf(value)
    return fractional, integer
