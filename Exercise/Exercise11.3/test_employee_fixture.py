import pytest
from employee import Employee


@pytest.fixture
def employee():
    return Employee("Sergie", "Azril", 50000)


def test_give_default_raise(employee):
    employee.give_raise()

    assert employee.annual_salary == 55000


def test_give_custom_raise(employee):
    employee.give_raise(10000)

    assert employee.annual_salary == 60000
    
# HASIL PYTEST
# platform win32 -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0
# rootdir: C:\Users\Sergie\pyser\Sergie-Muhammad-Azril_109\Exercise\Exercise11.3
# collected 4 items                                                                                                                                     

# test_employee.py ..                                                                                                                             [ 50%]
# test_employee_fixture.py ..                                                                                                                     [100%]
