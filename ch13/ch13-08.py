# Page 257
import asyncio
import tkinter

count = 0
root = None
label1 = None
T1 = None


def stopProg(e):
    global T1
    global root
    T1.cancel()
    root.quit()


def transfertext(e):
    global root, label1
    global count
    count = count+1
    label1.configure(text=count)


async def updater(interval):
    global root
    while True:
        root.update()
        await asyncio.sleep(interval)


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


async def main():
    global T1, root
    root.tk.willdispatch()
    T1 = asyncio.create_task(updater(0.01))
    T2 = asyncio.create_task(tick())
    await asyncio.wait((T1,))

setupGUI()
asyncio.run(main())
