class IncorrectInput(Exception):
    pass


def divide(numerator=1, denominator=2):
    try:
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
