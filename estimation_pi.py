#Simulate random points within a square of side 1 unit.

'''Estimate pi with 3 digits using monte carlo methods'''
import random
import math
class PiEstimator():
    def __init__(self) -> None:
        pass

    def compute(self):
        pointsTotal = 0
        pointsinCircle = 0
        pi = 0
        n = 1000
        for i in range(n**2):
            x = random.uniform(0,1)
            y = random.uniform(0,1)

            if (x**2 + y**2) <= 1:
                pointsinCircle += 1

            pointsTotal += 1
            pi = 4 * pointsinCircle/pointsTotal
            
            if math.trunc(pi * 1000)/1000 == 3.141:
                print(f'iterations {i}')
                print(f'pi: {pi}')
                break
        return pi
assert math.trunc(PiEstimator().compute() * 1000)/1000 == 3.141
