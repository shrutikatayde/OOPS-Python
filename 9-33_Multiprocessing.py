import concurrent
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import requests


def download_the_files_parallely(url, name):
    print(f"process {name} started")
    response = requests.get(url)
    open(f"files/file{name}.jpg", "wb").write(response.content)
    print(f"process {name} finished")


if __name__ == "__main__":
    # url = "https://picsum.photos/200/300"
    # PROCESSES = []
    #
    # for i in range(2):
    #     # download_the_files_parallely(url, i)
    #     d = multiprocessing.Process(target=download_the_files_parallely, args=[url, i])
    #     d.start()
    #     PROCESSES.append(d)
    #
    # for d in PROCESSES:
    #     d.join()

    url = "https://picsum.photos/200/300"

    with concurrent.futures.ProcessPoolExecutor() as executor:
        lst_url = [url for i in range(4)]
        lst_file = [i for i in range(4)]
        res = executor.map(download_the_files_parallely, lst_url, lst_file)
        for i in res:
            print(i)
