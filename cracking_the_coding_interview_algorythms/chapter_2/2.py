class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def push(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        new_node.next = cur_node
        self.head = new_node

    def reverse(self):
        prev_node = None
        cur_node = self.head

        while cur_node:
            nxt = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = nxt
        
        self.head = prev_node

    def append_Node(self, Node):
        prev = None
        cur = self.head
        
        while cur:
            prev = cur
            cur = cur.next

        prev.next = Node
        prev.next.next = None

    # 2.1 Remove Dups: Write code to remove duplicates from an unsorted li nked list.
    
    def RemoveDups(self):
        cur_node = self.head

        if cur_node is None:
            return ('List is empty')

        prev_node = None
        data_lst = []
        while cur_node:
            if cur_node.data not in data_lst:
                data_lst.append(cur_node.data)
                prev_node = cur_node
                cur_node = cur_node.next
            else:
                prev_node.next = cur_node.next
                cur_node.next = None
                cur_node = None
                cur_node = prev_node.next

    # 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
    
    def kth_to_last(self, k):
        cur_node = self.head

        length = 0
        while cur_node:
            cur_node = cur_node.next
            length += 1

        if length < k:
            print('List is shorter than ' + str(k))
            return

        cur_node = self.head
        for i in range(0, length - k):
            cur_node = cur_node.next
        print(cur_node.data)

    # 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
    # the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    # that node.
    # EXAMPLE
    # Input: the node c from the linked list a - >b- >c - >d - >e- >f
    # Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
    
    def delete_middle(self):
        cur_node = self.head

        length = 0
        while cur_node:
            cur_node = cur_node.next
            length += 1
        
        if length < 3:
            print('List has no middle elements')
            return
        
        cur_node = self.head
        prev_node = None
        for i in range(length//2):
            prev_node = cur_node
            cur_node = cur_node.next

        prev_node.next = cur_node.next
        cur_node.next = None
        cur_node = None
        
    # 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
    # before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
    # to be after the elements less than x (see below) . The partition element x can appear anywhere in the
    # "right partition"; it does not need to appear between the left and right partitions.
    # EXAMPLE
    # Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
    # Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    
    def partition(self, par):
        before = before_head = Node(0)
        after = after_head = Node(0)

        cur_node = self.head
        while cur_node:
            if cur_node.data < par:
                before.next = cur_node
                before = before.next
            else:
                after.next = cur_node
                after = after.next
            cur_node = cur_node.next

        after.next = None
        before.next = after_head.next
        self.head = before_head.next
        before_head = None
        after_head = None

# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-) 1 -) 6) + (5 -) 9 -) 2) .Thatis,617 + 295.
# Output: 2 -) 1 -) 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -) 1 -) 7) + (2 -) 9 -) 5) . Thatis,617 + 295 .
# Output: 9 -) 1 -) 2. That is, 912.
        
num_1 = LinkedList()
num_1.append(7)
num_1.append(1)
num_1.append(6)
num_2 = LinkedList()
num_2.append(5)
num_2.append(9)
num_2.append(2)
    
def sum_lists(num_1, num_2):
    num_1_lst = []
    cur_num_1 = num_1.head
    while cur_num_1:
        num_1_lst.append(str(cur_num_1.data))
        cur_num_1 = cur_num_1.next

    num_1_lst = num_1_lst[::-1]

    num_2_lst = []
    cur_num_2 = num_2.head
    while cur_num_2:
        num_2_lst.append(str(cur_num_2.data))
        cur_num_2 = cur_num_2.next

    num_2_lst = num_2_lst[::-1]

    integer_1 = int(''.join(num_1_lst))
    integer_2 = int(''.join(num_2_lst))

    integer_sum = integer_1 + integer_2
    sum_str = str(integer_sum)

    new_ll = LinkedList()
    for num in sum_str:
        new_ll.push(int(num))

    return new_ll.print_list()

# Przy drugim zalozeniu zamienic push na append

# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

def reversing(llist):
    new_ll = LinkedList()

    old_cur = llist.head
    while old_cur:
        new_ll.push(old_cur.data)
        old_cur = old_cur.next
    
    return new_ll


def check_if_palindrome(llist):
    norm_list = llist
    rev_list = reversing(norm_list)
    
    cur_ll_norm = norm_list.head
    cur_ll_rev = rev_list.head

    while cur_ll_norm:
        if cur_ll_norm.data != cur_ll_rev.data:
            return False
        cur_ll_norm = cur_ll_norm.next
        cur_ll_rev = cur_ll_rev.next
    return True

# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
# kth node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

def len_and_tail(llist):
    prev = None
    cur_node = llist.head
    counter = 0

    while cur_node:
        counter += 1
        prev = cur_node
        cur_node = cur_node.next
    tail = prev

    return tail, counter

def move_pointer(ll , num_steps):
    cur = ll.head
    for i in range(num_steps):
        cur = cur.next
    return cur

def intersection_check(ll_1, ll_2):
    tail_1, counter_1 = len_and_tail(ll_1)
    tail_2, counter_2 = len_and_tail(ll_2)

    if tail_1 != tail_2:
        return False
    
    cur_1 = ll_1.head
    cur_2 = ll_2.head
    
    if counter_1 > counter_2:
        len_diff = counter_1 - counter_2
        cur_1 = move_pointer(ll_1, len_diff)

    else:
        len_diff = counter_2 - counter_1
        cur_2 = move_pointer(ll_2, len_diff)

    while cur_1 and cur_2:
        if cur_1 == cur_2:
            return cur_1.data
        cur_1 = cur_1.next
        cur_2 = cur_2.next

    return False

    
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(3)
llist.append(2)
llist.append(1)
# llist.RemoveDups()
# llist.kth_to_last(2)
# llist.kth_to_last(9)
# llist.delete_middle()
# llist.partition(3)
# llist.partition(1)
# llist.partition(6)
# llist.partition(9)
# llist.print_list()
# num_1.print_list()
# num_2.print_list()
# print(sum_lists(num_1, num_2))
# print(check_if_palindrome(llist))
# print(intersection_check(num_1, num_2))
l1 = LinkedList()
l2 = LinkedList()
a = Node('a')
b = Node('b')
c = Node('c')
l1.append(1)
l1.append(2)
l1.append(3)
l1.append_Node(a)
l1.append_Node(b)
l1.append_Node(c)
l2.append(1)
l2.append_Node(a)
l2.append_Node(b)
l2.append_Node(c)
print(intersection_check(l1, l2))
# print(l1.print_list())
# print(l2.print_list())


