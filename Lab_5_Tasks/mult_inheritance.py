class Human:
    def eat(self):
        print("Human is eating.")
        super().eat()

class Mammal:
    def eat(self):
        print("Mammal is eating.")

class Employee(Human, Mammal):
    def eat(self):
        print("Employee starts eating.")
        super().eat()

emp = Employee()
emp.eat()
