def my_generator():
    strr = "apple"
    for i in range(len(strr)):
        yield strr[i]


g = my_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
