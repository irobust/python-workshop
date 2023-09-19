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
