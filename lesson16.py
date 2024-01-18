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
    def refueling(self, fuel_volume: int | float, fuel_balance: int | float):
        pass

    @abstractmethod
    def fuel_share(self, other: Self, fuel_volume: int | float, fuel_balance: int | float):
        pass


class Auto(Transport):
    def __init__(self, brand, speed, mileage, fuel_volume, fuel_balance,
        passenger_capacity: int,
        airbag: bool) -> dict:
        super().__init__(brand, speed, mileage, fuel_volume, fuel_balance)
        self.passenger_capacity = passenger_capacity
        self.airbag = airbag


    def refueling(self, fuel_volume: int | float, fuel_balance: int | float):
        if fuel_volume - fuel_balance != 0:
            total_fuel_volume = fuel_volume - fuel_balance
            print(
                f"Залишок у баку: {fuel_balance} літрів.\n"
                f"Об'єм баку: {fuel_volume} літрів.\n"
                f"Заправлено пального {total_fuel_volume} літрів, до повного баку."
            )
            fuel_balance += total_fuel_volume
        print("Бак повний. Заправка не потрібна.")


    def fuel_share(self, other: Self, fuel_volume: int | float, fuel_balance: int | float):
        his_fuel_need = other.fuel_volume - other.fuel_balance
        if self.fuel_volume > his_fuel_need:
            fuel_balance -= his_fuel_need
            his_total_fuel_balance = other.fuel_balance + his_fuel_need
            print(
                f"У нас було у баку: {self.fuel_volume} літрів\n"
                f"Йому треба ще долити в бак: {his_fuel_need} літрів\n"
                f"Ми долили йому повний бак {his_total_fuel_balance} літрів\n"
                f"У нас лишилося {fuel_balance} літрів."
            )
            other.fuel_balance = his_total_fuel_balance


class Motorcycle(Transport):
    def __init__(self,brand, speed, mileage, fuel_volume, fuel_balance, cradle: bool) -> dict:
        super().__init__(brand, speed, mileage, fuel_volume, fuel_balance,)
        self.cradle = cradle


    def refueling(self, fuel_volume: int | float, fuel_balance: int | float):
        if fuel_volume - fuel_balance != 0:
            total_fuel_volume = fuel_volume - fuel_balance
            print(
                f"Залишок у баку: {fuel_balance} літрів.\n"
                f"Об'єм баку: {fuel_volume} літрів.\n"
                f"Заправлено пального {total_fuel_volume} літрів, до повного баку."
            )
            fuel_balance += total_fuel_volume
        print("Бак повний. Заправка не потрібна.")


    def fuel_share(self, other: Self, fuel_volume: int | float, fuel_balance: int | float):
        his_fuel_need = other.fuel_volume - other.fuel_balance
        if self.fuel_volume > his_fuel_need:
            fuel_balance -= his_fuel_need
            his_total_fuel_balance = other.fuel_balance + his_fuel_need
            print(
                f"У нас було у баку: {self.fuel_volume} літрів\n"
                f"Йому треба ще долити в бак: {his_fuel_need} літрів\n"
                f"Ми долили йому повний бак {his_total_fuel_balance} літрів\n"
                f"У нас лишилося {fuel_balance} літрів."
            )
            other.fuel_balance = his_total_fuel_balance

