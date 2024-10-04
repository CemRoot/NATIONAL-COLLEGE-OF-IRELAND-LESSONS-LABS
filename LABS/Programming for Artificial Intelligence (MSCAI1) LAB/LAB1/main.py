"""Programming for Artificial Intelligence (MSCAI1) MoodleTeam-24 LAB 1"""


"""11
Questions for practise
11.1 Variables and Data Types
1. Write a program that takes a floating-point number as input and stores
it in a variable. Then, convert this number into an integer and a string,
and print all three values, showing their types. Discuss the behavior of
Python during these conversions."""


def convert_float_to_int_string():
    float_number = float(input("Enter a floating-point number: "))
    int_number = int(float_number)
    string_number = str(float_number)
    print(f"Float number: {float_number} ({type(float_number)})")
    print(f"Integer number: {int_number} ({type(int_number)})")
    print(f"String number: {string_number} ({type(string_number)})")

"""Create a Python script that accepts a date string in the format YYYY-MM-DD and then convert these into integers."""

def convert_date_string_to_integers():
    date_string = input("Enter a date in the format YYYY-MM-DD: ")

    # Check if the input contains only digits and hyphens
    for char in date_string:
        if not (char.isdigit() or char == '-'):
            print("Invalid input. Please enter only numeric characters and hyphens.")
            return convert_date_string_to_integers()

    try:
        year, month, day = date_string.split("-")
        year, month, day = int(year), int(month), int(day)

        if month > 12 or day > 31:
            raise ValueError

        print(f"Year: {year} ({type(year)})")
        print(f"Month: {month} ({type(month)})")
        print(f"Day: {day} ({type(day)})")

    except ValueError:
        print("Invalid date. Month can't be more than 12 and day can't be more than 31.")
        return convert_date_string_to_integers()


if __name__ == "__main__":
    convert_date_string_to_integers()





