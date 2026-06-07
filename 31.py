# Create function decorator (basic)      

# ---> A decorator is a function that modifies or extends the behavior of another function.

# ---> It allows you to add extra functionality without changing the original function code.

def first_func(func):          # Accept original function

    def second_func():          # Wrapper function
        print("Function started")
        func()                 # Call the original function
        print("Function ended")

    return second_func          # Return the wrapper


def say_hello():
    print("Hello")


say_hello = first_func(say_hello)   # Decorate
say_hello()                         # Call decorated function