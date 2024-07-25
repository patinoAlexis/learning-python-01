
class Employee:
    def __init__(self, fname, lname):
        self.name = fname
        self.name = lname


class SalaryEmployee(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 52


class HourlyEmployee(Employee):
    def __init__(self, name, age, hourly_rate, hours_worked):
        super().__init__(name, age)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_paycheck(self):
        return self.hourly_rate * self.hours_worked

class ComissionEmployee(SalaryEmployee):
    def __init__(self, name, age, salary, comission_rate, sales):
        super().__init__(name, age, salary)
        self.comission_rate = comission_rate
        self.sales = sales

    def calculate_paycheck(self):
        return super().calculate_paycheck() + (self.comission_rate * self.sales)