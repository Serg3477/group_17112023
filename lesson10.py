import library
import constants


def main():
    #   Конвертація сантиметрів в дюйми
    santimeter_input = input("Введіть число у форматі 0.0: ")
    convert_result = library.convert_santimetres_to_inches(santimeter_input)
    print(convert_result)
    print("*" * 50)

    #  Отримання списку парних чисел із заданного списку чисел
    numbers = [12, 43, 57, 54, 89, 100, 102, 76, 32, 33, 81, 2, 345, 458]
    paired_numbers: int = library.get_paired_numbers(numbers)
    print("Добірка чисел: ")
    print(numbers)
    print("З них парні числа:")
    print(paired_numbers)
    print("*" * 50)

    #  Отримання рішення банку про видачу кредиту на іпотеку, виходячи із данних: місячний дохід та сума щомісячного    платежу

    salary_input = input("Введіть ваш місячний дохід: ")
    ipoteka_sum = input("Введіть загальну сумму кредиту по іпотеці: ")
    bank_result: bool = library.get_ipoteka_result(salary_input, ipoteka_sum)
    if bank_result is True:
        print(constants.BANK_YES)
    else:
        print(constants.BANK_NO)


if __name__ == '__main__':
    main()
