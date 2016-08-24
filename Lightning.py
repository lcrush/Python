speed_sound = 1100
mile = 5280
distance = 0

time = float(input("How many seconds between flash and sound? "))

distance = (speed_sound/mile) * time

print ("The lightning is: ",distance, "from you.")
