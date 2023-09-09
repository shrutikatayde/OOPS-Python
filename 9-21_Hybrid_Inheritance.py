class Engineering:
    def __init__(self, year, branch, experience):
        self.year = year
        self.branch = branch
        self.experience = experience

    def student_details(self):
        print(f"Year: {self.year}")
        print(f"Branch: {self.branch}")

    def faculty_details(self):
        print(f"Year of experience: {self.experience}")


class Students(Engineering):
    def __init__(self, name, year=3, branch="Mechanical"):
        super().__init__(
            year, branch
        )  # Call the parent class constructor directly with experience=0
        self.name = name

    def student_details(self):
        super().student_details()
        print(f"Name: {self.name}")


class Faculty(Engineering):
    def __init__(self, t_name, year=7, branch="CSE", experience=10):
        super().__init__(
            year, branch, experience
        )  # Call the parent class constructor directly
        self.t_name = t_name

    def faculty_details(self):
        super().faculty_details()
        print(f"Teacher Name: {self.t_name}")


class SectionC(Students, Faculty):
    def __init__(self, subject):
        Students.__init__(self, name="Shrutika")  # Pass name directly
        Faculty.__init__(self, t_name="N. G. Rathi")  # Pass t_name directly
        self.subject = subject

    def section_c_details(self):
        Students.student_details(self)
        Faculty.faculty_details(self)
        print(f"Subject: {self.subject}")


result = SectionC("DBMS")
result.section_c_details()
