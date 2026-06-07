# Implement simple polymorphism example of method overiding

class Animal:
    def show_sound(self):
        print("Some sound")

class Dog(Animal):
    def show_sound(self):   # overriding
        print("Bark")

class Cat(Animal):
    def show_sound(self):   # overriding
        print("Meow")

animals = [Dog(), Cat()]

for i in animals:
    i.show_sound()