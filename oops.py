class MyClass:
    x=5
print(MyClass)
print(MyClass.x)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person('athu',22)
print(p1.name)
print(p1.age)

#print(p1)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name},{self.age}"
        
p1=Person('athu',22)
print(p1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("My name is " + self.name)

p1 = Person('athu', 22)
p1.myfun()

      
