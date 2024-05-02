# Page 199
import concurrent.futures
import urllib.request


def download():
    with urllib.request.urlopen('http://www.example.com/') as f:
        html = f.read().decode('utf-8')
    return html


def processDownload(f):
    print(f.result()[:25])


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(download)
    f2 = executor.submit(download)
    f1.add_done_callback(processDownload)
    f2.add_done_callback(processDownload)
    print("waiting")
