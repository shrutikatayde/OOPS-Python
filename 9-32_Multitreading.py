import threading
import time
from concurrent.futures import ThreadPoolExecutor


def f1(seconds):
    print(f"SLEEPING FOR {seconds}")
    time.sleep(seconds)
    return seconds


def main():
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

    t1.join()  # stop until t1 in not done
    t2.join()
    t2.join()

    total = time.perf_counter()
    print("\nTotal : ", total)

    print("using mutithreading :", (total - ta))


# for parallel execution


def concurrent_future():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(f1, 8)
        # future2 = executor.submit(f1, 2)
        # future3 = executor.submit(f1, 3)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        list1 = [8, 9, 6, 2]
        lst = executor.map(f1, list1)
        for i in lst:
            print(i)


concurrent_future()
