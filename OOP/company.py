class Company:
    # Composition
    def __init__(self, employee):
        self.employees = [employee]

    # Aggregation
    def addEmployee(self, employee):
        if employee is not employee:
            raise Exception("parameter must be Employee")
        self.employees.append(employee)

    def displayAllEmployees(self):
        for employee in self.employees:
            print(f'{employee.display()} => {employee.calculate_paycheck():,.2f}')