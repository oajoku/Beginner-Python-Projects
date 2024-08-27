Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Common Sytntax Problems
len("hell0")=5
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
"greek" = 4
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
#The problem occurs when you try to assign a value to a literal
len("juice")==6
False
#Misusing the assignement operator (=)
#Second Common sysntax problem is
#Misspelling, Missing or Missing a python keyword
#An example of misspelling a keyword is as follows
fro i in range(10):
    
SyntaxError: invalid syntax
#a common example of this is the use of "continue" or "break" outside of the loop. This could easily happen during development when you're implementing
#things and happened to move logic outside of a loop
#an example
fruit=["apple", "orange", "kiwi"]
if "kiwi" in fruit:
    print("kiwi found!")
    break
SyntaxError: incomplete input
#Another example is if you attempt to assign a python keyword to a variable or to use a keyword to define a function
pass=true
SyntaxError: invalid syntax
def pass():
    
SyntaxError: invalid syntax
#checking to see keywords in this version of python
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> #Missing parenthesis, brackets and quotes
>>> #An example is
>>> message='don't'
SyntaxError: unterminated string literal (detected at line 1)
>>> #correction
>>> message ='don\'t'
>>> message = "don't"
>>> message = "Onyinye is awesome!
SyntaxError: incomplete input
>>> #Become a bug bounty hunter
>>> #We're going to write a code from a different program to allow the user to spot bugs
>>> #The code is as follows
>>> import random # to allow me to generate a random number
>>> print("Guess a number between 1 and 10")
Guess a number between 1 and 10
>>> number = random.randit(1,10)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    number = random.randit(1,10)
AttributeError: module 'random' has no attribute 'randit'. Did you mean: 'randint'?
>>> number = random.randint(1,10)
>>> guess=input()
if guess==number:
>>> print(f'Correct!- the number was {number}')
Correct!- the number was 3
>>> else
SyntaxError: incomplete input
>>> 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
Traceback (most recent call last):
  File "/Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py", line 3, in <module>
    number = random.randit(1,10)
AttributeError: module 'random' has no attribute 'randit'. Did you mean: 'randint'?
>>> 6
6
>>> 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
Traceback (most recent call last):
  File "/Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py", line 3, in <module>
    number = random.randit(1,10)
AttributeError: module 'random' has no attribute 'randit'. Did you mean: 'randint'?
>>> 11
11
>>> 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
Traceback (most recent call last):
  File "/Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py", line 3, in <module>
    number = random.randit(1,10)
AttributeError: module 'random' has no attribute 'randit'. Did you mean: 'randint'?
>>> 8
8
>>> 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
7
Number:, 10, Guess: 7
Oops, the number was 10, not 7
>>> 10
10
>>> 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
2
Number: 1, Guess: 2
Number: <class 'int'>
Guess:  <class 'str'>
Oops, the number was 1, not 2

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
6
Number: 8, Guess: 6
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 8, not 6
8
8
4
4

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
1
Number: 8, Guess: 1
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 8, not 1
7
7

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
5
Number: 2, Guess: 5
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 2, not 5

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
8
Number: 5, Guess: 8
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 5, not 8

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
10
Number: 5, Guess: 10
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 5, not 10

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
6
Number: 9, Guess: 6
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 9, not 6

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
2
Number: 5, Guess: 2
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 5, not 2

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
9
Number: 7, Guess: 9
Number: <class 'int'>
Guess:  <class 'int'>
Oops, the number was 7, not 9

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
4
Number: 4, Guess: 4
Number: <class 'int'>
Guess:  <class 'int'>
Correct - the number was 4

======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
7
> /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py(9)<module>()
-> if guess==number:
(Pdb) 4
4
(Pdb) 9
9
(Pdb) 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
5
> /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py(9)<module>()
-> if guess==number:
(Pdb) 7
7
(Pdb) 0
0
(Pdb) 2
2
(Pdb) 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
> /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py(8)<module>()
-> guess=(input())
(Pdb) 9
9
(Pdb) 
======================================================== RESTART: /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py =======================================================
Guess a number between 1 and 10
> /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py(8)<module>()
-> guess=input()
(Pdb) 0
0
(Pdb) number
7
(Pdb) b
(Pdb) w
  <string>(1)<module>()
  /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/idlelib/run.py(164)main()
-> ret = method(*args, **kwargs)
  /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/idlelib/run.py(578)runcode()
-> exec(code, self.locals)
> /Users/onyinyeajoku/Documents/Python practice/Become a Bug Bounty Hunter!.py(8)<module>()
-> guess=input()
(Pdb) 3
3
(Pdb) 3
3
(Pdb) 6
6
(Pdb) 7
7
(Pdb) 9
9
