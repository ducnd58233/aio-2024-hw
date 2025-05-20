class Node:
    def __init__(self, prev=None, next=None, val=None):
        self.prev = prev
        self.next = next
        self.val = val


class Queue:
    def __init__(self, capacity: int):
        self.head_dummy = Node()
        self.tail_dummy = Node(prev=self.head_dummy)
        self.head_dummy.next = self.tail_dummy
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        self.tail_dummy.val = value
        self.tail_dummy.next = Node(prev=self.tail_dummy)
        self.tail_dummy = self.tail_dummy.next
        self.size += 1

    def dequeue(self):
        pop_val = self.head_dummy.next.val
        self.head_dummy = self.head_dummy.next
        self.head_dummy.prev = None
        self.head_dummy.val = None
        self.size -= 1
        return pop_val

    def front(self):
        return self.head_dummy.next.val

    def __str__(self):
        res = []
        ptr = self.head_dummy.next

        while ptr and ptr.next:
            res.append(str(ptr.val))
            ptr = ptr.next
        return "-".join(res)


if __name__ == "__main__":
    q1 = Queue(capacity=5)
    q1.enqueue(1)
    q1.enqueue(2)
    print(q1)

    print(q1.is_full())
    print(q1.front())
    print(q1.dequeue())
    print(q1.front())
    print(q1.dequeue())
    print(q1.is_empty())
