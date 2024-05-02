# Page 116
 
import urllib.request
import threading


def download(html, condition):
    with urllib.request.urlopen('http://www.example.com/') as f:
        html.append(f.read().decode('utf-8'))
    with condition:
        condition.notify()


html1 = []
html2 = []

myCondition = threading.Condition()

thread1 = threading.Thread(target=download, args=(html1, myCondition))
thread2 = threading.Thread(target=download, args=(html2, myCondition))

thread1.start()
thread2.start()
with myCondition:
    myCondition.wait()

if (html1 != []):
    print("thread1")
if (html2 != []):
    print("thread2")
