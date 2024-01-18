from abc import ABC, abstractmethod
from typing import Self
import random
from decimal import Decimal

class Client:
    def __init__(self, name: str):
        self.name = name
        self.current_accounts = []
        self.credit_accounts = []



class BaseAccount(ABC):
    def __init__(self):
        self.number = random.randint(21321454544, 999999999999999)
        self.balance = 0

    def deposit_money(self, summa):
        self.balance += summa

    @abstractmethod
    def make_transaction(self, other: Self, summa: int | float):
        pass


    @abstractmethod
    def withdraw_money(self, withdraw_summa: int | float):
        pass


class CurrentAccount(BaseAccount):
    def make_transaction(self, other: BaseAccount, summa: int | float):
        if self.balance - summa < 0:
            print('Not enough money')
            return
        self.balance -= summa
        other.balance += summa

    def withdraw_money(self, withdraw_summa):
        if self.balance - withdraw_summa < 0:
            print('Not enough money')
            return
        self.balance -= withdraw_summa


class CreditAccount(BaseAccount):
    percent_commission = 10 / 100



    def make_transaction(self, other: BaseAccount, summa: int | float):
        if (self.balance - summa - (summa * self.percent_commission)) < 0:
            print('Not enough money')
            return
        self.balance -= summa + summa * self.percent_commission
        other.balance += summa

    def withdraw_money(self, withdraw_summa):
        if (self.balance - withdraw_summa - (withdraw_summa * self.percent_commission)) < 0:
            print('Not enough money')
            return
        self.balance -= withdraw_summa + withdraw_summa * self.percent_commission


class AccountOperations(BaseAccount):
    def check_balance(self, other) -> bool:
        check_balance_result = False
        if self.balance > 0 and other.balance > 0: check_balance_result = True
        return check_balance_result


