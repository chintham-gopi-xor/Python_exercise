class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def is_balanced(text):

    stack = Stack()

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for ch in text:

        if ch in "([{":
            stack.push(ch)

        elif ch in ")]}":

            if stack.is_empty():
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return stack.is_empty()


# Driver Code

s = Stack()

for n in [10, 20, 30]:
    s.push(n)

print("size:", len(s))
print("peek:", s.peek())
print("pop:", s.pop())
print("size after pop:", len(s))

for text in ["(a + b) * [c]", "{[()]}", "(]", "((x)"]:
    print(f"{text!r} balanced: {is_balanced(text)}")