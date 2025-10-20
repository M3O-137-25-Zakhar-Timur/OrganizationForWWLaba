import random
import math


a: int = random.randint(1, 10)
b: float = 0.1

rad: float = 5.0
pi: float = math.pi
l: float = 2*pi*rad
l_sokr: float = round(l,2)

#2
text: str = ' Hello, Python! '

replaceText = text.replace('!', '?')
UpText = text.upper()
stripText = text.strip()
LowText = stripText.lower()

TrueText: str = 'hello, python!'

print('1.1)', a)
print('1.2)', b)
print('1.3)', b + a)
print('1.4)', a - b)
print('1.5)', a * b)
print('1.6)', a/b)
print('1.7', l_sokr)

print("№2!!!")
print(text)
print(stripText)
print(replaceText)
print(UpText)
print(LowText)

if LowText == TrueText:
    print('Все верно!')

numbers = [7, 2, 5]
numbers.append(4)
numbers.insert(1, 10)
numbers.extend([1, 1, 1])
numbers.remove(7)
numbersPop = numbers.pop()
numbers.sort()
numbers.reverse()
num2 = numbers.count(2)
numIndex = numbers.index(1)

print('№3')
print(numbers)
print(numbersPop)
print(num2)
print(numIndex)

t = (1, 2, 3)
t2 = (4, 5)
t_t2 = t + t2
t_count = t2.count(3)
tIndex = t_t2.index(4)

print("№4")
print(t)
try: t[1] = 100
except: print('Произошла ошибка, т.к. производиться попытка изменения неизменяемого списка')
print(t_t2)
print(t_count)
print(tIndex)

values = [3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
unique_values_num = len(unique_values)
other = {2, 4, 5}
peresech = (unique_values & other)
objedinenie = (unique_values | other)
raz_u_o = unique_values - other
raz_o_u = other - unique_values

print('№5')
print(values)
print(unique_values)
print(unique_values_num)
print(peresech)
print(objedinenie)
print(raz_u_o)
print(raz_o_u)

scores = {"Alie": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
True_get = scores.get("Bob")
False_get = scores.get("Dave")
pop = scores.pop("Alie")
len = len(scores)
keys = scores.keys()
values = scores.values()

print('№6')
print(scores)
print(True_get)
print(False_get)
print(pop)
print(len)
print(keys)
print(values)

text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""

StripText = text.strip()
LowerText = StripText.lower()
Replace = LowerText.replace('!', '.')
SplitText = Replace.split('.')

text1 = 'Python is a powerful programming language.'\

print('№7')

print(StripText)
print(LowerText)
print(Replace)
print(SplitText)

text1 = 'Python is a powerful programming language.'
text1_split = text1.split()
text1_count = text1.count('Python')


print(text1_split)
print(text1_count)



