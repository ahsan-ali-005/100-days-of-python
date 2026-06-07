import time

def greet_user():
    # Get the current hour in 24-hour format (0-23)
    # time.strftime("%H") returns a string, so we convert it to an integer
    current_hour = int(time.strftime("%H"))
    
    # Determine the appropriate greeting
    if 5 <= current_hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon!"
    elif 18 <= current_hour < 22:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"
    
    # Display the result
    print(f"It's currently {time.strftime('%I:%M %p')}.")
    print(greeting)



if __name__ == "__main__":
    greet_user()