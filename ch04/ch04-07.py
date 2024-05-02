# Page 79
import urllib.request
import time


def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')


t1 = time.perf_counter()
download()
download()
t2 = time.perf_counter()
print((t2-t1)*1000)
