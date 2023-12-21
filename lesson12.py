import library3
import pytest
import constants3


def main():
    time_input = input("Введіть час в секундах: ")
    if int(time_input) <= 0:
        raise ValueError (ERR)
    speed_input = input("Введіть швидкість (м/сек): ")
    if int(time_input) <= 0:
        raise ValueError (ERR)
    weight_input = input(" Введіть вагу авто (кг): ")
    if int(time_input) <= 0:
        raise ValueError (ERR)
    my_dict = {'time=': int(time_input), 'speed=': int(speed_input), 'weight=': int(weight_input)}
    result_string = library3.working_with_dict_from_input_walues(my_dict)
    print(result_string)


if __name__ == '__main__': 
    main()
    