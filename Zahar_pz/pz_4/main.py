import time
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


def fib_iter(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_rec(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def sum_nested(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total


n = 50

start = time.time()
res_iter = fib_iter(n)
time_iter = time.time() - start
logger.info(f"Итеративная F({n}) = {res_iter}, время: {time_iter:.6f} сек")


lst = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]
start = time.time()
total = sum_nested(lst)
time_sum = time.time() - start
logger.info(f"Сумма списка {lst} = {total}, время: {time_sum:.6f} сек")

start = time.time()
res_rec = fib_rec(n)
time_rec = time.time() - start
logger.info(f"Рекурсивная F({n}) = {res_rec}, время: {time_rec:.6f} сек")
