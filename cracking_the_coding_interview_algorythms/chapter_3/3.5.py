# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array) . The stack supports the following operations: push, pop, peek, and isEmpty.

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

def Sort_Stack(s1):
    temp_stack = Stack()
    while s1.is_empty() == False:
        temp = s1.peek()
        s1.pop()
        while temp_stack.is_empty() == False and temp_stack.peek() > temp:
            s1.push(temp_stack.pop())
        temp_stack.push(temp)
    return temp_stack.stack

s = Stack()
s.push(34)
s.push(3)
s.push(31)
s.push(98)
s.push(92)
s.push(23)
print(s.stack)
print(Sort_Stack(s))
        




    