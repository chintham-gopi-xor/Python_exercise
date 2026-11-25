def fizzbuzz(n):
    result = []
    for num in range(1, n + 1):
        if num % 15 == 0:
            result.append("FizzBuzz")
            continue
        if num % 3 == 0:
            result.append("Fizz")
            continue
        if num % 5 == 0:
            result.append("Buzz")
            continue
        
        result.append(str(num))
    return result
 
 
n = int(input("Enter the Number"))
print(*fizzbuzz(n),sep="\n")