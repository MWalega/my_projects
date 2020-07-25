# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).

class SetOfStacks():
    def __init__(self, capacity):
        self.stacks = [[]]
        self.stack_index = 0
        self.capacity = capacity

    def __len__(self):
        return self.stack_index + 1

    def push(self, data):
        if len(self.stacks[self.stack_index]) < self.capacity:
            self.stacks[self.stack_index].append(data)
        else:
            self.stacks.append([])
            self.stack_index += 1
            self.stacks[self.stack_index].append(data)

    def pop(self):
        if len(self.stacks[self.stack_index]) == 0:
            self.stack_index -= 1
        return self.stacks[self.stack_index].pop()

    def pop_at_no_rollovers(self, index):
        return self.stacks[index].pop()

s = SetOfStacks(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.stack_index)
print(s.stacks)
print(s.pop())
print(s.pop())
print(s.stack_index)




        




