from collections import deque
import functools
nb_stairs = 4
steps = [1,2]

solutions = []

# def checkReminderAllSolutions(sol):
#     reminder = 0
#     for s in sol:
#         reminder = reminder + s[-1][1]
#     if reminder == 0:
#         return True
#     return False
# #need to store for each path:
# #Actual step
# #Reminder number of steps
# while True:
#     if len(solutions) == 0:
#         reminder = 4
#         for s in steps:
#             solutions.append(deque([(s, reminder - s)]))
#     else:
#         for s in solutions:
#             last_step = s[-1]
#             reminder = last_step[1]
#             for st in steps:
#                 if reminder == 0:
#                     continue
#                 if reminder - st < 0:
#                     continue
#                 s.append([(st, reminder - st)])
#     if checkReminderAllSolutions(solutions):
#         break

# print(solutions)


# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# [1, 2, 3, 4, 5] -> [120, 60, 40, 30, 24]

# [3, 2, 1] -> [2, 3, 6]

# def mitoMultiply(arr):
#     if arr is None or len(arr) == 0:
#         return []
    
#     res = []
#     for i in range(len(arr)):
#         print(arr[i])
#         reminder_arr = arr[:i] + arr[i+1:]
#         res.append(functools.reduce((lambda x, y: x * y), reminder_arr))

#     print(res)
#     return res


# assert mitoMultiply([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
# assert mitoMultiply([3, 2, 1]) == [2, 3, 6]



# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# The following test should pass:




# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
#     def insert(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

# def serialize(tree):
#     tree_str = []

#     if tree:
#         tree_str.append(tree.val)
#         tree_str += serialize(tree.left)
#         tree_str += serialize(tree.right)
#     else:
#         tree_str.append('?')
#     return tree_str
#         #identify data -> . is inddicating tree depth 
#         #val is the actual depth+orientation of the tree
# def serialize2(root):
#     values = []
#     def serializer(node):
#         if not node:
#             values.append('?')
#         else:
#             values.append(str(node.val))
#             serializer(node.left)
#             serializer(node.right)
#     serializer(root)
#     return ','.join(values)


# def deserialize(tree_str):
#     vals = iter(tree_str)
#     def deserializer():
#         val = next(vals)
#         if val == '?':
#             return None
#         node = Node(val)
#         node.left = deserializer()
#         node.right = deserializer()
#         return node
#     return deserializer()


# node = Node('root', Node('left', Node('left.left')), Node('right'))

# print(serialize(node))
# print(serialize2(node))
# node = deserialize(serialize(node))

# assert deserialize(serialize(node)).left.left.val == 'left.left'


# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.





def autoComplete(s, wordList):
    return [word for word in wordList if s == word[:len(s)]]

assert autoComplete('de', ['dog', 'deer', 'deal']) == ['deer', 'deal']

