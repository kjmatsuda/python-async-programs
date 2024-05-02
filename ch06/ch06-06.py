# Page 113
 
import urllib.request
import threading


def download(html, barrier):
    with urllib.request.urlopen('http://www.example.com/') as f:
        html.append(f.read().decode('utf-8'))
    try:
        barrier.wait()
    except:
        pass


html1 = []
html2 = []
myBarrier = threading.Barrier(2)

thread1 = threading.Thread(target=download, args=(html1, myBarrier))
thread2 = threading.Thread(target=download, args=(html2, myBarrier))

thread1.start()
thread2.start()
myBarrier.wait()
myBarrier.abort()

if (html1 != []):
    print("thread1")
if (html2 != []):
    print("thread2")
