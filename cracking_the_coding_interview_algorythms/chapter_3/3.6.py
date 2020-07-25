# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintai n this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in LinkedList data structure.

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[-1]


class Shelter():
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.count = 0

    def enqueue_shelter(self, name, species):

        if species == "dog":
            self.dogs.enqueue((name, self.count))
            self.count += 1

        elif species == "cat":
            self.cats.enqueue((name, self.count))
            self.count += 1

    def dequeueDog(self):
        self.count -= 1
        return self.dogs.dequeue()

    def dequeueCat(self):
        self.count -= 1
        return self.cats.dequeue()

    def dequeueAny(self):
        
        if self.dogs.items[0][1] < self.cats.items[0][1]:
            self.count -= 1
            return self.dogs.dequeue()

        else:
            self.count -= 1
            return self.cats.dequeue()

s = Shelter()
s.enqueue_shelter('maciek', 'dog')
s.enqueue_shelter('tomek', 'cat')
s.enqueue_shelter('zbyszek', 'cat')
s.enqueue_shelter('zadzior', 'dog')
print(s.dogs.items, s.cats.items, s.count)      
print(s.dequeueAny())
print(s.dequeueCat())
print(s.dogs.items, s.cats.items, s.count)  
    