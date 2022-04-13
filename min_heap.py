

class MinHeap:
    def __init__(self):
        self.heap = []

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop(0)
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self.bubbleDown(0)
        return min_val

    def insert(self, key):
        self.heap.append(key)
        self.bubbleUp(len(self.heap)-1)
    
    def bubbleUp(self, index):
        if index == 0:
            return
        
        index_parent = (index - 1) //2
        if self.heap[index] < self.heap[index_parent]:
            #Swap values
            self.heap[index], self.heap[index_parent] = self.heap[index_parent], self.heap[index]
            self.bubbleUp(index_parent)


    def min_child_index(self, index):
        left_child_index = index*2 + 1
        right_child_index = index*2 + 2

        #check border conditions
        if right_child_index >= len(self.heap):
            if left_child_index >= len(self.heap):
                return -1
            return left_child_index
        else:
            if self.heap[left_child_index] > self.heap[right_child_index]:
                return right_child_index
            else:
                return left_child_index

    def bubbleDown(self, index):
        min_index_child = self.min_child_index(index)
        if min_index_child == -1:
            return
        
        if self.heap[index] > self.heap[min_index_child]:
            self.heap[index], self.heap[min_index_child] = self.heap[min_index_child], self.heap[index]
            self.bubbleDown(min_index_child)

minHeap = MinHeap()

minHeap.insert(20)
minHeap.insert(5)
assert minHeap.heap[0] == 5
