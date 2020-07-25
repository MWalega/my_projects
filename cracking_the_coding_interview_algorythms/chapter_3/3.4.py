# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        if len(self.s1) == 0:
            return print('This stack is empty!')

        else:
            return self.s1.pop()

a = Queue()
a.enqueue(1)
a.enqueue(2)
print(a.s1)
a.enqueue(3)
print(a.s1)
a.dequeue()
print(a.s1)