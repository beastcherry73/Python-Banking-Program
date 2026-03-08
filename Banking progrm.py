balance = float(0)
is_running = True

def check_balance(balance):
    print(f"Your current balance is: ${balance: .2f}")
def deposit():
    dep = float(input("How much would you like to deposit: $"))
    if dep < 0:
        print("Invalid input")
        return 0 # So that an error wouldn't occur
    else:
        return dep
def withdraw():
    wit = float(input("How much would you like to withdraw: $"))
    if wit > balance:
        print("Insufficient funds")
        return 0 # So that an error wouldn't occur
    elif wit < 0:
        print("Invalid input")
        return 0 # So that an error wouldn't occur
    else:
        return wit
def exit():
    pass

while is_running:
    print("Welcome to Banking Progrm")
    print("**************")
    print("Banking Program")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    service = input("How may I help you: ")
    if service == "1":
        check_balance(balance)
    elif service == "2":
        balance += deposit()
    elif service == "3":
        balance -= withdraw()
    elif service == "4":
        is_running = False
        print("Thank you!!")
    else:
        print("Invalid input")
