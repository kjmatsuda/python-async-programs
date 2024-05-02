# Page 80
import urllib.request
import threading
import time


def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')


thread1 = threading.Thread(target=download)
t1 = time.perf_counter()
thread1.start()
download()
thread1.join()
t2 = time.perf_counter()
print((t2-t1)*1000)
