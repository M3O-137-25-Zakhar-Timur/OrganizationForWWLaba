import pytest
import os
from purchase_analyzer import *

def test_read_purchases():
    purchases, errors = read_purchases("data/purchases.txt")
    assert isinstance(purchases, dict)
    assert isinstance(errors, list)
    assert purchases is not None
    assert errors is not None

def test_count_errors():
    count = count_errors("data/purchases.txt")
    assert isinstance(count, int)
    assert count >= 0

def test_total_spent():
    purchases, _ = read_purchases("data/purchases.txt")
    total = total_spent(purchases)
    assert isinstance(total, (int, float))
    assert total >= 0

def test_spent_by_category():
    purchases, _ = read_purchases("data/purchases.txt")
    category_spending = spent_by_category(purchases)
    assert isinstance(category_spending, dict)
    for category, amount in category_spending.items():
        assert isinstance(amount, (int, float))

def test_top_n_expensive():
    purchases, _ = read_purchases("data/purchases.txt")
    top_3 = top_n_expensive(purchases, 3)
    assert isinstance(top_3, list)
    assert len(top_3) == 3 or isinstance(top_3, str)

def test_top_n_expensive_with_small_n():
    purchases, _ = read_purchases("data/purchases.txt")
    top_1 = top_n_expensive(purchases, 1)
    assert isinstance(top_1, list)
    if isinstance(top_1, list):
        assert len(top_1) == 1

def test_write_report():
    purchases, errors = read_purchases("data/purchases.txt")
    try:
        write_report(purchases, errors, "test_report.txt")
        file_exists = os.path.exists("test_report.txt")
        assert file_exists == True
        if file_exists:
            os.remove("test_report.txt")
    except Exception as e:
        pytest.fail(f"write_report failed with error: {e}")