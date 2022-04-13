class SelectionSort(object):
    def sort(self, data):
        if data is None:
            raise Exception("invalid array")
        if len(data) < 2:
            return data
        
        list_sorted = data.copy()
        pointer = 0 
        while pointer < len(data):
            min_value = min(list_sorted[pointer:])
            #Find all mins and index
            list_mins = [(j, i) for i, j in enumerate(list_sorted) if j == min_value]
            mins = [ t[0] for t in list_mins ]
            index = [ t[1] for t in list_mins ]
            
            for i in sorted(index, reverse = True):
                del list_sorted[i]
            
            #pop and replace
            list_sorted = list_sorted[0:pointer] + mins + list_sorted[pointer:]
            pointer += len(mins)
        
        return list_sorted

    def sort_alt(self, data):
        if data is None:
            raise Exception("invalid array")
        if len(data) < 2:
            return data

        for i in range(len(data) -1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
                if data[min_index]<data[i]:
                    data[min_index], data[i] = data[i], data[min_index]
        return data


t = SelectionSort()
assert t.sort([43,2,2,1]) == sorted([43,2,2,1])

assert t.sort_alt([5, 1, 7, 2, 6, -3, 5, 7, -10]) == sorted([5, 1, 7, 2, 6, -3, 5, 7, -10])