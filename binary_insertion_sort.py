

class BinarySort:
    def __init__(self):
        pass

    def binarySearch(self, arr, val, start, end):
        if start == end:
            if arr[start] > val:
                return start
            else: 
                return start+1

        if start>end:
            return start
        
        mid = (start + end) // 2

        if arr[mid] > val:
            return self.binarySearch(arr, val, start, mid-1)
        elif arr[mid] < val:
            return self.binarySearch(arr, val, mid + 1, end)
        else: 
            return mid

    def binarySort(self, arr):
        for i in range(1, len(arr)):
            val = arr[i]
            j = self.binarySearch(arr, val, 0, i-1)
            arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        return arr