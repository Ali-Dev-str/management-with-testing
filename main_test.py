
def add(a,b):
    return a+b


def is_even(number):
    return number % 2 == 0


def divide(a,b):
    return a / b

def get_lenthg(text):
    return len(text)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount


class BankManger:
    def __init__(self,name):
        self.name = name
        self.allaccunts=[]
        

    def addaccount(self,account):
        self.allaccunts.append(account)

    def delete_account(self,account):
        for accoun in self.allaccunts:
            if accoun == account:
                self.allaccunts.remove(account)
                print("succsesfull remove")
            else:
                print("Sry Found this account")

    def search_account(self,account):
        for acc in self.allaccunts:
            if acc == account:
                return acc
            else:
                return "sry found this account "

    def how_many_account(self):
        return len(self.allaccunts)
    

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def __repr__(self):
        return f"{self.name} {self.age} {self.grade}"

class StudentManager:
    def __init__(self,name_manager):
        self.name_manger=name_manager
        self.all_students=[]

    def add_student(self,student):
        self.all_students.append(student)

    def delete_student(self,student):
        for stu in self.all_students:
            if stu == student:
                self.all_students.remove(stu)


    def search_student(self,student):
        for stu in self.all_students:
            if stu == student:
                print(stu)

    def update_student(self,student,name,age,grade):
        for stu in self.all_students:
            if stu == student:
                old_student=stu
                self.all_students.remove(old_student)
                new_student=name + age + grade
                self.all_students.append(new_student)

    def get_all_student(self):
        return self.all_students
    

