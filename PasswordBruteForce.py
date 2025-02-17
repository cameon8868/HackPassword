import time
from datetime import datetime 
from itertools import *

answer = '001110010011'
s_easy = '01'
s_middle = '1234567890'
s_hard = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
k = 0 
result = ''


start = datetime.now()

while result != answer:
    k += 1
    for i in product(s_middle, repeat=k):
        end_time = time.time()
        a = ''.join(i)
        result = a
        if result == answer:
            print(a, datetime.now() - start)
            break