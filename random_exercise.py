# Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.
# lettersum("") => 0
# lettersum("a") => 1
# lettersum("z") => 26
# lettersum("cab") => 6
# lettersum("excellent") => 100
# lettersum("microspectrophotometries") => 317


# def lettersum(str):
#     if str == '' or not str:
#         return 0

#     sum_ord = 0
#     for c in str:
#         sum_ord += ord(c) - ord('a') + 1
#     print(sum_ord)
#     return sum_ord

# assert lettersum('') == 0
# assert lettersum('a') == 1
# assert lettersum('z') == 26
# assert lettersum('cab') == 6
# assert lettersum('excellent') == 100
# assert lettersum('microspectrophotometries') == 317


# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

# def addUpToNumber(list, num):
#     for i in range(len(list)):
#         reminder_list = list[i:]
#         print(reminder_list)
#         for val in reminder_list:
#             if val + list[i] == num:
#                 return True

#     return False

# def addUpToNumberFast(list, num):
#     return any(num - i in list for i in list)

# assert addUpToNumber([3, 15, 3, 7, 10], 17) == True
# assert addUpToNumberFast([3, 15, 3, 7, 10], 17) == True

import functools

@functools.lru_cache(maxsize=None)
def phonedrop(n, k):
    if n == 1 or k == 1 or k == 0:
        return k
    
    num_tries = 0
    for i in range(1, k):
        x = phonedrop(n-1, i)
        print(f'x: {x}')
        y = phonedrop(n, k - i)
        print(f'y: {y}')
        num_tries = max(num_tries, min(x,y) + 1)

    return num_tries

# assert phonedrop(1, 100) == 100
# assert phonedrop(2, 100) == 14
# assert phonedrop(3, 100) == 9
# assert phonedrop(1, 1) == 1
# assert phonedrop(2, 456) == 30
# assert phonedrop(3, 456) == 14
# assert phonedrop(4, 456) == 11
# assert phonedrop(2, 789) == 40
# assert phonedrop(3, 789) == 17
# assert phonedrop(4, 789) == 12


# def nonogramrow(arr):
#     res = []
    
#     #Scan array -> increment counter -> if 0 push back to res then reset counter
#     counter = 0
#     for v in arr:
#         if v == 1:
#             counter += 1
#             continue
#         if counter != 0:
#             res.append(counter)
#         counter = 0
#     if counter != 0:
#         res.append(counter)
#     print(res)
#     return res
    

# assert nonogramrow([]) == []
# assert nonogramrow([0,0,0,0,0]) == []
# assert nonogramrow([1,1,1,1,1]) == [5]
# assert nonogramrow([0,1,1,1,1,1,0,1,1,1,1]) == [5,4]
# assert nonogramrow([1,1,0,1,0,0,1,1,1,0,0]) == [2,1,3]
# assert nonogramrow([0,0,0,0,1,1,0,0,1,0,1,1,1]) == [2,1,3]
# assert nonogramrow([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]) == [1,1,1,1,1,1,1,1]


# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# Implement car and cdr.
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair

# print(cons(3,4))

# def car(cons):
#     def return_first(a,b):
#         return a
#     return cons(return_first)

# print(car(cons(3,4)))

# def cdr(cons):
#     def return_last(a,b):
#         return b
#     return cons(return_last)

# assert car(cons(3,4)) == 3
# assert cdr(cons(3,4)) == 4


# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.



# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

import ctypes
class XORNode():
    def __init__(self, data, both = 0) -> None:
        self.data = data
        self.both = both
    
class XorLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.__nodes = []

    def _xor(self, node_prev, node_next):
        return (node_prev and not node_next) or (not node_prev and node_next)

    #Adds element to the end
    def add(self, element):
        if not element:
            raise Exception('invalid element')
        
        node = XORNode(element)
        
        if not self.head:
            self.head = node
            self.tail = node        
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node
        
        self.__nodes.append(node)

    #return node at Index
    def get(self, index):
        prev_id = 0
        next_id = 1
        node = self.head
        counter = 0
        while counter != index:
            next_id = prev_id ^ node.both
            if next_id:
                node = self.__type_cast(next_id)
                counter += 1       


