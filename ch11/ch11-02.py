# Page 198 modified by top
import concurrent.futures
import time
import urllib.request


def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')
    return html


t1 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(download)
    f2 = executor.submit(download)

    t2 = time.perf_counter()
    print((t2-t1)*1000)

    res = concurrent.futures.wait([f1, f2],
                                  return_when=concurrent.futures.FIRST_COMPLETED)
    for f in res.done:
        print(f.result()[:25])
