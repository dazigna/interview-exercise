
from binary_insertion_sort import BinarySort


class TestBinarySort:

    def testSort(self):
        arr = [8,6,1,5,3]
        sortingClient = BinarySort()
        res = sortingClient.binarySort(arr)
        assert sorted(arr) == res
    
    def testSearch(self):
        arr = [1,4,5,7,9]
        sortingClient = BinarySort()
        index = sortingClient.binarySearch(arr, 5, 0, len(arr))
        assert index == 2