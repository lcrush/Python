print("We are going to balance your checkbook.")
balance = int(input("How many transactions do you have? "))
beginning_balance= int(input('Enter beginning balance. '))

total = 0.0
transactions = 0.0
checkbook = [] # create an empty list

for balance in range(balance):
    temp= int(input("Enter transaction" + str(balance + 1) + ": "))
    checkbook.append(temp)
    total += checkbook[balance] #total = total + transaction

transaction = total - balance

print("The checkbook balance is " + str(total))

for balance in checkbook:
    print(balance)