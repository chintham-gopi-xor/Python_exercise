class Queue:

    def __init__(self):
        self.inbox = []
        self.outbox = []

    def _transfer(self):
        while self.inbox:
            self.outbox.append(self.inbox.pop())

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):

        if not self.outbox:
            self._transfer()

        if not self.outbox:
            raise IndexError("dequeue from empty queue")

        return self.outbox.pop()

    def front(self):

        if not self.outbox:
            self._transfer()

        if not self.outbox:
            raise IndexError("front from empty queue")

        return self.outbox[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.inbox) + len(self.outbox)


def process_jobs(jobs):

    q = Queue()

    for job in jobs:
        q.enqueue(job)

    result = []

    while not q.is_empty():
        result.append(q.dequeue())

    return result


# Driver Code

q = Queue()

q.enqueue("a")
q.enqueue("b")
q.enqueue("c")

print("front:", q.front())
print("dequeue:", q.dequeue())

q.enqueue("d")

print("size:", len(q))
print("remaining:", [q.dequeue() for _ in range(len(q))])

print("jobs:", process_jobs(
    ["report.pdf", "photo.png", "notes.txt"]
))