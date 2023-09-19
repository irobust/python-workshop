from employee import Employee, SalaryEmployee, HourlyEmployee
from company import Company

def main():
    employee1 = SalaryEmployee("john", "doe", 20000)
    print(employee1._firstname)

    employee1._firstname = 'John'
    employee1._lastname = 'Doe'
    print(employee1.display())

    company1 = Company(employee1)
    company1.addEmployee(employee1)

    employee2 = SalaryEmployee("Jack", "Doe", 30000)
    employee3 = HourlyEmployee("Jimmy", "Doe", 50, 2000)

    company1.addEmployee(employee2)
    company1.addEmployee(employee3)

    company1.displayAllEmployees()


if __name__ == '__main__': main()