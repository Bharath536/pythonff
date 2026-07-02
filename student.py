# Student Class

class Student:

    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def display(self):
        print("----- Student Details -----")
        print("Student ID :", self.id)
        print("Student Name :", self.name)
        print("Student Marks :", self.marks)


# Create Student Object
student1 = Student(101, "Siva", 95)

student1.display()

print()   # Empty line


# Person Class

class Person:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def profile(self):
        print("----- Person Profile -----")
        print("Name :", self.name)
        print("Age :", self.age)
        print("City :", self.city)


# Create Person Object
person1 = Person("Siva", 22, "Hyderabad")

person1.profile()