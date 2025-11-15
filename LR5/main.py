from string import ascii_uppercase
alphf = '0123456789' + ascii_uppercase
#----------------------------------------------------------
def to_base(number,osn):
    if number == 0: return "0"
    result = ""
    while number > 0:
        result = alphf[number%osn] + result
        number //= osn
    return result
#----------------------------------------------------------
def to_pow(number,pow):
    return number**pow
#----------------------------------------------------------
a = [0, 1]
def to_fibonacci(base):
    for i in range(2, base+1):
        a.append(a[i-1] + a[i-2])
    return a[base]
#----------------------------------------------------------
def is_simple_number(number):
    dels = set()
    for num in range(1, int(number**0.5) + 1):
        if number % num == 0:
            dels.add(num)
            dels.add(number // num)
    return True if len(dels) == 2 else False
#----------------------------------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
#----------------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
#----------------------------------------------------------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr