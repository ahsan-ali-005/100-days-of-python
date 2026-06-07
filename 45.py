# Operator overloading (Vector class)

class Vector:

    def __init__(self,i,j,k):

        self.i=i
        self.j=j
        self.k=k
    
    def show_vector(self):
        print(f"({self.i}i,{self.j}j,{self.k}k)")
    
    def __add__(self, other):
        return Vector(self.i+other.i, self.j+other.j, self.k+other.k)
    
    def __mul__(self, other):
        return (self.i*other.i) + (self.j*other.j) + (self.k*other.k)
    
    def __str__(self):
        return f"{self.i}i,{self.j}j,{self.k}k"


v1=Vector(1,2,3)
v2=Vector(1,2,4)

v=v1+v2
v3=v1*v2
print(v)
print(v3)