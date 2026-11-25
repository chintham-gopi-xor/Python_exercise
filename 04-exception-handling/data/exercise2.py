from pathlib import Path

file_path="C:/Users/Chintham.Gopi/Downloads/Python Training -Interns/Python Training -Interns/04-exception-handling/data/readings.txt"


def parse_readings(file_path):
    bad=[]
    values=[]
    with open(file_path,"r") as f:
        data=f.readlines()
    
    for line_no,line in enumerate(data,start=1):
        text=line.strip()
        try:
            value=float(text)
            values.append(value)

        except ValueError:
            bad.append((line_no,text))
    return values,bad


values,bad=parse_readings(file_path)

print(values)
print(bad)
