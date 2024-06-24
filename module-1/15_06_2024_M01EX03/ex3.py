class Stack:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.data = []

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def is_full(self) -> bool:
        return len(self.data) == self.capacity

    def pop(self):
        return self.data.pop()

    def push(self, value):
        self.data.append(value)

    def top(self):
        return self.data[-1]


if __name__ == '__main__':
    s = Stack(capacity=5)
    s.push(1)
    s.push(2)

    print(s.is_full())
    print(s.top())
    print(s.pop())
    print(s.top())
    print(s.pop())
    print(s.is_empty())
