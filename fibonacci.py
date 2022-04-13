class Math(object):
    # F(0) = 0
    # F(1) = 1
    # F(i) = F(i-1)+ F(i-2)
    def fib_iterative(self, n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a+b
        return a

    def fib_recursive(self, n):
        if n == 0  or n == 1:
            return n
        else:
            return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_dynamic(self, n):
        cache = {}
        return self._fib(n, cache)

    def _fib(self, n, cache):
        if n == 0  or n ==1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self._fib(n-1, cache) + self._fib(n-2, cache)
        return cache[n]

    def fib_me(self, n):
        fib_list = [0,1]
        
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])

        return fib_list[n]
    
    def fib_custom_start(self, n, start, start1) :
        fib_list = [start,start1]
        
        for i in range(2, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2])

        return fib_list[n]
    def staircase(self, n):
        if n <= 1:
            return 1
        return self.staircase(n - 1) + self.staircase(n - 2)
def test_fib(func):
    result = []
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(len(expected)):
        result.append(func(i))
    assert result == expected
    print('Success: test_fib')

m = Math()
# test_fib(m.fib_iterative)
# test_fib(m.fib_recursive)
# test_fib(m.fib_me)
test_fib(m.fib_dynamic)


    