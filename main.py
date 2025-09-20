import copy
import math
from idlelib.replace import replace
from itertools import count

from PIL.ImImagePlugin import number
from numpy.core.defchararray import startswith, endswith

print("---1---")
a: int = 2
b: float = 0.1
suAB = a + b
print("Сумма: ", suAB)
razAB = a - b
print("Разность a b: ", razAB)
delAB = a / b
print("Тип при делении : ", type(delAB))

#####
print("\b")
r:float = 5.0
pi:float = math.pi
s = pi * math.pow(r,2)
print(F"Площадь круга до округления: {s}")
sOkr = round(s,2)
print(F"Площадь круга после округления: {sOkr}")

print("\b")
print("---2---")

text: str = "     Hello, Python!   "
print(F"1) text: {text}")
stripText = text.strip()
print(F"2) textStrip: {stripText}")
textWithQ = stripText.replace("!","?")
print(F"3) textWithQ: {textWithQ}")
upTextWithQ = textWithQ.upper()
print(F"4) uppercase: {upTextWithQ}")
lowerText = text.strip().lower()
print(F"5) lowerText: {lowerText}")

print("\b")
print("---3---")

numbers = [7,2,5]
print(F"numbers: {numbers}")
numbers.append(4)
print(F"append: {numbers}")
numbers.insert(1,10)
print(F"insert: {numbers}")
numbers.extend([1,1,1])
print(F"extend: {numbers}")
numbers.remove(7)
print(F"remove: {numbers}")
pop:int = numbers.pop()
print(F"pop: {pop}")
numbers.sort()
print(F"sort: {numbers}")
numbers.reverse()
print(F"reverse: {numbers}")
countTwo = numbers.count(2)
print(F"countTwo: {countTwo}")
print(F"first index 1: {numbers.index(1)} ")
copyNum = numbers.copy()
deepCopyNum = copy.deepcopy(numbers)
print(F"copyNum : {copyNum} ")
print(F"deepCopyNum : {deepCopyNum} ")
numbers.clear()
print(f"clear: {numbers}")

print("\b")
print("---4---")

t1 = (1,2,3)

# если написать t[0] = 23 выпадет ошибка, потому что нельзя изменять кортежи, они считаются инмутабельными
try:
    t1[0] = 23
except:
    print("Нельзя присваивать кортежу новое значение!!!")
t2 = (4,5)
t3 = t1 + t2
print(F"t3: {t3}")
print(f"count 3 in tuple : {t3.count(3)}")
print(f"count index 4: {t3.index(4)}")
print(f"t3: {t3} - такой же как и был")

print("\b")
print("---5---")

values = [3,1,3,2,1,5,2]
unique_values = set(values)

other = set([2,4,5])

print(f"unique_set : {unique_values}")
print(f"кол-во уникальных элементов: {len(unique_values)}")

print(F"A & B : {unique_values & other}")
print(F"A | B : {unique_values | other}")

print(F"A - B : {unique_values - other}")
print(f"B - A : {other - unique_values}")

print("\b")
print("---6---")

scores  = {
    "Alice" : 85,
    "Bob" : 90,
}
print(scores)
scores["Charlie"] = 78
print(scores)
scores["Bob"] = 95
print(scores)
scoreDave = scores.get("Dave")
print(F"scoreDave : {scoreDave}") # None так как нет такого ключа
scoreAlice = scores.get("Alice")
print(F"scoreAlice : {scoreAlice}")
scores.pop("Alice")
print(scores)
print(f"len scores : {len(scores)}")
assert "Alice" not in scores, "нет такого алиса"

print("ключи : ")
for key in scores.keys():
    print(key)
print("\b")
print("значения : ")
for value in scores.values():
    print(value)

print("\b")
print("---7---")
text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
textTwo = text.lower().strip().replace("!",".")
textSplit = textTwo.split(".")
textClear = []
for textSpl in textSplit:
    textClear.append(textSpl.strip())
print(textClear)

print("Для 1го предложения: ")

firstPredlogenie = textClear[0]

print(F"Предложение: {firstPredlogenie}")
splitFirst = firstPredlogenie.split()
print(F"Кол-во питона: {firstPredlogenie.count("python")}")
starts = startswith(firstPredlogenie,"python")
print(F"начинается ли с питона : {starts}")
ends = endswith(firstPredlogenie,"language")
print(F"начинается ли с лангуаге : {starts}")
lenFirst = len(firstPredlogenie)
countA = firstPredlogenie.count("a")
indexData = firstPredlogenie.find("data")
print(F"Кол-во символов: {lenFirst}")
print(f"Кол-во а : {countA}")
print(f"Индекс data : {indexData}")
textWithTire = "-".join(splitFirst)
print(textWithTire)

print("\b")
print("Словарь: ")
dirFirst = {}

for word in splitFirst:
    dirFirst[word] = splitFirst.count(word)
print(dirFirst)

def clean_text(text: str) :
    result = (text.lower().strip()
              .replace(",","").replace(".","")
              .replace("!","").replace("?","")
              )
    return result

print("---проверка функции---")
print(clean_text(text))