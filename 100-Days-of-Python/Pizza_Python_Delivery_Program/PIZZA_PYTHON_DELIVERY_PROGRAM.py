print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_bill =0

#Using if/else/elif statements

if size == "L":
    total_bill = 25
    if pepperoni == "Y":
        total_bill += 3
    if extra_cheese == "Y":
        total_bill += 1
    print(f"Your final bill is: ${total_bill}.")

elif size == "M":
    total_bill = 20
    if pepperoni == "Y":
        total_bill += 3
    if extra_cheese == "Y":
        total_bill += 1
    print(f"Your final bill is: ${total_bill}.")

else:
    total_bill = 15
    if pepperoni == "Y":
        total_bill += 2
    if extra_cheese == "Y":
        total_bill += 1
    print(f"Your final bill is: ${total_bill}.")







