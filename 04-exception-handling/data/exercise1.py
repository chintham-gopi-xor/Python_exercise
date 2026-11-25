values=input()
numbers=[]
for value in values.split():
   
    try:
        if value.isdigit():
            num =int(value)
            numbers.append(num)
        else:
            raise ValueError(f"{value} is not a valid integer.")
    except ValueError as e:
        raise ValueError(f"{value} is not a valid integer.")

try:
    if len(numbers)>2:
        raise ValueError("Invalid Input : expected two numbers")
    print(f"{numbers[0]}/{numbers[-1]}  = ",numbers[0]/numbers[-1])

except ZeroDivisionError as e:
    raise ZeroDivisionError("Cannot divide by zero")

        