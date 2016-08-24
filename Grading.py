print("We are going to calculate average grades for a quarter.")
grades = int(input("How many grades do you have?"))


total = 0.0
average = 0.0
gradebook = [] # create an empty list


for grade in range(grades):
    temp= int(input("Enter grade" + str(grade + 1) + ": "))
    gradebook.append(temp)
    total += gradebook[grade] #total = total + grade

average = total/grades

print("The average grade is " + str(average) + "%")

for grade in gradebook:
    print(grade)


