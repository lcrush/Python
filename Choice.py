print("1. mi-km 3. F-C")
print("2. ft-m  4. km-mi")
print("5. C-F   6. m-ft")
choice = int(input("=>"))
if choice == 1:
    mi = float(input("Enter miles:"))
    km = mi * 1.609
    print("km=: "+str(km))
elif choice ==2:
    feet = float(input("Enter feet:"))
    m = feet/3.281
    print("m=: "+str(m))
elif choice == 3:
    fahrenheit = float(input("Enter degrees in fahrenheit:"))
    celsius = (5/9) * (fahrenheit - 32)
    print("Temperature in celsius:"+str(celsius))
elif choice == 4:
    km = float(input("Enter km:"))
    miles = km/1.609
    print("miles=: "+str(miles))
elif choice == 5:
    celsius = float(input("Enter degrees in celsius:"))
    fahrenheit = (9/5 * celsius) + 32
    print("Temperature in fahrenheit:"+str(fahrenheit))
elif choice == 6:
    m = float(input("Enter m:"))
    feet = m * 3.281
    print("feet=: "+str(feet))    