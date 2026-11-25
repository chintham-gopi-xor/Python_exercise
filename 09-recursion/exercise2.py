def fib_naive(n, counter=None):
    if counter is not None:
        counter[0] += 1
    if n <= 1:
        return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)


def fib_memo(n, memo=None, counter=None):
    if counter is not None:
        counter[0] += 1
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fib_memo(n - 1, memo, counter) + fib_memo(n - 2, memo, counter)
    memo[n] = result
    return result


def fib_iter(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    print([fib_memo(i) for i in range(10)])
    naive_calls = [0]
    print(fib_naive(20, naive_calls), naive_calls[0])
    memo_calls = [0]
    print(fib_memo(20, counter=memo_calls), memo_calls[0])
    print(fib_memo(90))
    print(fib_memo(90) == fib_iter(90))
