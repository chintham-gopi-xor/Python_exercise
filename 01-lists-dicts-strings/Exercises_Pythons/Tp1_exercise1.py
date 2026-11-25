
import csv
numbers = [14, 3, 9, 27, 8, 21, 5, 18]

def filter_numbers(numbers):
    return {
        "Max": max(numbers),
        "Min": min(numbers),
        "Average": sum(numbers) / len(numbers),
        "descending": sorted(numbers, reverse=True),
        "every_second": numbers[::2],
    }

names = ["  aNNa   maRIA  smith ", "o'brien   john", "MARY-JANE watson", "li   wei"]


def clean_names(names):
    cleaned_names=list(name.strip().title() for name in names )

    result = []

    for name in cleaned_names:
        initials = ".".join(word[0] for word in name.split()) + "."
        result.append(f"'{name}' -> {initials}")

    return result

def mask_number(number):
    return '*'*(len(str(number)) - 4) + str(number)[-4:]

def revers_string(s):
    return s[::-1]

def middle_text(text):
    mid=len(text) // 2
    if len(text) % 2 == 0:
        return text[mid-1:mid+1]
    else:
        return text[mid]



def letter_frequency(text):
    freq={}
    for char in text:
        if char.isalpha():
            char=char.lower()
            freq[char]=freq.get(char,0)+1

    return freq


def top_n_frequent(text,n):
    freq=letter_frequency(text)
    sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
    return sorted_freq[:n]

def summarizer(rows):
    stats={}
    for row in rows:
        dept=row["department"]
        salary=int(row["salary"])
        name=row["name"]
        if dept not in stats:
            stats[dept] = {
                "count": 0,
                "total": 0,
                "max_salary": -1,
                "top": "",
            }

        stats[dept]["count"] += 1
        stats[dept]["total"] += salary

        if salary > stats[dept]["max_salary"]:
            stats[dept]["max_salary"] = salary
            stats[dept]["top"] = name

        results = {}
        for dept, data in stats.items():
            avg_salary = data["total"] / data["count"]
            results[dept] = {
                "count": data["count"],
                "average_salary": avg_salary,
                "top_earner": data["top"],
            }

        return results



with open("C:\\Users\\Chintham.Gopi\\Downloads\\Python Training -Interns\\Python Training -Interns\\01-lists-dicts-strings\\data\\employees.csv",
          mode="r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)
    summary =summarizer(reader)


