def working_with_dict_from_input_walues(my_dict: dict) -> str:
    distance = my_dict['time='] * my_dict['speed=']
    result = ("Транспортний засіб вагою " + str(my_dict['weight=']) + " кг рухався "
              + str(my_dict['time=']) + " секунд зі швидкістю " + str(my_dict['speed='])
              + " м/сек, і подолав відстань " + str(distance) +" метрів.")
    return result