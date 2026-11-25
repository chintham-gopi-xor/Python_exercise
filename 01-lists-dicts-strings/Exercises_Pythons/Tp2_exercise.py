import sys

def enter_input():
    a=input("Enter text : ")
    return a


def grades(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def validation():
    line=input()
    valid_scores=[]
    for score in line.split():
        if score.isdigit() and 0 <= int(score) <= 100:
            scores=int(score)
            valid_scores.append(scores)
            print(f"{scores}: {grades(scores)}")

        else:
            print(f"{scores}: {"Invalid"}")

    if valid_scores:
        average=calculate_average(valid_scores)
        print(f"Average score: {average:.2f}")
    else:
        print("No valid scores entered.")



def _temprature():

    print("C    F    K")
    for i in range(-20,41,10):
        cel=i
        far=(cel*9/5)+32
        kel=cel+273.15
        print(f"{cel:<5}{far:<5}{kel:<5}")

        
            




def is_prime(num):
    if num <= 1:
        return False
    indi=num**0.5+1
    i=2
    while indi> i:
        if num % i == 0:
            return False
        i += 1
    return True

def prime_numbers():
    input_num = (input())

    for i in input_num.split():
        
        if i.isdigit():
            num = int(i)
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        else:
            print(f"{i} is not a valid integer.")





def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def std_input_palin_call():
    for line in sys.stdin:
        text=line.strip()
        if text:
            if is_palindrome(text):
                print(f"{text} is a palindrome.")
            else:
                print(f"{text} is not a palindrome.")



def word_line_count():
    for line in sys.stdin.read():
        lines=line.strip().splitlines()
        for line in lines:
            words=line.split()
            word_count=len(words)
            print(f"Line: {line}")
            print(f"Word count: {word_count}")
