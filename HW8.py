'''
Tracks an initial account balance
Tracks deposits in the account
Tracks withdrawals to the account
Prints out a current balance
Prints an error message if someone tries to withdraw more money than what is currently in the account
'''
class BankAccount():
    def user_menu(choice):
        if (choice == 0):
            return print("Thanks for banking today!")
        if (choice == 1):
            BankAccount.current_balance()
        if (choice == 2):
            BankAccount.current_balance()
            dep_amt = float(input("How much are you depositing?"))
            BankAccount.deposit_to_check(dep_amt, current_balance)
            BankAccount.current_balance()
        if (choice == 3):
            BankAccount.current_balance()
            withdraw_amt = float(input("How much would you like today?"))
            BankAccount.withdraw_from_check(withdraw_amt, current_balance)
            BankAccount.current_balance()

    def current_balance():
        try:
            (current_balance > 0)
        except (current_balance == 0):
            print("Your current balance is $0.00")
        print(f"Your current balance is {current_balance:.2f}.")
        return current_balance

    def deposit_to_check(dep_amt, current_balance):
        current_balance = current_balance + dep_amt
        return current_balance

    def withdraw_from_check(withdraw_amt, current_balance):
        assert (withdraw_amt > current_balance), "Insufficent funds."
        current_balance = (current_balance - withdraw_amt)
        return current_balance

if __name__ == "__main__":
    initial_balance = 0.00
    current_balance = 500.00
    choice = BankAccount.user_menu(int(input("What would you like to do? 1) Check Balance. 2) Deposit Funds. 3) Withdraw Funds. 0) Leave.")))

