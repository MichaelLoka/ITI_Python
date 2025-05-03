class Human:
    def eat(self):
        print("Human is eating.")

class Mammal:
    def eat(self):
        print("Mammal is eating.")

class Employee(Human, Mammal):
    def eat(self):
        print("Employee starts eating.")
        super().eat()

emp = Employee()
emp.eat()
