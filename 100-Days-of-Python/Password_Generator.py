import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



passwords=[letters, numbers, symbols]
password_choice= random.choice(passwords)

letter_choice= str(random.choice(letters))
number_choice= str(random.choice(numbers))
symbols_choice = str(random.choice(symbols))

nr_letter=0
nr_number=0
nr_symbol=0

for password in passwords:
    for password in letter_choice:
        if nr_letters == 4:
            nr_letter+=4
            print({letter_choice})
    for password in numbers:
        if nr_symbols == 2:
            nr_symbol+=2
            print(number_choice)
    for password in symbols:
        if nr_symbols == 3:
            nr_symbol+=3
            print(symbols_choice)
else:
    print(f"This is your new password: {password_choice}")
