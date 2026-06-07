# Convert decimal to binary

def deci_to_bi(num, binary_number):

    while num > 0:
        remainder = num % 2
        binary_number = str(remainder)  + binary_number
        num = num // 2

    return binary_number


num = int(input("Enter a Number in Decimal: "))
binary_number = ""

result = deci_to_bi(num, binary_number)

print("Binary Number:", result)