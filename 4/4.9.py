class Profile:
    def __init__(self, profession):
        self.profession = profession
    def info(self):
        return ""
    def describe(self):
        print(f"Profession: {self.profession} {self.info()}")
class Vacancy(Profile):
    def __init__(self, profession, salary):
        super().__init__(profession)
        self.salary = salary
    def info(self):
        return f"Salary: {self.salary}"
class Resume(Profile):
    def __init__(self, profession, experience):
        super().__init__(profession)
        self.experience = experience
    def info(self):
        return f"Experience: {self.experience} years"
vacancy1 = Vacancy("Software Engineer", 70000)
vacancy1.describe()
resume1 = Resume("Data Scientist", 5)
resume1.describe()