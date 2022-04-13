from min_heap import MinHeap
import unittest

class TestMinHeap(unittest.TestCase):

    def test_min_heap(self):
        minheap = MinHeap()
        minheap.insert(20)
        self.assertEqual(minheap.heap[0], 20)
        minheap.insert(5)
        self.assertEqual(minheap.heap[0], 5)
        self.assertEqual(minheap.heap[1], 20)
        minheap.insert(15)
        self.assertEqual(minheap.heap[0], 5)
        self.assertEqual(minheap.heap[1], 20)
        self.assertEqual(minheap.heap[2], 15)
        minheap.insert(22)
        self.assertEqual(minheap.heap[0], 5)
        self.assertEqual(minheap.heap[1], 20)
        self.assertEqual(minheap.heap[2], 15)
        self.assertEqual(minheap.heap[3], 22)
        minheap.insert(40)
        self.assertEqual(minheap.heap[0], 5)
        self.assertEqual(minheap.heap[1], 20)
        self.assertEqual(minheap.heap[2], 15)
        self.assertEqual(minheap.heap[3], 22)
        self.assertEqual(minheap.heap[4], 40)
        minheap.insert(3)
        self.assertEqual(minheap.heap[0], 3)
        self.assertEqual(minheap.heap[1], 20)
        self.assertEqual(minheap.heap[2], 5)
        self.assertEqual(minheap.heap[3], 22)
        self.assertEqual(minheap.heap[4], 40)
        self.assertEqual(minheap.heap[5], 15)
        mins = []
        while minheap.heap:
            print(mins)
            mins.append(minheap.extract_min())
        self.assertEqual(mins, [3, 5, 15, 20, 22, 40])
        print('Success: test_min_heap')
