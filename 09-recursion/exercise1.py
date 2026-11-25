def fact(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n==0:
        return 1
    return n*fact(n-1)


def countdown(n):
    if n <= 0:
        return []
    return [n] + countdown(n - 1)

def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


if __name__ == "__main__":
    print(fact(0), fact(1), fact(5))
    print(fact(20))
    print(countdown(5))
    print(countdown(0))
    print(sum_list([1, 2, 3, 4]))
    print(sum_list([]))
    try:
        fact(-3)
    except ValueError as err:
        print("Error:", err)