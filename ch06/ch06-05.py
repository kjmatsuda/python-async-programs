# Page 112
 
import urllib.request
import threading


def download(html, barrier):
    with urllib.request.urlopen('http://www.example.com/') as f:
        html.append(f.read().decode('utf-8'))
    barrier.wait()


html1 = []
html2 = []
myBarrier = threading.Barrier(3)

thread1 = threading.Thread(target=download, args=(html1, myBarrier))
thread2 = threading.Thread(target=download, args=(html2, myBarrier))

thread1.start()
thread2.start()
myBarrier.wait()

if (html1 != []):
    print("thread1")
if (html2 != []):
    print("thread2")
