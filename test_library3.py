import library3
import pytest


def working_with_dict_from_input_walues(my_dict: dict) -> str:
    if my_dict['time='] < 0:
        raise ValueError ('Введ іть корректне значення.')
    if my_dict['speed='] < 0:
        raise ValueError ('Введ іть корректне значення.')
    if my_dict['weight='] < 0:
        raise ValueError ('Введ іть корректне значення.')
    distance = my_dict['time='] * my_dict['speed=']
    result = ("Транспортний засіб вагою " + str(my_dict['weight=']) + " кг рухався " + str(my_dict['time='])
              + " секунд зі швидкістю " + str(my_dict['speed=']) + " м/сек, і подолав відстань " + str(distance) +" метрів.")
    
    my_time = '20'
    my_speed = '10'
    my_weight = '1000'
    distance = my_time * my_speed
    expected = ("Транспортний засіб вагою " + str(my_weight) + " кг рухався " + str(my_time) + " секунд зі швидкістю "
                + str(my_speed) + " м/сек, і подолав відстань " + str(distance) +" метрів.")
    assert result == expected
    