from project03multiple_inheritance.employee import Employee
from project03multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."