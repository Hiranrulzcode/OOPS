class Student():
    name=""
    age=13
    grade=7
    student_number=10947568

    def __init__(self):
        print("This is the object of student class.")


    def changed_details(self):
        self.age=input("Enter your age")
        self.name=input("Enter your name")
    
    def show_details(self):
        print(self.name, self.age, self.grade, self.student_number)


hiran=Student()
nireeksh=Student()
hiran.changed_details()
hiran.show_details()
nireeksh.changed_details()
nireeksh.show_details()
