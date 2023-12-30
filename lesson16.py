from abc import ABC, abstractmethod
from typing import Self
class Transport(ABC):
    items = []

    def __init__(
        self,
        brand: str,
        speed: int,
        mileage: int | float,
        fuel_volume: int | float,
        fuel_balance: int | float,
    ):
        self.items.append(self)
        self.brand = brand
        self.speed = speed
        self.mileage = mileage
        self.fuel_volume = fuel_volume
        self.fuel_balance = fuel_balance

    @abstractmethod
    def vehicle(self, other: Self):
        pass


class Auto(Transport):
    def __init__(self, passenger_capacity: int, airbag: bool) -> dict:
        super().__init__(passenger_capacity, airbag)
        self.passenger_capacity = passenger_capacity
        self.airbag = airbag

    def vehicle(self, fuel_volume: int | float, fuel_balance: int | float):
        if fuel_volume - fuel_balance != 0:
            total_fuel_volume = fuel_volume - fuel_balance
            print(
                f"Залишок у баку: {fuel_balance} літрів.\n"
                f"Об'єм баку: {fuel_volume} літрів.\n"
                f"Заправлено пального {total_fuel_volume} літрів, до повного баку."
            )
        print("Бак повний. Заправка не потрібна.")


class Motorcycle(Transport):
    def __init__(self, cradle: bool) -> dict:
        super().__init__(cradle)
        self.cradle = cradle

    def vehicle(
        self, other: Transport, fuel_volume: int | float, fuel_balance: int | float):
        his_fuel_need = other.fuel_volume - other.fuel_balance
        if self.fuel_volume > his_fuel_need:
            fuel_balance -= his_fuel_need
            his_total_fuel_value = other.fuel_balance + his_fuel_need
            print(
                f"У нас було у баку: {self.fuel_volume} літрів\n"
                f"Йому треба ще долити в бак: {his_fuel_need} літрів\n"
                f"Ми долили йому повний бак {his_total_fuel_value} літрів\n"
                f"У нас лишилося {fuel_balance}, додому якось доїдемо."
            )
