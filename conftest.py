import pytest

from lesson17 import Client, CurrentAccount, CreditAccount, AccountOperations

@pytest.fixture(scope='class')
def current_account() -> CurrentAccount:
    instance = CurrentAccount()
    return instance

@pytest.fixture(scope='class')
def credit_account() -> CreditAccount:
    instance = CreditAccount()
    return instance

@pytest.fixture(scope='class')
def client1() -> Client:
    instance = Client(name='Alex')
    return instance

@pytest.fixture(scope='class')
def client2() -> Client:
    instance = Client(name='Jack')
    return instance
