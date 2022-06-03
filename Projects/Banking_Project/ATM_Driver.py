
def main():
    account = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)

    # ATM Processes
    while True:  

        id = int(input("\nEnter Account pin: "))
        