from main_program import Account, Cash, Momo
from main_program import mainProgram
import unittest
import Operations
from unittest.mock import patch


class TestExpensesFunctionality(unittest.TestCase):
    def test_spend_momo(self):
        # Test what happens if the user records an expense which was done using momo account
        ac = Account(10000)
        self.assertEqual(ac.spend(4000), 6000)

    def test_spend_bank_account(self):
        # Test the outcome when a user records an expense which was done using bank account
        bank = Account(1000000)
        self.assertEqual(bank.spend(10000), 990000)
        print("New bank balance =", bank.balance)

    def test_negative_amount(self):
        # Test the outcome when a user records a negative price of expense. It raises a valueerror
        bank_ac = Account(10000)
        with self.assertRaises(ValueError):
            bank_ac.spend(-100)

    def test_spend_cash_on_hand(self):
        # Test the outcome when a user records an expense which was done using cash
        cash = Account(5000)
        self.assertEqual(cash.spend(4000), 1000)
        print("New cash balance =", cash.balance)

    def test_spend_cash(self):
        # Test that the spend function actually checks for the correct answer
        cash = Account(50000)
        self.assertNotEqual(cash.spend(40000), 1000)


class TestIncomeFunctionality(unittest.TestCase):
    def test_add_income_momo(self):
        # Test what happens if the user records an income into momo account
        momo = Account(0)
        self.assertEqual(momo.earnings(20000), 20000)
        print("New momo balance after adding income=", momo.balance)

    def test_add_income_cash(self):
        # Test what happens if the user records an income into cash account
        cash = Account(125000)
        self.assertEqual(cash.earnings(25000), 150000)
        print("New cash balance after adding income=", cash.balance)

    def test_add_income_bank(self):
        # Test what happens if the user records an income into bank account
        bank = Account(60000)
        self.assertEqual(bank.earnings(20), 60020)
        print("New bank balance after adding income=", bank.balance)

    def test_negative_amount(self):
        # Test the outcome when a user records a negative price of expense. It raises a valueerror
        momo_ac = Account(1000)
        with self.assertRaises(ValueError):
            momo_ac.earnings(-20000)


class TestTransferFunctionality(unittest.TestCase):
    def test_transfer_momoToCash(self):
        # Test the outcome of transferring from Momo account to cash account
        momo = Account(10000)
        cash = Account(50000)
        amount = 5000
        self.actual = momo.transfer(amount, momo, cash)
        self.expected = [5000, 55000]

        self.assertListEqual(self.actual, self.expected)

    def test_transfer_momoToBank(self):
        # Test the outcome of transferring from Momo account to bank account
        momo = Account(500)
        bank = Account(0)
        amount = 500
        self.actual = momo.transfer(amount, momo, bank)
        self.expected = [0, 500]

        self.assertListEqual(self.actual, self.expected)

    def test_transfer_cashToBank(self):
        # Test the outcome of transferring from cash account to bank account
        cash = Account(250000)
        bank = Account(100000)
        amount = 200

        self.actual = cash.transfer(amount, cash, bank)
        self.expected = [249800, 100200]

        self.assertListEqual(self.actual, self.expected)

    def test_transfer_same(self):
        # Test the outcome of transferring from and to the same account
        momo = Account(10000)
        amount = 5000
        with self.assertRaises(ValueError):
            momo.transfer(amount, momo, momo)

    def test_transfer_insufficient(self):
        # Test the outcome of transferring from momo account with insufficient balance
        momo = Account(1000)
        cash = Account(0)
        amount = 50000
        with self.assertRaises(ValueError):
            momo.transfer(amount, momo, cash)


class Test_verify_password_functionality(unittest.TestCase):
    def test_pwd(self):
        # Checks if the program catches a password that does not have a special character
        with patch('builtins.input', return_value="Hell0123"):
            assert Operations.Check_password_testing() == "Weak password, please consider including at least one special character; !@#$%^&*"

    def test_pwd2(self):
        # Checks if the program catches a password that does not have atleast one lowercase character
        with patch('builtins.input', return_value="HELLO0123!"):
            assert Operations.Check_password_testing() == "Weak password, please consider including at least one lowercase letter"

    def test_pwd3(self):
        # Checks if the program runs well if a user inputs a valid password that meets all requirements
        with patch('builtins.input', return_value="Hell0123!"):
            assert Operations.Check_password_testing() == "Valid password"

    def test_pwd4(self):
        # Checks if the program catches a password that does not have atleast one number
        with patch('builtins.input', return_value="MyPassword!!"):
            assert Operations.Check_password_testing() == "Weak password, please consider including at least one number"

    def test_pwd5(self):
        # Checks if the program catches a password that does not have atleast one uppercase character
        with patch('builtins.input', return_value="my100password!!"):
            assert Operations.Check_password_testing() == "Your password is weak, please consider including at least one UPPERCASE letter"

    def test_pwd6(self):
        # Checks if the program catches a password that does not have 8 characters
        with patch('builtins.input', return_value="Hi12!"):
            assert Operations.Check_password_testing() == '''Please enter a valid password.\nPassword should contain at least 8 characters, one upper and lower case letters, a number, and a special character'''


class Test_verify_email_functionality(unittest.TestCase):
    def test_email(self):
        # Checks if the program catches an email without the "@"
        with patch('builtins.input', return_value="myemail.com"):
            assert Operations.Check_email_testing() == "Invalid Email, Please enter a correct email address"

    def test_email2(self):
        # Checks if the program runs well if a user inputs a valid password that meets all requirements
        with patch('builtins.input', return_value="clarekanja@gmail.com"):
            assert Operations.Check_email_testing() == "Valid Email"

    def test_email3(self):
        # Checks if the program catches an email without the ".com"
        with patch('builtins.input', return_value="f.mukantwari@alustudent"):
            assert Operations.Check_email_testing() == "Invalid Email, Please enter a correct email address"

    def test_email4(self):
        # Checks if the program runs well if a user inputs a valid password that meets all requirements
        with patch('builtins.input', return_value="f.mukantwari@alustudent.com"):
            assert Operations.Check_email_testing() == "Valid Email"

    def test_email5(self):
        # Checks if the program catches an email without the a string before the @... and .com
        with patch('builtins.input', return_value="@gmail.com"):
            assert Operations.Check_email_testing() == "Invalid Email, Please enter a correct email address"


if __name__ == '__main__':
    unittest.main()