from random import randint


class Account:
    def __init__(self,balance = 100):
        self.account_number = randint(0,9999999999)
        self.balance = float(balance)
        self.interest_rate = float(10)

    def deposit(self,amount):
        self.balance = self.balance + amount
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Cannot withraw more than the available balance")



class SavingsAccount(Account):
    def calculate_interest(self):
        interest = (self.balance/100 * self.interest_rate)
        self.balance = self.balance + interest
        print(f"The interset amount is: {interest}\n")
        print(f"The total amount after adding interest is: {self.balance}\n")
    

class CurrentAccount(Account):
    def calculate_interest(self):
        interest = (self.balance/100 * 5)
        self.balance = self.balance + interest
        print(f"The interset amount is: {interest}\n")
        print(f"The total amount after adding interest is: {self.balance}\n")

choice = 1
while choice == 1:
    account_type = int(input("Which type of account you want to create\n"
                         "1)  To create Savings Account\n"
                         "2)  To create Current Account\n"
                         "0)  Exit\n"))
    if account_type == 1:
        balance_input = input("Enter your account balance\n")
        ac = SavingsAccount(balance_input)

        acc_choice = 1
        while acc_choice != 0:
            acc_choice = int(input("1)  Deposit Amount\n"
                            "2)  Withdraw Amount\n"
                            "3)  Calculate Interest\n"
                            "4)  See Balance\n"
                            "0)  Exit\n"))
            
            if acc_choice == 1:
                deposit_amt = int(input("Enter the amount to be dposited\n"))
                ac.deposit(deposit_amt)

            if acc_choice == 2:
                withdraw_amt = int(input("Enter the amount to be withdrawn\n"))
                ac.withdraw(withdraw_amt)

            if acc_choice == 3:
                ac.calculate_interest()

            if acc_choice == 4:
                print(ac.balance)

    if account_type == 2:
        balance_input = input("Enter your account balance\n")
        ac = Account(balance_input)

        acc_choice = 1
        while acc_choice != 0:
            acc_choice = int(input("1)  Deposit Amount\n"
                            "2)  Withdraw Amount\n"
                            "3)  Calculate Interest\n"
                            "4)  See Balance\n"
                            "0)  Exit\n"))
            
            if acc_choice == 1:
                deposit_amt = int(input("Enter the amount to be dposited\n"))
                ac.deposit(deposit_amt)

            if acc_choice == 2:
                withdraw_amt = int(input("Enter the amount to be withdrawn\n"))
                ac.withdraw(withdraw_amt)

            if acc_choice == 3:
                ac.calculate_interest()

            if acc_choice == 4:
                print(ac.balance)

    if account_type == 0:
        choice = 0