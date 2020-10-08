import functools


def get_month_decorator(func):
    """This is a decorator that makes sure that the input to get_month function is between 1 and 12"""

    @functools.wraps(func)
    def wrapper(month):
        if 1 <= month <= 12:  # If condition is satisfied, return the function, else raise ValueError
            return func(month)
        else:
            raise ValueError("Your month value can only be between 1 and 12")
    # return the wrapper without brackets
    return wrapper


@get_month_decorator  # Applying the get_month_decorator to the get_month function
def get_month(month):
    """This function takes in an integer(month) argument and returns the name of the month that
    corresponds to the number"""

    # Generate a list of numbers between 1 and 12
    number = [i for i in range(1, 13)]
    # Declare a list of 12 months
    month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    # Generate a dictionary that takes in both month_name and number , with the number as the key
    month_dict = {number[i]: month_name[i] for i in range(len(number))}

    if month in month_dict:  # If the key exists, return the corresponding month, else return an error message
        return month_dict[month]
    else:
        return "Key does not exist"
