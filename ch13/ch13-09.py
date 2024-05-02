# Page 259
import asyncio
import tkinter
import threading

count = 0
root = None
label1 = None


def stopProg(e):
    global root
    root.quit()


def transfertext(e):
    global label1
    global count
    count = count+1
    label1.configure(text=count)


def setupGUI():
    global root, label1
    root = tkinter.Tk()
    button1 = tkinter.Button(root, text="Exit")
    button1.pack()
    button1.bind('<Button-1>', stopProg)
    button2 = tkinter.Button(root, text="Click Me")
    button2.pack()
    button2.bind('<Button-1>', transfertext)
    label1 = tkinter.Label(root, text="nothing to say")
    label1.pack()


async def tick():
    i = 0
    while True:
        i += 1
        print("TICK", i)
        await asyncio.sleep(0.5)


def runasyncio():
    asyncio.run(main())


async def main():
    T2 = asyncio.create_task(tick())
    await asyncio.wait((T2,))

setupGUI()
t1 = threading.Thread(target=runasyncio, daemon=True)
t1.start()
root.mainloop()
