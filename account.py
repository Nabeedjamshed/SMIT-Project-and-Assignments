def create_account(name):
    account = {
        "name": name,
        "balance": 0.0,
        "transactions": []
    }
    return account

def check_balance(account):
    return account["balance"]
