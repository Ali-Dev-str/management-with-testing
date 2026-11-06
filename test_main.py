from main import add
from main import is_even
from main import divide
from main import get_lenthg 
from main import BankAccount
from main import BankManger
from main import Student
from main import StudentManager
import pytest

def test_add():
    """Get This Method additonal result = 5 """
    result=add(2,3)
    assert result == 5
    """Get This Method additonal result = 30 """
    result2= add(10,20)
    assert result2 == 30

def test_is_even():
    result=is_even(4)
    assert result is True
    result2= is_even(7)
    assert result2 is False

def test_divide():
    result=divide(10,2)
    assert result == 5
    result2= divide(9,2)
    assert result2 == 4.5

def test_len_text():
    result=get_lenthg("ibrhim")
    assert result == 6
    result2=get_lenthg("")
    assert result2 == 0

def test_create_balance():
    account=BankAccount(1000)
    assert account.balance == 1000
    account.deposit(500)
    assert account.balance == 1500
    account.withdraw(300)
    assert account.balance == 1200
    
def test_bank_manger():
    manger=BankManger("manger")
    manger.addaccount("HSB505")
    assert "HSB505" in manger.allaccunts

    acc=manger.search_account("HSB505")
    assert acc == "HSB505"

    foundacc=manger.search_account("req502")
    assert foundacc == "sry found this account "

    lenthg_account=manger.how_many_account()
    assert lenthg_account == 1


@pytest.fixture
def students():
        student=Student("khaled","20","4")
        return student

def test_programming_student(students):
    
    manger=StudentManager("manger",)
    manger.add_student(students)

    assert  students in  manger.all_students




    












