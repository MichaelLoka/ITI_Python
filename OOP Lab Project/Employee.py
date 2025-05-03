import Person as Person
import Car as Car

class Employee(Person):
    def __inti__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        self.salary = hours*25

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = self.car.fuelRate + gasAmount

    def send_mail(self, name, msg):
        print(f"Sending email from {self.email} ...")
        print(f"Hello {name},")
        print(f"I hope you are doing alright.")
        print(f"I'm reaching out to you to report that {msg}")
