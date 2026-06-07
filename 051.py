# Implement inheritance (Animal example)

class Animal:

    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    
    def eat(self):
        print(f"{self.name} is Eating...")
    
    def sleeping(self):
        print(f"{self.name} is Sleeping...")


class Dog(Animal):

    def __init__(self,name,age,color,breed):  # one more attribute need to make new constructor so use super() to call parent constructor with this constructor
        super().__init__(name,age,color)
        self.breed=breed
    
    def eat(self):
        super().eat()

    def sleeping(self):
        super().sleeping()

class Bird(Animal):

    #Method Overiding
    def eat(self):
        print(f"{self.name} is eating seeds.")

    def sleeping(self):
        super().sleeping()  
    



d1=Dog("Tommy",5,"Black","Bulldog")

b1=Bird("Buddy",2,"Brown")

b1.sleeping()
d1.eat()