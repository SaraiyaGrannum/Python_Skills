age = int(input("How old are you? "))

if age <= 0:
    print("Invalid age - positive numbers only! ")
    exit()
elif age <= 12:
    ticketPrice = 4
elif age >= 65:
    ticketPrice = 6
else:
    ticketPrice = 10

print("Your price of admission is $", ticketPrice)



