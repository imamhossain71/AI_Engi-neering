print("Hello AI Engineering!")
name= "AI Engineer"
age = 25
is_student = False
skills = ["Python", "Machine Learning", "Data Analysis"]
print(f"Name: {name}, Age: {age}, Student: {is_student} Skills: {skills}")
#Functions
def squre(num):
    return num*num
print (squre(2))
#class & Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p1 = Person("Aronb", 25)
print(p1.introduce())