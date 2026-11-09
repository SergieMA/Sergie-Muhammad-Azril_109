from city_functions import city_country


def test_city_country():
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"


def test_city_country_population():
    result = city_country("santiago", "chile", population=5000000)
    assert result == "Santiago, Chile – population 5000000"
    
# platform win32 -- Python 3.14.7, pytest-9.2.0, pluggy-1.7.0
# rootdir: C:\Users\Sergie\pyser\Sergie-Muhammad-Azril_109\Exercise\Exercise11.2
# collected 2 items                                                                                                                                     

# test_cities.py ..                                                                                                                               [100%]
