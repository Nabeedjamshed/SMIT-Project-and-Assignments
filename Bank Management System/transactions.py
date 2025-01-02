def save_transaction_to_file(account):
    try:
        with open(f"{account['name']}_transactions.txt", "a") as file:
            for transaction in account["transactions"]:
                file.write(f"{transaction}\n")
            file.write(f"Final Balance: {account['balance']}\n\n")
    except IOError:
        print("Error writing to the transaction file.")

def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be positive.")
        return account

    account["balance"] += amount
    account["transactions"].append(f"Deposited: {amount}")
    save_transaction_to_file(account)
    print(f"Successfully deposited {amount}. New balance: {account['balance']}")
    return account

def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return account

    if account["balance"] < amount:
        print("Insufficient balance for this withdrawal.")
        return account

    account["balance"] -= amount
    account["transactions"].append(f"Withdrew: {amount}")
    save_transaction_to_file(account)
    print(f"Successfully withdrew {amount}. New balance: {account['balance']}")
    return account

def print_statement(account):
    if not account["transactions"]:
        print("No transactions to display.")
        return

    print(f"Account statement for {account['name']}:")
    for transaction in account["transactions"]:
        print(transaction)
    print(f"Final balance: {account['balance']}")
