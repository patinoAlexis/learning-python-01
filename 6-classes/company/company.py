from .employee import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employees(self):
        print('All employees:')
        for employee in self.employees:
            print(employee.name)
        print('---------------------------')

    def display_paycheck_employees(self):
        print('All employees and their paychecks:')
        for employee in self.employees:
            print(f"{employee.name} - ${employee.calculate_paycheck():,.2f}")
        print('---------------------------')



def main():
    company = Company()
    employee1 = SalaryEmployee("Alice", 30, 60000)
    employee2 = HourlyEmployee("Bob", 35, 50,25)
    employee3 = ComissionEmployee("Charlie", 25,30000,5,200)
    # employee1.hello = 1
    company.add_employee(employee1)
    company.add_employee(employee2)
    company.add_employee(employee3)

    company.display_all_employees()
    company.display_paycheck_employees()
    # print(employee1.hello)

if __name__ == '__main__':
    main()