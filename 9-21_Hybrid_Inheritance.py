# Hybrid Inheritance


class Engineering:
    def __init__(self, year, branch):
        self.year = year
        self.branch = branch

    def student_details(self):
        print(f"Name : {self.year}")
        print(f"Branch : {self.branch}")


class Student1(Engineering):
    def __init__(self, name):
        Engineering.__init__(self, year=4, branch="CSE")
        self.name = name

    def student_details(self):
        print(f"Name : {self.year}")
        print(f"Branch : {self.branch}")


class Student2(Engineering):
    pass


class SectionC(Student1, Student1):
    pass
