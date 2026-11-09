# TANPA FIXTURE
from employee import Employee


def test_give_default_raise():
    employee = Employee("Sergie", "Azril", 50000)
    employee.give_raise()

    assert employee.annual_salary == 55000


def test_give_custom_raise():
    employee = Employee("Sergie", "Azril", 50000)
    employee.give_raise(10000)

    assert employee.annual_salary == 60000
    
# HASIL PYTEST
# rootdir: C:\Users\Sergie\pyser\Sergie-Muhammad-Azril_109\Exercise\Exercise11.3
# collected 2 items                                                                                                                                     

# test_employee.py .