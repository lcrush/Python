total = 0
total = total+89
total = total + 42
total = total + 36

numbers = [89, 42, 36]

average = total/3
print(total, average)

total= 0

for number in numbers:
    total = total + number
    
print (total)

total = 0

#n1 = int(input("Enter a number: "))
#n2 = int(input("Enter a number: "))
#n3 = int(input("Enter a number: "))

#numbers = []
#for i in range(3):
    #temp = int(input("enter a number: "))
    #numbers.append(temp)
    
#print(numbers)

total = float(input("Enter a starting value: "))

numbers = []
limit = int(input("how many numbers do you have to enter: "))

for i in range (limit):
    temp = float(input("enter a number: "))
    numbers.append(temp)

for number in numbers:
    total = total + number
    
print("Ending total is $", total)