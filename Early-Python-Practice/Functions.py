Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Fom previous work
#There are five different types of built-in functions that python uses
#The abs function, #The Boole function, #The Eval function, #The exec function & The Range function
#The range function
#The first two paraameteres given to a range are called start and the stop
for x in range (0,5)
SyntaxError: incomplete input
for x in range (0,5):
    print (x)

    
0
1
2
3
4
print(list(0,5)):
    
SyntaxError: incomplete input
print(list(0,5))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(list(0,5))
TypeError: list expected at most 1 argument, got 2
print(list(range(0,5)))
[0, 1, 2, 3, 4]
count_by_two = list(range(0,30,2))
print(count_by_two)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
#Example
#We Will write a program that calcuklates the sum of all the even numbers from 1 to 100. Thus even the first even number would be 2, and the last one would be 100.
#solution
even_numbers =list(range(2,100,2))
eval(even_numbers + even_numbers)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    eval(even_numbers + even_numbers)
TypeError: eval() arg 1 must be a string, bytes or code object
eval(even_numbers + even_numbers):
    
SyntaxError: incomplete input
even_numbers =list(range(2,100,2))

eval(even_numbers+ 2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    eval(even_numbers+ 2)
TypeError: can only concatenate list (not "int") to list
>>> even_numbers =list(range(2,100,2))
>>> print(even_numbers)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> #Correction
>>> even_sum=0
>>> for number in range(2,101,2):
...     #print(number)
...     even_sum+=number
...     print(even_sum)
... 
...     
2
6
12
20
30
42
56
72
90
110
132
156
182
210
240
272
306
342
380
420
462
506
552
600
650
702
756
812
870
930
992
1056
1122
1190
1260
1332
1406
1482
1560
1640
1722
1806
1892
1980
2070
2162
2256
2352
2450
2550
