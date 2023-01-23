class Employee:

    raise_amount = 1.04

    def __init__(self, name, family_name, salary):
        self.name = name
        self.family_name = family_name
        self.full_name = f"{self.name} {self.family_name}"
        self.salary = salary


    def email(self):
        return f"{self.name}.{self.family_name}@company.com"


    def raise_salary(self):
        self.salary = int(self.salary * self.raise_amount)


    def __str__(self):
        return self.full_name


    def __repr__(self):
        return self.full_name


class Developer(Employee):
    def __init__(self, name, family_name, salary, lang):
        super().__init__(name, family_name, salary)
        self.lang = lang


class Manager(Employee):
    def __init__(self, name, family_name, salary, employees=None):
        Employee.__init__(self, name, family_name, salary)
        if not employees:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_employees(self):
        for emp in self.employees:
            print(f"---> {emp}")



emp_2 = Employee('Mahnaz', 'Mahnazi', 42_000)
emp_1 = Developer('Behdad', 'siyavoshi', 40_000, 'Python')
manager = Manager("Sepehr", "Akbarzadeh", 50_000)

# print(emp_1.lang)
# print(emp_1.name)
# print(emp_1.email())
# print(emp_1.salary)
# emp_1.raise_salary()
# print(emp_1.salary)

manager.add_employee(emp_1)
manager.show_employees()
print(manager.email())
