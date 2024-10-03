print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
#Created a new variable to calculate the percentage tip
#The percentage tip is the tip divided by 100, + 1
#1 represents 100% of the bill and the tip/100 is simply the %tip eg 0.12, which
#is simply 12/100.
percentage_tip = (tip/100)+1
# The round() function was used to round up the total bill and split it into to 2 decimal places. The total was 
# calculated by multiplying the bill to the percentage_tip / by the number of people splitting the total bill that was
# inputed by the user.

total = round(bill*percentage_tip/people,2)
#F-strings were used to put the number which is the total bill in a string to avoid errors from python.

print(f"Each person should pay ${total}")

