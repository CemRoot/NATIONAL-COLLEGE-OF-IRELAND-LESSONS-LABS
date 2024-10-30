# Python Programming Concepts Implementation

# 1. Operators in Python


def arithmetic_operations(a, b):
    """
    Performs basic arithmetic operations between two numbers.
    :param a: First number
    :param b: Second number
    :return: Dictionary with the results of addition, subtraction, multiplication, division, and modulus
    """
    operations = {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b,
        "modulus": a % b,
    }
    return operations


def comparison_operations(a, b):
    """
    Compares two numbers and returns comparison results.
    :param a: First number
    :param b: Second number
    :return: Dictionary with comparison results
    """
    comparisons = {"greater_than": a > b, "equal": a == b, "not_equal": a != b}
    return comparisons


def logical_operations(a, b):
    """
    Performs logical operations between two boolean conditions.
    :param a: First boolean condition
    :param b: Second boolean condition
    :return: Dictionary with logical operation results
    """
    logicals = {
        "and_operation": a and b,
        "or_operation": a or b,
        "not_operation": not a,
    }
    return logicals


# Task: Complex Number Arithmetic
def complex_operations(c1, c2):
    """
    Performs basic arithmetic operations between two complex numbers.
    :param c1: First complex number
    :param c2: Second complex number
    :return: Dictionary with the results of addition, subtraction, multiplication, and division
    """
    operations = {
        "addition": c1 + c2,
        "subtraction": c1 - c2,
        "multiplication": c1 * c2,
        "division": c1 / c2,
    }
    return operations


# 2. Data Types and Type Conversion


def type_conversion(value):
    """
    Checks and converts the input value to float if it is an integer, otherwise returns the value as it is.
    :param value: Input value
    :return: Converted value
    """
    if isinstance(value, int):
        return float(value)
    return value


# 3. Control Flow (if-elif-else)


def age_category(age):
    """
    Categorizes the input age into child, teenager, adult, or senior.
    :param age: Age in years
    :return: Category string
    """
    if age < 12:
        return "Child"
    elif 12 <= age <= 17:
        return "Teenager"
    elif 18 <= age <= 65:
        return "Adult"
    else:
        return "Senior"


# 4. Loops (for and while)


# Task: Sum of Even Numbers
def sum_even_numbers():
    """
    Calculates the sum of all even numbers between 1 and 100 using a for loop.
    :return: Sum of even numbers
    """
    return sum(num for num in range(1, 101) if num % 2 == 0)


# Task: Prime Numbers with Nested Loops
def prime_numbers(n):
    """
    Returns a list of all prime numbers less than n using a nested loop.
    :param n: Upper limit for prime numbers
    :return: List of prime numbers
    """
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# 5. Functions and Lambda Expressions


# Task: Lambda Expression for Multiplication
def multiply(a, b, c):
    return a * b * c


# Task: Sorting with Lambda
def sort_dictionaries_by_key(dicts, key):
    """
    Sorts a list of dictionaries by a given key using a lambda function.
    :param dicts: List of dictionaries
    :param key: Key by which to sort
    :return: Sorted list of dictionaries
    """
    return sorted(dicts, key=lambda x: x[key])


# 6. Lists and List Comprehension


# Task: Flatten a Nested List
def flatten_nested_list(nested_list):
    """
    Flattens a nested list using list comprehension.
    :param nested_list: A list of lists
    :return: Flattened list
    """
    return [item for sublist in nested_list for item in sublist]


# 7. Dictionaries and Sets


# Task: Merge Dictionaries
def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries, summing values for matching keys.
    :param dict1: First dictionary
    :param dict2: Second dictionary
    :return: Merged dictionary
    """
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict


# Example usage:
if __name__ == "__main__":
    # Operators in Python
    print("Arithmetic Operations:", arithmetic_operations(10, 5))
    print("Comparison Operations:", comparison_operations(10, 5))
    print("Logical Operations:", logical_operations(True, False))

    # Complex Number Arithmetic
    print("Complex Number Operations:", complex_operations(3 + 2j, 1 + 7j))

    # Data Types and Type Conversion
    print("Type Conversion:", type_conversion(10))

    # Control Flow
    print("Age Category:", age_category(20))

    # Loops
    print("Sum of Even Numbers:", sum_even_numbers())
    print("Prime Numbers less than 20:", prime_numbers(20))

    # Lambda Expressions
    print("Lambda Multiplication:", multiply(2, 3, 4))

    # Sorting with Lambda
    dicts = [{"name": "John", "age": 25}, {"name": "Jane", "age": 22}]
    print("Sorted by Age:", sort_dictionaries_by_key(dicts, "age"))

    # Lists and List Comprehension
    nested_list = [[1, 2], [3, 4], [5, 6]]
    print("Flattened List:", flatten_nested_list(nested_list))

    # Dictionaries and Sets
    dict1 = {"a": 10, "b": 20}
    dict2 = {"b": 5, "c": 15}
    print("Merged Dictionaries:", merge_dictionaries(dict1, dict2))
