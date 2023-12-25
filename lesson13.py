def create_csv_to_write_logs(func: callable):
    def inner(dict_time, dict_result):
        result = func(dict_time, dict_result)
        print(result)
    return inner


def input_logs(dict_time: str, dict_result: str):
    with open('file_logs.csv', mode='a', encoding='utf-8') as file:
        file.write(f'{dict_time}; {dict_result}\n')
    with open('file_logs.csv', mode='r', encoding='utf-8') as file1:
        result_reading_file = file1.read()
    return result_reading_file

    
input_logs = create_csv_to_write_logs(input_logs)
dict_time = input("Введіть час: ")
dict_result = input("Введіть результат: ")
input_logs(dict_time, dict_result)
   
     