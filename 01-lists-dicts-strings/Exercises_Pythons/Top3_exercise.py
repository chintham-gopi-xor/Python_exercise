from pathlib import Path

def file_stats(path):
    lines=0
    words=0
    characters=0
    blank=0
    with open(path,"r") as f:
        for raw_line in f:
            line =raw_line.strip("\r\n")
            lines += 1
            words += len(line.split())
            characters += len(line)
            if not line:
                blank += 1

    return {
        "lines": lines,
        "words": words,
        "characters": characters,
        "blank": blank
    }

file_path = Path("C:\\Users\\Chintham.Gopi\\Downloads\\Python Training -Interns\\Python Training -Interns\\03-file-handling\\data\\notes.txt")

def read_file(file_path):
    with open(file_path,encoding="utf-8") as f:
        for line_no,raw_line in enumerate(f, start=1):
            line = raw_line.strip("\r\n")
            print(f"{line_no}: {line}")

    stats = file_stats(file_path)
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
    print(f"Blank lines: {stats['blank']}")


def write_squares(path,n):
    file_path=Path(path)
    file_path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        for i in range(1,n+1):
            f.write(f"{i} squared is {i**2}\n")

    return n


out_path=Path("output/squares.txt")
def writing_squares(out_path,n):
    count=write_squares(out_path,10)
    print(f"Lines written: {count}")
    print(out_path.read_text(encoding="utf-8"), end="")

def append_squares(path,n):
    file_path=Path(path)
    file_path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,"a",encoding="utf-8") as f:
        for i in range(1,n+1):
            f.write(f"{i} squared is {i**2}\n")

    return n

def count_lines(path):
    file_path=Path(path)
    if not file_path.exists():
        return 0
    with open(file_path,"r",encoding="utf-8") as f:
        return sum(1 for _ in f)

    