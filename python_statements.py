my_list = [1,2,3,4,5,6,7,8,9,10]
#for jelly in my_list:
#    print('hello')

#for num in my_list:
#    if num % 2 == 0:
#        print(f'Even Number: {num}')
#    else:
#        print(f'Odd Number: {num}')

#list_sum = 0
#for num in my_list:
#    list_sum = list_sum + num
#    print(list_sum)

my_string = 'Hello World'
#for letter in my_string:
#    print(letter)
#for _ in my_string:
#    print('Cool!')

tup = (1,2,3)
#for item in tup:
#    print(item)

my_list = [(1,2), (3,4), (5,6), (7,8)]
#for (a,b) in my_list:
#    print(a)
#    print(b)

my_list = [(1,2,3), (5,6,7), (8,9,10)]
#for a,b,c in my_list:
#   print(b)

d = {'k1':1, 'k2':2, 'k3':3}
#for item in d:
#    print(item)
#for key,value in d.items():
#    print(key, value)

my_list = [1,2,3]
#for num in range(1,11,2):
#    print(num)

#index_count = 0
#for letter in 'abcde':
#    print(f'At index {index_count} the letter is {letter}')
#    index_count += 1

word = 'abcde'
#for letter in word:
#    print(word[index_count])
#    index_count += 1

#for index, letter in enumerate(word):
#    print(f'At index {index} the letter is {letter}')

my_list1 = [1,2,3]
my_list2 = ['a', 'b', 'c']
#for item in zip(my_list1, my_list2):
#    print(item)
#
#print(list(zip(my_list1, my_list2)))

#print('x' in my_list2)
#print('x' in ['x', 'y', 'z'])

#print(min(my_list1))

from random import shuffle, randint
my_list = [1,2,3,4,5,6,7,8,9,10]
#print(my_list)
#shuffle(my_list)
#print(my_list)
#print(randint(1,10))

#result = input('What is your name? ')
#print(f'Hello {result}')

#fav_num = int(input('Favorite Number? '))
#print(f'{fav_num}? Wow, me too!')

#my_string = 'hello'
#my_list = []
#for letter in my_string:
#    my_list.append(letter)

#print(my_list)

#my_list = [letter for letter in my_string]
#print(my_list)

#my_list = [letter for letter in 'word']
#print(my_list)

#my_list = [num**2 for num in range(0,11)]
#print(my_list)

#my_list = [x for x in range(0,11) if x%2==0]
#print(my_list)

#celsius = [0,10,20,43.5]
#farenheit = [9/5*temp+32 for temp in celsius]
#print(farenheit)

#results = [x if x%2==0 else 'ODD' for x in range(0,11)]
#print(results)

my_list = []
for x in [2,4,6]:
    for y in [100,200,300]:
        my_list.append(x*y)
print(my_list)