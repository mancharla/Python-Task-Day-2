account = {
    "name": "rakesh reddy",
    "balance": 5000
}

def deposit():
    amount = 2000
    account["balance"] = account["balance"] + amount
    print("After Deposit :", account["balance"])

def withdraw():
    amount = 1000
    account["balance"] = account["balance"] - amount
    print("After Withdraw :", account["balance"])

def check_balance():
    print("Current Balance :", account["balance"])

deposit()
withdraw()
check_balance()