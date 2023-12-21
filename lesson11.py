import library2
import pytest
import constants2

def main():
    source_list = [2.78, 5, 9 ,89, 45.3, 66.11, 23.5, 77, 55, 90, 102, 56.01, 83, 256]
    print(constants2.SOURCE)
    print(source_list)
    string_list: str = library2.converting_numbers_to_string_list(source_list)
    print(constants2.RESULT_STR)
    print(string_list)
    print(constants2.SPACE)
    
    
    print(constants2.SOURCE)
    print(source_list)
    integer_list = library2.inserting_only_integer_list(source_list)
    print(constants2.RESULT_INT)
    print(integer_list)
    print(constants2.SPACE)


if __name__ == '__main__': 
    main()