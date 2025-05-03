import Person as Person

class Employee(Person):
    def __inti__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        self.salary = hours*25
