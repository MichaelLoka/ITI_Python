class Human:
    def eat(self):
        print("Human is eating with utensils.")

class Mammal:
    def eat(self):
        print("Mammal is eating raw.")

class Employee(Human, Mammal):
    pass

emp = Employee()
emp.eat()
