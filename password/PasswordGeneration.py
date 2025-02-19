from random import *


def Generation():
    res = ''
    for i in range(randrange(5, 17)):
        alf = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        res += alf[randrange(1, len(alf))]
    return res

print(Generation())