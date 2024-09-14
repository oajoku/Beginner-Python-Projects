#Band Name Generator

##Description:
This project generates a band name by taking user input for their city and pet name and combining them.

##Key Concepts:
1. String() function
2. String Concactenation
3. Input() function
4. Syntax Errors
5. Syntax Highlighting
6. Debugging
7. Indentation
8. Variables
9. Len() function

##How to Run:
1. Clone this repository.
2. Run the "band_name_generator.py" file using python.

##Code:

#Create a greeting for your program
print("Hello and welcome to the Band Name Generator!")

#Ask the user for the city that they grew up in and store it in a variable.
user_city = input("What city did you grow up in?\n")

#Ask the user for the name of a pet and store it in a variable.
user_pet = input("What is the name of your pet?\n") #I added the new line command so that the input cursor shows on a new line


#Combine the name of their city and pet and show them their band name.
print("Your band name could be :" + user_city + " " + user_pet)
