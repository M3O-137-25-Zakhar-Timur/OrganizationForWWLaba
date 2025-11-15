from main import to_pow, to_base, to_fibonacci, is_simple_number,bubble_sort, selection_sort, insertion_sort

def test_to_pow():
    testNumber = 12
    trueAnswer = 144
    answer = to_pow(testNumber,2)
    assert answer == trueAnswer
def test_to_base():
    testNumber = 120312312351
    trueAnswer = "1C7GEM6G5"
    answer = to_base(120312312351,23)
    assert answer == trueAnswer
def test_to_fibonacci():
    testNumber = 101
    trueAnswer = 573147844013817084101
    answer = to_fibonacci(testNumber)
    assert answer == trueAnswer
def test_is_simple_number():
    testNumber = 463
    trueAnswer = True
    answer = is_simple_number(testNumber)
    assert answer == trueAnswer


testNumber = [45, 12, 78, 3, 91, 34, 67, 23, 89, 56, 1, 77, 42, 19, 84, 29, 61, 5, 96, 38, 72, 15, 50, 8, 99]
trueAnswer = [1, 3, 5, 8, 12, 15, 19, 23, 29, 34, 38, 42, 45, 50, 56, 61, 67, 72, 77, 78, 84, 89, 91, 96, 99]
def test_bubble_sort():
    global testNumber, trueAnswer
    answer = bubble_sort(testNumber)
    assert trueAnswer == answer

def test_selection_sort():
    global testNumber, trueAnswer
    answer = selection_sort(testNumber)
    assert trueAnswer == answer
def test_insertion_sort():
    global testNumber, trueAnswer
    answer = insertion_sort(testNumber)
    assert trueAnswer == answer