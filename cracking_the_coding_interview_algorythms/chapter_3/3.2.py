# 3.2 Stack Min: How would you design a stack wh ich, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class Stack():
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, data):
        self.stack.append(data)
        if not self.min:
            self.min.append(data)
        else:
            self.min.append(min(self.min[-1], data))
    
    def pop(self):
        self.min.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min[-1]

s = Stack()
s.push(-2)
s.push(0)
s.push(-6)
print(s.get_min())
print(s.pop())
print(s.get_min())