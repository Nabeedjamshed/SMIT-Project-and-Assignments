from account import create_account, check_balance
from transactions import deposit, withdraw, print_statement

def main():
    name = input("Enter your name to create an account: ")
    account = create_account(name)
    print(f"Account created for {name} with balance: {check_balance(account)}")

    while True:
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Print Statement")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account = deposit(account, amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account = withdraw(account, amount)
        elif choice == "3":
            print(f"Your current balance is: {check_balance(account)}")
        elif choice == "4":
            print_statement(account)
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
