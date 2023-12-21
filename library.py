import typing
import constants


def convert_santimetres_to_inches (santimeter: int | float) -> float:
    converted_float_value = float(santimeter)
    converted_inch_value = round(converted_float_value/constants.INCH, 2)
    return converted_inch_value


def get_paired_numbers(numbers: list[int]) -> list[int]:
    paired_numbers: str =[]
    for key in range(len(numbers)):
        if numbers[key] % 2 == 0:
            paired_numbers.append(numbers[key])
    return paired_numbers



def get_ipoteka_result(salary_input: int, ipoteka_sum: int) -> bool:
    ipoteka_years = 25
    month_in_year = 12
    percent_of_month_income = 35
    salary_input_in_percents = int(salary_input)/100 * percent_of_month_income
    ipoteka_month = int(ipoteka_sum)/ ipoteka_years / month_in_year
    result: bool = salary_input_in_percents > ipoteka_month
    return result





