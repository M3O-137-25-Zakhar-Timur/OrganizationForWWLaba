import math
from functools import lru_cache

import numpy

def read_purchases(path):
    file = open(path, "r")
    dict = {}
    result = [st.split(";") for st in file.readlines()]
    valid_result, _, error = validate_table(result)
    for i, st in enumerate(valid_result):
        dict[str(i + 1)] = st

    return dict, error

def validate_table(table):
    errors_count = 0
    validate_table = []
    error_table = []
    for st in table:
        if len(st) < 5:
            errors_count += 1
            error_table.append(st)
            continue
        quantity = float(st[4])
        if not(math.modf(quantity) != 0):
            errors_count += 1
            error_table.append(st)
            continue
        try:
            price = float(st[3])
            quantity = int(st[4])
            if price <= 0 or  quantity < 0:
                errors_count += 1
                error_table.append(st)
                continue
            validate_table.append(st)
        except ValueError:
            errors_count += 1
            error_table.append(st)
            continue

    return validate_table, errors_count, error_table


def count_errors(purchases):
    _, errors_count, _ = validate_table(purchases)
    return errors_count
def total_spent(purchases):
    result = 0
    for st in purchases:
        result += float(purchases[st][3]) * int(purchases[st][4])
    return round(result,2)

def spent_by_category(purchases) :
    category_spending = {}

    for id, item in purchases.items():
        quantity = int(item[4])
        price = float(item[3])
        category = item[1]

        category_spending[category] = round(category_spending.get(category,0) + quantity * price,2)
    return category_spending
def top_n_expensive(purchases, n=3):
    product_spending = {}
    if n > len(purchases):
        return "N больше значений в массиве!"
    for id, item in purchases.items():
        quantity = int(item[4])
        price = float(item[3])
        product = item[2]

        product_spending[product] = round(product_spending.get(product, 0) + quantity * price, 2)
    return sorted(product_spending.items(), key=lambda x: x[1], reverse=True)[0:n]

def write_report(purchases, errors, out_path):
    with open(out_path, "w", encoding='utf-8') as file:
        file.write("")
        report = ["----------ОТЧЕТ ПО ТАБЛИЦЕ---------- \n"
                  f"Валидные строки : {purchases} \n"
                  f"Ошибочные строки : {errors} \n"
                  f"Общая сумма : {total_spent(purchases)} \n"
                  f"Сумма по категориям : {spent_by_category(purchases)} \n"
                  f"Топ-3 покупок : {top_n_expensive(purchases, 3)} \n"]
        file.writelines(report)
    pass
