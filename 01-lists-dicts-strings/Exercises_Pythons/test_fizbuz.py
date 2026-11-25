from fizzbuzz import fizzbuzz


def test_fizzbuzz_1():
    assert fizzbuzz(1) == ["1"]


def test_fizzbuzz_3():
    assert fizzbuzz(3) == ["1", "2", "Fizz"]


def test_fizzbuzz_5():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fizzbuzz_15():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
def test_fizzbuzz_():
    assert fizzbuzz(-2)==[]

def test_multiple_of_3():
    result = fizzbuzz(9)
    assert result[2] == "Fizz"     # 3
    assert result[5] == "Fizz"     # 6
    assert result[8] == "Fizz"     # 9


def test_multiple_of_5():
    result = fizzbuzz(10)
    assert result[4] == "Buzz"     # 5
    assert result[9] == "Buzz"     # 10


def test_multiple_of_15():
    result = fizzbuzz(15)
    assert result[14] == "FizzBuzz"


def test_return_type():
    assert isinstance(fizzbuzz(10), list)


def test_length():
    assert len(fizzbuzz(20)) == 20


def test_last_element():
    assert fizzbuzz(30)[29] == "FizzBuzz"