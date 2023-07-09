class IncorrectInput(Exception):
    pass


class MissingArgument(Exception):
    pass


def divide(numerator=None, denominator=None):
    try:
        if (numerator is None or denominator is None):
            raise MissingArgument
        return (numerator/denominator)
    except ZeroDivisionError as e:
        print("⚠️ Error:", e)
        raise ZeroDivisionError
    except TypeError as e:
        print("⚠️ Error:", e)
        raise IncorrectInput


def get_user_input():
    numerator = int(input("Please enter your numerator: "))
    denominator = int(input("Please enter your denominator: "))
    return numerator, denominator

# HOW TO USE THE FUNCTIONS:
# user_input = get_user_input()
# num1 = user_input[0]
# num2 = user_input[1]
# print(divide(num1, num2))
