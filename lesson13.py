def create_csv_to_write_logs(func: callable):
    def inner(*args):
        dict_time = input("Введіть час: ")
        dict_result = input("Введіть результат: ")
        with open('file_logs.csv', mode='a', encoding='utf-8') as file:
            file.write(f'{dict_time}; {dict_result}\n')
        with open('file_logs.csv', mode='r', encoding='utf-8') as file:
            result_reading_file = file.read()
        return func(*args)
    return inner

@create_csv_to_write_logs
def input_logs():
    print('В файл "file_logs.csv" записано успішно.')
    
input_logs()