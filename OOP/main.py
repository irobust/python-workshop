from employee import Employee

def main():
    employee1 = Employee(firstname="john", lastname="doe")
    print(employee1._firstname)

    employee1._firstname = 'John'
    employee1._lastname = 'Doe'
    print(employee1.display())

if __name__ == '__main__': main()