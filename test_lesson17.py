from lesson17 import CurrentAccount, CreditAccount
import random


class TestAddAccount:
    def test_add_current_accounts(self,  client2, current_account):
        client2.current_accounts.append(current_account)
        client2.current_accounts.append(current_account)
        assert len(client2.current_accounts) == 2

    def test_add_credit_accounts(self, client1, client2, credit_account):
        client2.credit_accounts.append(credit_account)
        client2.credit_accounts.append(credit_account)
        client1.credit_accounts.append(credit_account)
        assert len(client2.credit_accounts) == 2
        random.shuffle(client2.credit_accounts)


    def test_deposit_on_current_account(self, client2):
        for account in client2.current_accounts:
            if isinstance(account, CurrentAccount):
                account.deposit_money(2000)
                assert account.balance == 2000
                break

    def test_deposit_on_credit_account(self, client2):
        for account in client2.credit_accounts:
            if isinstance(account, CreditAccount):
                account.deposit_money(3000)
                assert account.balance == 3000
                break

    def test_withdraw_from_current_account(self, client2):
        for account in client2.current_accounts:
            if isinstance(account, CurrentAccount):
                account.withdraw_money(500)
                assert account.balance == 1500
                break


    def test_withdraw_from_credit_account(self, client2):
        for account in client2.credit_accounts:
            if isinstance(account, CreditAccount):
                account_before_withdraw = account.balance
                account.withdraw_money(1000)
                assert account.balance == account_before_withdraw - (1000 +(1000 * CreditAccount.percent_commission))
                break


    def test_transfer_from_client1_to_client2(self, client1, client2):
        client1_credit_account = 0
        client2_current_account = 0
        client1_credit_account_before = 0
        client2_current_account_before = 0
        float(client1_credit_account)
        float(client2_current_account)
        float(client1_credit_account_before)
        float(client2_current_account_before)
        for account in client2.current_accounts:
            if isinstance(account, CurrentAccount):
                client2_current_account = account
                client2_current_account_before = client2_current_account
                break
        for account in client1.credit_accounts:
            if isinstance(account, CreditAccount):
                client1_credit_account = account
                client1_credit_account_before = client1_credit_account
                account.make_transaction(client2_current_account, 1.33)
                break
        assert client1_credit_account == client1_credit_account_before - 1.33 - 1.33 * CreditAccount.percent_commission
        assert client2_current_account == client2_current_account_before + 1.33


















