class Office:
    employeeNum = 0

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_emp(self):
        return list(self.employees.values())

    def get_employees(self, empId):
        return self.employees[empId]

    def hire(self, employee):
        self.employees[employee.id] = employee
        Office.employeeNum += 1

    def fire(self, empId):
        if empId in self.employees:
            del self.employees[empId]
            Office.employeeNum -= 1
        else:
            print("This employee does not exist")

    def deduct(self, empId, deduction):
        if empId in self.employees:
            self.employees[empId].salary -= deduction

    def reward(self, empId, reward):
        if empId in self.employees:
            self.employees[empId].salary += reward


    def check_lateness(self, empId, moveHour):
        employee = self.employees[empId]
        if not employee:
            return

        is_late = self.calculate_lateness(9, moveHour, employee.distanceToWork, employee.car.velocity)
        if is_late:
            self.deduct(empId, 10)
        else:
            self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            raise ValueError("Can't divide by zero")
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeeNum = num
