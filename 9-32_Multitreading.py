import threading
import time


def f1(seconds):
    print(f"SLEEPING FOR {seconds}")
    time.sleep(seconds)


t = time.perf_counter()
print(t)

f1(8)
f1(2)
f1(3)
ta = time.perf_counter()
print("using normal function call : ", ta - t)
# using threads

t1 = threading.Thread(target=f1, args=[8])
t2 = threading.Thread(target=f1, args=[2])
t3 = threading.Thread(target=f1, args=[3])

t1.start()
t2.start()
t3.start()

t1.join()   # stop until t1 in not done
t2.join()
t2.join()

total = time.perf_counter()
print("\nTotal : ", total)

print("using mutithreading :", (total - ta))
