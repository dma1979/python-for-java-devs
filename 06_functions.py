global actual_balance

def deposit(newAmt):
    amount = actual_balance + newAmt
    return amount

def withdraw(newAmt):
    amount = actual_balance - newAmt
    return amount

def checkBalance():
    return actual_balance

oneMoreTime = "N"
while (oneMoreTime == "N"):
    print("What is the name of your bank account holder?")
    aName = str(input())
    print("What is your account number?")
    aNumber = input()
    print("What is the initial balance?")
    actual_balance = int(input())
    print("What would you like to do today: W for Withdraw, D for Deposit and B for check balance.")
    action = input()
    if (action == "D"):
        dAmount = float(input("How much would you like to deposit today?"))
        balance = deposit(dAmount)
    if (action == "W"):
        wAmount = float(input("How much would you like to withdraw today?"))
        balance = withdraw(wAmount)
    if (action == "B"):
        balance = checkBalance()
    print("The amount in the bank is " + str(balance))
    oneMoreTime = input("Are you done? Y for yes and N for no")
