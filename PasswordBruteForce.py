import time
from datetime import datetime 
from itertools import *

n = input()

def BruteForce(n):
    n = str(n)
    k = 0 
    result = ''
    alf = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    end = 0
    start = datetime.now()

    while result != n:
        k += 1
        for i in product(alf, repeat=k):
            a = ''.join(i)
            result = a
            if result == n:
                break
            
    return result, datetime.now() - start

print(BruteForce(n))