
class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def __repr__(self):
        return f"{self.name} {self.age} {self.id} "

