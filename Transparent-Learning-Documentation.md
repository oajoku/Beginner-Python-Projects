Python Input Exercise Attempt #1!🐍
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Overview
This exercise was an attempt to practice capturing user inputs, performing simple string transformations, and producing results using Python's input() method. The idea was to develop a straightforward application that would ask the user for their name, age, and salary before understandably returning the data. As anticipated, I ran into a few problems that prevented the application from working. 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Code Attempt🟨
Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Input exercise
s=input()
Python is fun!
s
'Python is fun!'
message=input(What's your name?")
              
SyntaxError: incomplete input
message=input("What's your name?")
              
What's your name? Onyinye
message
              
' Onyinye'
input('What is your name?')
              
What is your name? Onyinye
' Onyinye'
#Input function exercise
              
input('How many characters are in your name?')
              
How many characters are in your name? Seven
' Seven'
print('There are'+ input, len())
              
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print('There are'+ input, len())
TypeError: can only concatenate str (not "builtin_function_or_method") to str
len(Onyinye)
              
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    len(Onyinye)
NameError: name 'Onyinye' is not defined
len(input)
              
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    len(input)
TypeError: object of type 'builtin_function_or_method' has no len()
input('How many characters are in your name?')
              
How many characters are in your name? 7
' 7'
input('What is your name?')
              
What is your name? Onyinye
' Onyinye'
j= input('How many characters are in your name?')
              
How many characters are in your name?
w=input('What is your name?')
              
What is your name?
len('j')
              
1
What is your name?Onyinye
              
SyntaxError: invalid syntax
w=input('What is your name?')
              
What is your name? Onyinye
j=input('How many characters are in your name')
              
How many characters are in your name 7
len('j')
              
1
print('j')
              
j
#Solution
              
input('What is your name?')
              
What is your name? Onyinye
' Onyinye'
len('Onyinye')
              
7
print( len( input('What is your name?) ) )
                  
SyntaxError: incomplete input
print( len( input('What is your name?') ) )
                  
What is your name? Onyinye
8
print( len( input("What is your name?") ) )
                  
What is your name? Ellla
6
input('72')
                  
72
''
#Exercise
                  
#Write a program that asks the user to enter his or her name, age and income, then display the value entered.
                  
name=input('What is your name?')
                  
What is your name? Maddy
What is your name? Maddy
                  
SyntaxError: invalid syntax
name=input('What is your name?')
                  
What is your name? Maddy
age=input('How old are you?')
                  
How old are you?26
income=input('How much do you earn?')
                  
How much do you earn?
print('name' +\n + 'age' +\n + 'income')
                  
SyntaxError: unexpected character after line continuation character
print('name' \n'age' \n'income')
                  
SyntaxError: unexpected character after line continuation character
print('name:' 'age:' 'income:')
                  
name:age:income:
>>> name:age:income:
...                   
SyntaxError: invalid syntax
>>> print('name')
...                   
name
>>> #Correction
...                   
>>> #Get the user's name, age and income
...                   
>>> name=input('What is your name?')
...                   
What is your name?
>>> age=int(input('How old are you?)
...               
SyntaxError: incomplete input
>>> age=int(input('How old are you?')
... income=float(input('How much do you earn?')
...              
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> age=int(input('How old are you?')
... #Display the data
... print('Display information below:')
...         
SyntaxError: '(' was never closed
>>> age=int(input('How old are you?'))
...         
How old are you?
Traceback (most recent call last):
  File "<:#51>", line 1, in <module>
    age=int(input('How old are you?'))
ValueError: invalid literal for int() with base 10: ''
>>> income=float(input('How much do you earn?'))
...         
How much do you earn?
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    income=float(input('How much do you earn?'))
ValueError: could not convert string to float: ''
>>> print('Here is the data you entered:')
...         
Here is the data you entered:
>>> print('name', name)
...         
name 
>>> print('age' age)
...         
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('age', age)
...         
age 26
>>> print('income', income)
...         
income 
>>> message=input('How much money did you spend today?')
...         
How much money did you spend today? 2000
>>> print('message')
...         
message
>>> print('message')
...         
message
>>> print('message', message)
...         
message  2000
>>>
--------------------------------------------------------------------------------------------------------------------------------------------

Issues Encountered🟥
1. Syntax Errors: Missing or incorrectly positioned parentheses and quote marks resulted in several syntax mistakes.
2. Incorrect Data Type Handling: When attempting to merge a string using a built-in function or method, an error was encountered. Print('There are' + input, len(), for instance) resulted in a TypeError.
3. Unintentional Outputs: During execution, the program did not behave as anticipated, yielding wrong values or displaying syntactic mistakes.
--------------------------------------------------------------------------------------------------------------------------------------------

Lessons Learned🟩
1. Proper Syntax: When working with string inputs and functions, it's important to closely monitor the syntax, particularly when it comes to quote marks and parentheses.
2. Data Type Management: To prevent problems such as TypeError, it's critical to comprehend the distinctions between strings, integers, and other data types.
3. Debugging: SyntaxError and TypeError error messages offer helpful tips for fixing the code.
--------------------------------------------------------------------------------------------------------------------------------------------

Next Steps❗
1. Rewrite the code and try again: I'm going to make some changes to the data type handling and syntax and then try the exercise again.
2. Further Learning: To strengthen my comprehension and steer clear of similar errors in the future, I will go over the fundamental grammar and functions of Python.

********************************************************************************************************************************************
Python Exercise #2🐍!
--------------------------------------------------------------------------------------------------------------------------------------------
Overview
This documentation covers the fundamental string operations, escape characters, string formatting, and more that I learned while working with Python strings. The exercises show you how I handled strings in many situations, including multiple-line strings, escape characters, and formatting techniques. This was a tough exercise for me, and I encountered several challenges.
--------------------------------------------------------------------------------------------------------------------------------------------
Code Attempt🟦
#STRINGS
sales='1000'
type(sales)
<class 'str'>
sales=1000
type(sales)
<class 'int'>
#using escape characters in python
message='don't forget to save
SyntaxError: invalid syntax
message="don't forget to save"
print(message)
don't forget to save
#OR
message='don\'t forget to save'
print(message)
don't forget to save
#The esacape character is used to differentiate the single and double quotes to python
#Newlines
d="Onyinye is gorgeous\nShe is a hottie as well
SyntaxError: incomplete input
d="Onyinye is gorgeous\nShe is a hottie as well"
print(d)
Onyinye is gorgeous
She is a hottie as well
#Tab Escape Character
e="I\tLove\tMe\tLOL
SyntaxError: incomplete input
e="I\tLove\tMe\tLOL"
print(e)
I	Love	Me	LOL
#Raw Strings
o=r"One\nTwo!"
print(o)
One\nTwo!
#Raw strings basically print out the exact same statment without implementing the escape character
#Multi line strings
print("""Hey there
My name is Onyinye Ajoku
I am 22 years old """)
Hey there
My name is Onyinye Ajoku
I am 22 years old 
#Typecasting
str(2.2)
'2.2'
#The STR funstion is used to convert integers or floats to strings
#Exercise
a="Hello"
b="World"
c="""Hello World"""
print(c)
Hello World
#In this exercise, I am supposed to create two variables and join them together
#String Indexing
#An example includes
a='apple'
a[0]
'a'
a[2]
'p'
a[4]
'e'
#OR
a[len (a) -1]
'e'
#len is a built in function used to get the length of a string
#negtive indices
a[-1]
'e'
a[-3]
'p'
a[-len(a)]
'a'
#String slicing
d='avocado'
d[1:4]
'voc'
d[:2]
'av'
d[:5]
'avoca'
d[3:]
'cado'
d[:3]
'avo'
d[7:]
''
d[6:]
'o'
d[:]
'avocado'
d[2:len(d)]
'ocado'
d[-5:-1]
'ocad'
#String Concatenation -- This is basically the joining of strings
a='sing'
b='robot'
c='loser'
a+b+c
'singrobotloser'
#OR
print('Loser' + 'Jerk')
LoserJerk
#I joined the above strings using the plus sign
#Joining strings using the multiplication operator
d=10
c*d
'loserloserloserloserloserloserloserloserloserloser'
print('turning'.upper())
TURNING
cheat='BORING'
print(cheat.lower())
boring
ord('s')
115
#It will return a unicode function
ord('')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
32
ord('+')
43
chr(97)
'a'
chr(28)
'\x1c'
e='I love myself very much'
len(e)
23
str(22.9)
'22.9'
#String formatting
#Using the % operator
print('My name is %s and my weight is %d kg'%('Onyinye', 62))
My name is Onyinye and my weight is 62 kg
print('My name is {0:s} and my weight is {1:d} kg'.format('Onyinye', 62))
My name is Onyinye and my weight is 62 kg
#If you do not wish to format the string, you can simply write
print('My name is {} and my weight is {} kg'.format('Onyinye',62))
My name is Onyinye and my weight is 62 kg
#Using f-stirngs
name="Hillary"
"Hello %s."
'Hello %s.'
"Hello %s." %name
'Hello Hillary.'
age=10
"Hello %s. You are %s."%(name,age)
'Hello Hillary. You are 10.'
#String formatting involving many variables
first_name="Hillary"
last_name="Ajoku"
age=10
profession="Student"
"Hello, %s %s. You are %s years old. You are a %s." %(first_name, last_name, age, profession)
'Hello, Hillary Ajoku. You are 10 years old. You are a Student.'
#OR
"Hello {} {}. You are {} years old. You are a {}.".format (first_name, last_name, age)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    "Hello {} {}. You are {} years old. You are a {}.".format (first_name, last_name, age)
IndexError: Replacement index 3 out of range for positional args tuple
#Using f strings
"fHello, {name}. you are {age} years old. You are a {profession}."
'fHello, {name}. you are {age} years old. You are a {profession}.'

#OR
F"Hello, {first_name}. you are {age} years old. You are a {profession}."
'Hello, Hillary. you are 10 years old. You are a Student.'
#arbitrary expressions
>>> f"{2*30}"
'60'
>>> f"{first_name*7}"
'HillaryHillaryHillaryHillaryHillaryHillaryHillary'
>>> #Multi line expressions using the f string
>>> message=(
...     f"hello{name}."
...     f"You are {age} years old."
...     )
>>> message
'helloHillary.You are 10 years old.'
>>> #String exercises
>>> first_name="Tamiko"
>>> last_name="Bellingham"
>>> #uSING F STRINGS
>>> f"Hi there {first_name} {last_name}."
'Hi there Tamiko Bellingham.'
>>> #Print () Formatting methods
>>> first='Lulu'
>>> last='John'
>>> age=36
>>> message="Hello Mrs %s, I try to improve my computer skills by learning python." %last
>>> print(message)
Hello Mrs John, I try to improve my computer skills by learning python.
>>> print("My full name is %s %s." %(first, last))
My full name is Lulu John.
>>> print("I am %d years old." %(age))
I am 36 years old.
>>> print("The value of pi is approximately: 1.2%f." %(3.1415))
The value of pi is approximately: 1.23.141500.
>>> The value of pi is approximately: 1.23.141500.#error
SyntaxError: invalid syntax
>>> print("The value of pi is approximately %1.2f."%(3.1415))
The value of pi is approximately 3.14.
>>> print("My name is %s, and I am %d years old. i live in Canada."%("Chuckwukaima", 29))
My name is Chuckwukaima, and I am 29 years old. i live in Canada.
>>> #Using the second formatting method, which is the string format method
>>> print('My name is {x}.'  .format(x='Levi'))
My name is Levi.
>>> print("My name is {x} and I am {y} years old.".format(x="Levi", y=28))
My name is Levi and I am 28 years old.
>>> message=f'Hello, my name is {name}{last} and i spend my free tim learning python'
>>> print(message)
Hello, my name is HillaryJohn and i spend my free tim learning python
>>> #RECEIPT PRINTING PROGRAM
>>> #Create a product and price for three items
>>> p1_name, p1_price="Oranges", 5.90
>>> p2_name, p2_price="Shampoo", 3.70
>>> p3_name, p3_price="Olive oil", 9.50
>>> 
>>> #Create a company name and information
>>> company_name="golden corner"
>>> company_name="golden corner"
>>> company_address="2 Mandilara St"
>>> company_city='Rodos, Gr"
SyntaxError: incomplete input
>>> company_city="Rodos, Gr"
>>> 
>>> #declare ending message
>>> message= "Thanks for shopping with us today!"
>>> 
>>> #Create a top broder
>>> print("*" *50)
**************************************************
>>> 
>>> #Print company information first using format
>>> print("\t\t{}".format(company_name
--------------------------------------------------------------------------------------------------------------------------------------------

Issues Encountered🟥
1. Syntax Errors: Using multi-line strings and escape characters caused me to run into syntax errors. Syntax mistakes or omissions were frequently the cause of these issues. I feel like I'm always having trouble with this.
2. Formatting Problems: Several formatting techniques failed to yield the desired outcomes; for example, the format() method raised an index error. Being a beginner, I'm still learning how to use the vast amount of information in Python's format section.
3. Inconsistent Output: Typos or missing code caused some escape characters, such as \n and \t, to not appear as intended. Unfortunately, it is not possible to go back and fix typos in the code once it has been written and the "enter/return" key has been pushed.
--------------------------------------------------------------------------------------------------------------------------------------------

Lessons Learned🟩
1. Comprehending Escape Characters: This exercise taught me how to handle special characters in strings by using escape characters.
2. String Formatting Techniques: I looked into a variety of string formatting techniques, such as f-strings, format(), and the % operator. Every technique has a set of use cases and syntax. I still have trouble with the f-strings in particular, and I need to practice more to get the hang of it.
3. Error Handling: I became more adept at seeing and fixing syntactic mistakes as well as better comprehending error messages. I have more work to do and I'm not flawless yet.
--------------------------------------------------------------------------------------------------------------------------------------------

Next Steps❗
1. Investigate Further String Methods: I'll work on more complex string techniques, such as splitting and string replacement. My string methods will hopefully get better as I continue to progress.
2. Work on Bigger Projects: To explore how these ideas fit into actual situations, I intend to use string handling in bigger projects. Naturally, I'll do this after finishing more challenging Python courses.
3. Examine Documentation Practices: I will improve my documentation techniques to guarantee accuracy and comprehensiveness in records going forward.
--------------------------------------------------------------------------------------------------------------------------------------------

Python Exercise #3🐍!
--------------------------------------------------------------------------------------------------------------------------------------------
Overview

In this practice session, I worked on basic Python operations, such as arithmetic calculations, variable assignments, and Boolean comparisons. Below are the details of the code snippets and their outputs.
--------------------------------------------------------------------------------------------------------------------------------------------

Code Attempt🟦




