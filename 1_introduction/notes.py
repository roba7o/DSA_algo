#Child and parent class example

class Person:
    def __init__(self, f_name, l_name, home_country):
        self.first_name = f_name
        self.last_name = l_name
        self.home_country = home_country

    def print_name(self):
        print(self.first_name, self.last_name)

    def print_country(self):
        print(self.home_country)

class Student(Person):
    def __init__(self, f_name, l_name, home_country, university):
        super().__init__(f_name, l_name, home_country)
        self.university = university
    
    def print_university(self):
        print(self.university)

class Employee(Person):
    def __init__(self, f_name, l_name, home_country, employer):
        Person.__init__(self, f_name, l_name, home_country)
        self.employer = employer