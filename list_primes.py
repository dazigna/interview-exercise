import math
class PrimeGenerator(object):

    def generate_primes(self, max_num):
        if not isinstance(max_num, int):
            raise TypeError("invalid number")
        premier = []
        
        
        for i in range(max_num):
            is_premier = True
            if i <2: # 0 & 1 are no premier
                premier.append(False)
                continue
            
            for j in range(2, int(math.sqrt(i)) + 1):
                if i%j == 0:
                    is_premier = False

            premier.append(is_premier)
        return premier


res = [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
print(res)
print(PrimeGenerator().generate_primes(20))

assert PrimeGenerator().generate_primes(20) == res