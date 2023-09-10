from functools import lru_cache
import time

# lru cache
@lru_cache(maxsize=None)
def funct_cache(x):
    time.sleep(5)
    return x * 10


print(funct_cache(5))
print(funct_cache(4))
print(funct_cache(3))


print(funct_cache(5))
print(funct_cache(3))
