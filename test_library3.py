import lesson12
import library3
import pytest


def test_working_with_dict_from_input_values():
    my_time = '20'
    my_speed = '10'
    my_weight = '1000'
    expected_distance = '300'
    distance = int(my_time) * int(my_speed)
    actual_result = library3.working_with_dict_from_input_values(my_time, my_speed, my_weight)
    expected = (f'Транспортний засіб вагою {my_weight} кг рухався {my_time} секунд зі швидкістю {my_speed} м/сек, і подолав відстань {distance} метрів.')
    assert actual_result == expected
    