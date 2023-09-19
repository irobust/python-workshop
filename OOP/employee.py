class Employee:
    def __init__(self, **args):
        self._firstname = args['firstname'] if 'firstname' in args else ''
        self._lastname = args['lastname']
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, firstname):
        if len(firstname) <= 3:
            raise AttributeError("Firstname must be at least 4 characters")
        self._firstname = firstname

    def display(self):
        return f'{self._firstname.upper()} {self._lastname.upper()}'

class SalaryEmployee(Employee):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname=firstname, lastname=lastname)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary * 0.97
    

class HourlyEmployee(Employee):
    def __init__(self, firstname, lastname, weekly_hours, hourly_rate):
        super().__init__(firstname=firstname, lastname=lastname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return (self.weekly_hours * self.hourly_rate) * 0.97