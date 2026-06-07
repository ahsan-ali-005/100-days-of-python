# Create custom exception

class My_custom_Exception(Exception):
    pass


def check_exception(string):

    if string == str(string):
        raise My_custom_Exception("String numbers are not allowed!")
    else:
        print(f"String is fine: {string}")


num=input("Enter a Number: ")
try:
    check_exception(num)
except My_custom_Exception as e:
    print("Caught an exception:", e)