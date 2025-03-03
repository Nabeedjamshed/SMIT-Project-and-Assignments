class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Successfully deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if self.balance < amount:
            print("Insufficient balance for this withdrawal.")
            return

        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        print(f"Successfully withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def print_statement(self):
        if not self.transactions:
            print("No transactions to display.")
            return

        print(f"Account statement for {self.name}:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Final balance: {self.balance}")

    def add_transaction(self, description):
        self.transactions.append(description)
        try:
            with open(f"{self.name}_transactions.txt", "a") as file:
                for transaction in self.transactions:
                    file.write(f"{transaction}\n")
                file.write(f"Final Balance: {self.balance}\n\n")
        except IOError:
            print("Error writing to the transaction file.")
