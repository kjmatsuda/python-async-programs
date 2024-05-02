# Page 109
 
import urllib.request
import threading


def download(html, lock):
    with urllib.request.urlopen('http://www.example.com/') as f:
        html.append(f.read().decode('utf-8'))
    lock.release()


html1 = []
html2 = []
mySem = threading.Semaphore()

thread1 = threading.Thread(target=download, args=(html1, mySem))
thread2 = threading.Thread(target=download, args=(html2, mySem))


mySem.acquire()
thread1.start()
thread2.start()
mySem.acquire()

if (html1 != []):
    print("thread1")
if (html2 != []):
    print("thread2")
