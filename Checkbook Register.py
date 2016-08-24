transactions = [] # date, description, amount

balance = float(input("Enter beginning balance: $"))

#print("Enter -1 as a date to end")

for i in range(1000):
    date = input("Enter date: ") # leave this as a string
    if date == str(-1):
        break
    else:
        transactions.append(date)
    transactions.append(input("Enter description: "))
    amount = (float(input("Enter amount: $")))
    balance += amount  # balance = balance + amount
    transactions.append(amount)

    
for i in range(0,len(transactions),3):
    print (transactions[i], transactions[i+1], transactions[i+2])
    
print("Ending Balance: $" +str(balance))