# Page 118
 
import urllib.request
import threading


def download(html, condition):
    with urllib.request.urlopen('http://www.example.com/') as f:
        html.append(f.read().decode('utf-8'))
    global myCount
    with condition:
        myCount += 1
        condition.notify()


myCount = 0

html1 = []
html2 = []
html3 = []

myCondition = threading.Condition(threading.Lock())

thread1 = threading.Thread(target=download, args=(html1, myCondition))
thread2 = threading.Thread(target=download, args=(html2, myCondition))
thread3 = threading.Thread(target=download, args=(html3, myCondition))
thread1.start()
thread2.start()
thread3.start()
with myCondition:
    myCondition.wait_for(lambda: myCount >= 2)

if (html1 != []):
    print("thread1")
if (html2 != []):
    print("thread2")
if (html3 != []):
    print("thread3")
