Python Input Exercise Attempt!🐍
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
