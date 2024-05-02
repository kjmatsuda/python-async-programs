# Page 72
import threading


def myThread():
    while True:
        pass


t0 = threading.main_thread()
t1 = threading.Thread(target=myThread, daemon=True)
t2 = threading.Thread(target=myThread, daemon=False)
t1.start()
t2.start()
print(t0.native_id)
print(t1.native_id)
print(t2.native_id)
print("ending")
