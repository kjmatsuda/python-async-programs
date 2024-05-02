# Page 197
import concurrent.futures
import time
import urllib.request


def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')
    return html


with concurrent.futures.ThreadPoolExecutor() as executor:
    t1 = time.perf_counter()
    f1 = executor.submit(download)
    f2 = executor.submit(download)
    t2 = time.perf_counter()
    print((t2-t1)*1000)
    print(f1.result()[:25])
    print(f2.result()[:25])
