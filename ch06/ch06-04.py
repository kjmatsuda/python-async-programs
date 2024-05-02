# Page 111
 
import urllib.request
import threading


def download(html, event):
    with urllib.request.urlopen('http://www.example.com/') as f:
        html.append(f.read().decode('utf-8'))
    event.set()


html1 = []
html2 = []
myEvent = threading.Event()

thread1 = threading.Thread(target=download, args=(html1, myEvent))
thread2 = threading.Thread(target=download, args=(html2, myEvent))


myEvent.clear()
thread1.start()
thread2.start()
myEvent.wait()

if (html1 != []):
    print("thread1")
if (html2 != []):
    print("thread2")
