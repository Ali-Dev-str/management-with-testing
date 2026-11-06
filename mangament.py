from student import Student

class Mangament:
    def __init__(self):
        self.Students=[]

    def add_student(self,student):
        self.Students.append(student)

    def show_studens(self):
        print(self.Students)

    def get_student(self,id):
        for student in self.Students:
            if student.id == id:
                return student
            
        return None


    