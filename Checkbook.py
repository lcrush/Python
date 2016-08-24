print("We are going to balance your checkbook.")
#balance = int(input("How many transactions do you have? "))
#beginning_balance= int(input('Enter beginning balance: $ '))

total = float(input("Enter a starting balance: $"))
#transactions = 0.0
#checkbook = [] # create an empty list

#for balance in range(balance):
    #temp= int(input("Enter transaction" + str(balance + 1) + ": "))
    #checkbook.append(temp)
    #total += checkbook[balance] #total = total + transaction

#transaction = total - balance

#print("The checkbook balance is " + str(total))

#for balance in checkbook:
    #print(balance)
    
numbers = []
limit = int(input("how many transactions do you have to enter: "))
    
for i in range (limit):
    temp = float(input("Enter a transaction amount: $"))
    numbers.append(temp)
    
for number in numbers:
    total = total + number
        
print("Ending total is $"+str(total))