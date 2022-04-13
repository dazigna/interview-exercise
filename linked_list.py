from dataclasses import dataclass
from mimetypes import init



class Node:
    def __init__(self,data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, head = None) -> None:
        self.head = head

    def insert_to_front(self, data):
        if not data:
            raise Exception("not valid")
        node = Node(data, self.head)
        self.head = node
        return node
        
    def append(self, data):
        if not data:
            raise Exception("not valid")
        
        node = Node(data)
        
        if not self.head:
            self.head = node
        else:
            #find last node 
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = node
        
        return node

    def find(self, data):
        if not data or not self.head:
            raise Exception("not valid")
        
        res = []
        cur_node = self.head
        while cur_node.next is not None:
            if cur_node.data == data:
                return cur_node
            cur_node = cur_node.next
        return None

    def delete(self, data):
        if not data or not self.head:
            raise Exception("not valid")  
        
        if self.head.data == data:
            self.head.next = self.head.next
            return
        
        cur_node = self.head.next
        prev_node = self.head
        while cur_node.next is not None:
            if cur_node.data == data:
                prev_node.next = cur_node.next
                return
            prev_node = cur_node
            cur_node = cur_node.next

    def lenght(self):
        counter = 0
        cur_node = self.head
        while cur_node.next is not None:
            counter += 1
            cur_node = cur_node.next
        return counter
    def find_kth_element(self, k):
        slow_pointer = self.head
        fast_pointer = self.head.next
        
        for _ in range(k):
            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return None

        while fast_pointer.next is not None:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

        return slow_pointer.data

    def print(self):
        cur_node = self.head
        while cur_node.next is not None:
            print(cur_node)
            cur_node = cur_node.next
    
    def get_all_data(self):
        data = []
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data

    def nodePartition(self, k):
        if self.head.data == k:
            return self.head
        left =  LinkedList(None)
        right = LinkedList(None)


        cur_node = self.head
        while cur_node.next is not None:
            if cur_node.data > k:
                right.append(cur_node.data)    
            elif cur_node.data == k:
                right.insert_to_front(cur_node.data)    
            else:
                left.append(cur_node.data)

            cur_node = cur_node.next
        #Merge list
        cur_left = left.head
        if cur_left is None:
            return right
        else:
            while cur_left.next is not None:
                cur_left = cur_left.next
            cur_left.next = right.head
            return left

linked_list = LinkedList(Node(12))
linked_list.insert_to_front(10)
linked_list.insert_to_front(14)
linked_list.insert_to_front(1)
linked_list.insert_to_front(10)
linked_list.insert_to_front(8)
linked_list.insert_to_front(13)
linked_list.insert_to_front(3)
linked_list.insert_to_front(4)

print(linked_list.get_all_data())
partion = linked_list.nodePartition(10)
print(partion.get_all_data())
