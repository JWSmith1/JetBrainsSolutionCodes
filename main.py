class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = name[0] + last_name + birth_year


name1 = input()
last_name1 = input()
birth_year1 = input()
id = Student(name1, last_name1, birth_year1)
print(id.student_id)






