# math_utils.py

def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide_numbers(a, b):
    """Returns a / b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b