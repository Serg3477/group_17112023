def working_with_dict_from_input_values(time_input: str, speed_input: str, weight_input: str) -> str:
    distance = int(time_input) * int(speed_input)
    result = (f'Транспортний засіб вагою {weight_input} кг рухався {time_input} секунд зі швидкістю {speed_input}'
              f' м/сек, і подолав відстань {distance} метрів.')
    return result