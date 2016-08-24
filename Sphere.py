import math
# print(math.pi)
r=input("Enter radius: ")

r= int(r)

#v=(4/3) * pi * (r**3)

v= (4/3) * math.pi * (r**3)

a= 4 * math.pi * r**2

print("Volume = ",v)

print("Surface area = ",a)