# Page 198 modified by bottom
import concurrent.futures
import time
import urllib.request


def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')
    return html


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(download)
    f2 = executor.submit(download)
    for f in concurrent.futures.as_completed([f1, f2]):
        print(f.result()[:25])
