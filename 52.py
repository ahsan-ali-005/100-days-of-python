# Implement multiple inheritance

class A:
    @staticmethod
    def call_A():
        print("I am A")
class B:
    @staticmethod
    def call_B():
        print("I am B")
class C:
    @staticmethod
    def call_C():
        print("I am C")

class D(A,B,C):

    @staticmethod
    def call_D():
        print("I am D")



o1=D()

o1.call_A()
o1.call_B()
o1.call_C()
o1.call_D()
