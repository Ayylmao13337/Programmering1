'''import klasser

klasser.Student
'''
from klasser import Student

student_1 = Student("Ola","Nordmann",25,1232141)


student_2 = Student("Kari","Nordmann",30,63211)

print(student_1.get_description())
print(student_2.get_description())