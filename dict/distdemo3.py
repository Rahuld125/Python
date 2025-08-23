accounts = {101: 50000, 102: 45000, 103: 55000}
print("Accounts details:")
print(accounts)
acid = int(input("Enter account id: "))
bal = int(input("Enter balance: "))
amt = accounts.get(acid)
if amt == None:
    accounts[acid] = bal
    print("New account added")
else:
    bal += amt
    accounts[acid] = bal
    print("Account updated")
print(accounts)
