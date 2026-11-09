from city_functions import city_country


def test_city_country():
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"
    
# Hasil dari pytest
# platform win32 -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0
# rootdir: C:\Users\Sergie\pyser\Sergie-Muhammad-Azril_109\Exercise
# collected 1 item                                                                                                                                      
# Exercise11.1\test_city.py .