from Person import Person
from Employee import Employee
from Car import Car
from Office import Office

def main():
    car1 = Car("Toyota", 50, 100)
    car2 = Car("Ford", 60, 100)

    emp1 = Employee("Michael", 1000, "neutral", 80, 1, car1, "michael@gmail.com", 5000, 30)

    emp1.sleep(6)
    print(emp1.mood)
    emp1.eat(2)
    print(emp1.healthRate)
    emp1.buy(3)
    print(emp1.money)

    emp1.work(9)
    print(emp1.mood)
    emp1.refuel(30)
    print(emp1.car.fuelRate)
    emp1.drive(100)
    emp1.send_mail("Martin", "there is a problem with production")

    office = Office("TechCorp", {})
    office.hire(emp1)
    print(len(office.get_all_emp()))

if __name__ == "__main__":
    main()