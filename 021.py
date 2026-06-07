# Create function for temperature converter

def TempConv(temp,unit):

    if unit.lower() == "c":
        return (temp * 9/5) + 32
    elif unit.lower() == "f":
        return (temp - 32) * 5/9
    else:
        print("Invalid Unit!")


temp=float(input("Enter Temperature: "))
unit=input("Enter Unit (C/F): ")

print("Converted Temperature: " , TempConv(temp,unit))

