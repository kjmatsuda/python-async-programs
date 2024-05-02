# Page 200
import concurrent.futures
import urllib.request


def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')
    return html


def processDownloadA(f):
    print(f.result()[:25])
    f2 = executor.submit(download)
    f2.add_done_callback(processDownloadB)


def processDownloadB(f):
    print(f.result()[:25])


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(download)
    f1.add_done_callback(processDownloadA)

    print("waiting")
    while True:
        pass
