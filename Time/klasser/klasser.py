from multiprocessing import set_forkserver_preload


class Student:
    def __init__(self,firstname,lastname,age,student_id):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.student_id = student_id 
    def get_description(self):
        return(f"the students name is"\
            f" {self.firstname} {self.lastname}"\
                f", is {self.age} years old with student id"\
                    f"{self.student_id}") 

