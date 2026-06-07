# Track total objects using class variable

class A:
    count = 0

    def __init__(self):
        self.__class__.count += 1   # increment count for class variable 

    @classmethod
    def show_count(cls):
        print(f"The Number of objects: {cls.count}")

ob1 = A()
ob2 = A()
ob3 = A()

A.show_count()