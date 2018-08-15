'''
Tracks an initial account balance
Tracks deposits in the account
Tracks withdrawals to the account
Prints out a current balance
Prints an error message if someone tries to withdraw more money than what is currently in the account
'''
class BankAccount():
    initial_balance = 0.00
    balance = 500.00

    def user_menu(self):
        choice = 9999
        while (choice > 9000):
            choice = int(input("What would you like to do? 1) Check Balance. 2) Deposit Funds. 3) Withdraw Funds. 0) Leave."))
        if (choice == 0):
            return print("Thanks for banking today!")
        elif (choice == 1):
            self.current_balance()
        elif (choice == 2):
            self.current_balance()
            dep_amt = float(input("How much are you depositing?"))
            self.deposit_to_check(dep_amt)
            self.current_balance()
        elif (choice == 3):
            self.current_balance()
            withdraw_amt = float(input("How much would you like today?"))
            self.withdraw_from_check(withdraw_amt)
            self.current_balance()
        else:
            print("That's not something I can do. Please see a teller, or try again.")

    def current_balance(self):
        try:
            (self.balance > 0)
        except (self.balance == 0):
            print("Your current balance is $0.00")
        print("Your current balance is {:.2f}.".format(self.balance))

    def deposit_to_check(self, dep_amt):
        self.balance = self.balance + dep_amt

    def withdraw_from_check(self, withdraw_amt):
        assert (withdraw_amt < self.balance), "Insufficent funds."
        self.balance = (self.balance - withdraw_amt)

if __name__ == "__main__":
    ba = BankAccount()
    ba.user_menu()

