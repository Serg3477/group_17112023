import library3
import pytest
import constants3


def main():
    time_input = input("Введіть час в секундах: ")
    if int(time_input) <= 0:
        raise ValueError (constants3.ERR)
    speed_input = input("Введіть швидкість (м/сек): ")
    if int(speed_input) <= 0:
        raise ValueError (constants3.ERR)
    weight_input = input("Введіть вагу авто (кг): ")
    if int(weight_input) <= 0:
        raise ValueError (constants3.ERR)
    result = library3.working_with_dict_from_input_values(time_input, speed_input, weight_input)
    print(result)


if __name__ == '__main__': 
    main()
    