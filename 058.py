# Implement Method Overloading using *argus

class Calculator:
    
    def add(self, *numbers):
        total = 0
        for num in numbers:
            total += num
        return total


obj = Calculator()

print(obj.add(5))            # 5
print(obj.add(5, 10))        # 15
print(obj.add(5, 10, 20))    # 35
print(obj.add(1, 2, 3, 4))   # 10