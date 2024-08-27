Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
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
