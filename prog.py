from student import Student
from mangament import Mangament
manger=Mangament()

class StartProject:
    while True:
        MASSEG="""1.Add Student
2.show Students
3.get Student
4.Quit"""
        print(MASSEG)
        try:
            choise=int(input("enter your choise: "))
        except ValueError:
            print("Please Enter a valid number.")
            continue
            
             
        if choise == 1 :
            name=input("Enter Name Student:  ")
            age=input("Enter Age Student: ")
            Id=input("Enter Id Stuident: ")
            print(f"name= {name}\nage= {age}\nId= {Id}")
            choise_save=input("save press (s)\nend press (e)\n ")
            if choise_save == "s":
                student=Student(name , age , Id)
                manger.add_student(student)
                print("Adding Student")
            elif choise_save == "e":
                print("don't save any data..\n end press (q) \n repet programing press (r)..")
                choise_end_or_repet=input("Enter here: ")
                if choise_end_or_repet == "q" : 
                    break
                elif choise_end_or_repet == "r":
                    continue
            else:
                print("Please Press (s) Or (e) to saving")
                continue

        elif choise == 2 :
            manger.show_studens()
            choise_repet_quit=input("press (c) continoe\npress (q) quit\n ")
            if choise_repet_quit == "c":
                continue
            elif choise_repet_quit == "q":
                print("nice to time")
                break
        elif choise == 3 :
            search_id=input("enter id: ")
            result=manger.get_student(search_id)
            if result is not None:
                print(result.id,
                    result.name,
                    result.age)
                print("student Found! ")
                
            else:
                print(result)
                print("Student not found.")
        
        elif choise == 4 :
            print("nice time see you leter (: ") 
            break

        else:
            print("Please select 1 to 4 ")
            continue






