Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2+4
6
>>> 7/4
1.75
>>> 7/4.0
1.75
>>> 7.0/4.0
1.75
>>> 7 % 4
3
>>> 50%5
0
>>> 23 % 2
1
>>> 20 % 2
0
>>> 2**3
8
>>> 2 + 10 * 10 + 3
105
>>> (2+10)*(10+3)
156
>>> 0.1+0.2-0.3
5.551115123125783e-17
>>> (0.1 + 0.2) - 0.3
5.551115123125783e-17
>>> a = 5
>>> a = 10
a
>>> a
10
>>> a + a
20
>>> a = a + a
>>> a
20
>>> a = a + a
>>> a
40
>>> a = a + a
>>> a
80
>>> type(a)
<class 'int'>
>>> a = 3.1
>>> type(a)
<class 'float'>
>>> int = 4
>>> int
4
>>> my_income = 100
>>> tax_rate = 0.1
>>> my_taxes = my_income * tax_rate
>>> my_taxes
10.0
>>> message = 'hello'
>>> message[0]
'h'
>>> for ch in message:
	print(ch)

	
h
e
l
l
o
>>> message[1:3:2]
'e'
>>> print(message)
hello
>>> print('hello world')
hello world
>>> print('hello \nworld')
hello 
world
>>> print('hello \tworld')
hello 	world
>>> len('I am')
4
>>> mystring = 'Hello World'
>>> mystring[8]
'r'
>>> mystring[-2]
'l'
>>> mystring = 'abcdefghijk'
>>> mystring[2:]
'cdefghijk'
>>> mystring[:3]
'abc'
>>> mystring[3:6]
'def'
>>> mystring[1:3]
'bc'
>>> mystring[::]
'abcdefghijk'
>>> mystring[::2]
'acegik'
>>> mystring[0:-1]
'abcdefghij'
>>> mystring[0:]
'abcdefghijk'
>>> mystring [::-1]
'kjihgfedcba'
>>> for ch in mystring:
	print

	
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
>>> i = -1
>>> for ch in mystring:
	print(mystring[






	fdff

	fffg)_
	      
SyntaxError: invalid syntax
>>> i = -1
	      
>>> for i in range(-1, -len(mysring)):
	      print(mystring[i])

	      
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    for i in range(-1, -len(mysring)):
NameError: name 'mysring' is not defined
>>> for i in range(-1, -len(mystring)):
	      print(mystring[i])

	      
>>> i
	      
-1
>>> for i in range(-1, -len(mystring)):
	      print(i)

	      
>>> mystring[::-1]
	      
'kjihgfedcba'
>>> name = "Sam"
	      
>>> name[0] = 'P'
	      
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    name[0] = 'P'
TypeError: 'str' object does not support item assignment
>>> name = name[0] + name[1:]
	      
>>> name
	      
'Sam'
>>> name = 'P' + name[1:]
	      
>>> name
	      
'Pam'
>>> x = 'Hello World'
	      
>>> x + ' it is beautiful outside'
	      
'Hello World it is beautiful outside'
>>> letter = 'z'
	      
>>> letter*10
	      
'zzzzzzzzzz'
>>> x = 'Hello World'
	      
>>> x.upper()
	      
'HELLO WORLD'
>>> x
	      
'Hello World'
>>> x.split()
	      
['Hello', 'World']
>>> x.split('i')
	      
['Hello World']
>>> x.split('o')
	      
['Hell', ' W', 'rld']
>>> print('This is a string {}'.format('INSERTED')
	  )
	      
This is a string INSERTED
>>> print('The {} {} {}'.format('fox', 'brown', 'fix')
	  )
	      
The fox brown fix
>>> print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
	      
The quick brown fox
>>> print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
	      
The quick brown fox
>>> result = 100/777
	      
>>> result
	      
0.1287001287001287
>>> print('The result was {r}'.format(r = 'result'))
	      
The result was result
>>> print('The result was {r}'.format(r = result))
	      
The result was 0.1287001287001287
>>> print('The result was {r:1.3f}'.format(r = result))
	      
The result was 0.129
>>> print('The result was {r}'.format(r = round(result,2)))
	      
The result was 0.13
>>> name = 'Jose'
	      
>>> print(f'Hello, his name is {name}')
	      
Hello, his name is Jose
>>> name = 'Sam'
	      
>>> age = 3
	      
>>> print(f'{name} is {age} years old')
	      
Sam is 3 years old
>>> mylist = ['one', 'two', 'three']
	      
>>> print(mylist)
	      
['one', 'two', 'three']
>>> mylist[1]
	      
'two'
>>> mylist[1:]
	      
['two', 'three']
>>> another_list = ['four', 'five']
	      
>>> new_list = my_list + another_list
	      
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    new_list = my_list + another_list
NameError: name 'my_list' is not defined
>>> new_list = another_list + mylist
	      
>>> new_list
	      
['four', 'five', 'one', 'two', 'three']
>>> new_list[0] = 'ONE IN ALL CAPS'
	      
>>> new_list
	      
['ONE IN ALL CAPS', 'five', 'one', 'two', 'three']
>>> new_list
	      
['ONE IN ALL CAPS', 'five', 'one', 'two', 'three']
>>> new_list.sort()
	      
>>> new_list
	      
['ONE IN ALL CAPS', 'five', 'one', 'three', 'two']
>>> new_list.append('six')
	      
>>> new_list
	      
['ONE IN ALL CAPS', 'five', 'one', 'three', 'two', 'six']
>>> new_list.append('seven')
	      
>>> new_list
	      
['ONE IN ALL CAPS', 'five', 'one', 'three', 'two', 'six', 'seven']
>>> new_list.pop()
	      
'seven'
>>> new_list
	      
['ONE IN ALL CAPS', 'five', 'one', 'three', 'two', 'six']
>>> popped_item = new_list.pop()
	      
>>> popped_item
	      
'six'
>>> new_list
	      
['ONE IN ALL CAPS', 'five', 'one', 'three', 'two']
>>> new_list.pop(0)
	      
'ONE IN ALL CAPS'
>>> new_list
	      
['five', 'one', 'three', 'two']
>>> new_list = ['a', 'e', 'x', 'b', 'c']
	      
>>> num_list = [4,1,8,3]
	      
>>> new_list.sort()
	      
>>> new_list
	      
['a', 'b', 'c', 'e', 'x']
>>> num_list
	      
[4, 1, 8, 3]
>>> num_list.sort()
	      
>>> num_list
	      
[1, 3, 4, 8]
>>> num_list.reverse()
	      
>>> string = 'Cats are soft'
	      
>>> str_list = []
	      
>>> for ch in string: str_list.append(ch)

	      
>>> str_list.reverse()
	      
>>> str_list
	      
['t', 'f', 'o', 's', ' ', 'e', 'r', 'a', ' ', 's', 't', 'a', 'C']
>>> for ch in str_list: print(ch)

	      
t
f
o
s
 
e
r
a
 
s
t
a
C
>>> for ch in str_list: print(ch, new_line = '/')

	      
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    for ch in str_list: print(ch, new_line = '/')
TypeError: 'new_line' is an invalid keyword argument for this function
>>> my_dict = {'key1': 'value1', 'key2': 'value2'}
	      
>>> my_dict{'key1'}
	      
SyntaxError: invalid syntax
>>> my_dict['key1']
	      
'value1'
>>> prices_lookup = {'apple':2.99, 'orange':1.99, 'milk':5.80}
	      
>>> prices_lookup['milk']
	      
5.8
>>> d  = {'k1':123, 'k2':[0,1,2], 'k3':{'insidekey':100}}
	      
>>> d
	      
{'k1': 123, 'k2': [0, 1, 2], 'k3': {'insidekey': 100}}
>>> d['k2']
	      
[0, 1, 2]
>>> d['k3']['insidekey']
	      
100
>>> d = {'key1':['a','b','c']}
	      
>>> d['key1'][2]
	      
'c'
>>> d['key1'][2].upper()
	      
'C'
>>> d ={'k1':100, 'k2':200}
	      
>>> d
	      
{'k1': 100, 'k2': 200}
>>> d['k3'] = 300
	      
>>> d
	      
{'k1': 100, 'k2': 200, 'k3': 300}
>>> d['k1'] = 'NEW VALUE'
	      
>>> d
	      
{'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}
>>> d.keys()
	      
dict_keys(['k1', 'k2', 'k3'])
>>> d.values()
	      
dict_values(['NEW VALUE', 200, 300])
>>> d.items()
	      
dict_items([('k1', 'NEW VALUE'), ('k2', 200), ('k3', 300)])
>>> t = (1,2,3)
	      
>>> mylist = [1,2,3]
	      
>>> type(t)
	      
<class 'tuple'>
>>> type(mylist)
	      
<class 'list'>
>>> t  = ('one', 2)
	      
>>> t[0]
	      
'one'
>>> t[-1]
	      
2
>>> t = ('a', 'a', 'b')
	      
>>> t.count('a')
	      
2
>>> t.index('a')
	      
0
>>> t
	      
('a', 'a', 'b')
>>> mylist
	      
[1, 2, 3]
>>> mylist[0] = 'NEW'
	      
>>> mylist
	      
['NEW', 2, 3]
>>> t[0] = 'NEW'
	      
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    t[0] = 'NEW'
TypeError: 'tuple' object does not support item assignment
>>> myset = set()
	      
>>> myset
	      
set()
>>> myset.add(1)
	      
>>> myset
	      
{1}
>>> myset.add(2)
	      
>>> myset
	      
{1, 2}
>>> myset.add(2)
	      
>>> myset
	      
{1, 2}
>>> mylist=[1,1,1,1,1,2,2,2,2,2,3,3,3,3]
	      
>>> set*mylist)
	
SyntaxError: invalid syntax
>>> set(mylist)
{1, 2, 3}
>>> True
True
>>> False
False
>>> true
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> 1 > 2
False
>>> 1 == 1
True
>>> b = None
>>> b
>>> type(b)
<class 'NoneType'>
>>> 
