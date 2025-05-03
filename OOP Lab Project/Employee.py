from Person import Person
class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        elif hours < 8:
            self.mood = "lazy"

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = self.car.fuelRate + gasAmount

    def send_mail(self, name, msg):
        print(f"Sending email from {self.email} ...")
        print(f"Hello {name},")
        print(f"I hope you are doing alright.")
        print(f"I'm reaching out to you to report that {msg}")

