class Student:
    # Class variable
    school = "ABC High School"
    def __init__(self):
        self.marks1='marks 1'
        self.marks2='marks 2'
        self.marks3='marks 3'

    # Instance methods
    def show(self):
        print(self.marks1)
    def give(self,value):
        self.marks1= value

    #class method
    @classmethod
    def get_school(cls):
        return cls.school
    
    # static method
    @staticmethod
    def sayhello():
        print("Hello students!")

s1=Student()
s2=Student()
s1.give(72)
s2.give(68)
s1.show()
s2.show()
print(Student.get_school())
Student.sayhello()