# Page 256
import tkinter

count = 0
root = None
label1 = None


def stopProg(e):
    global root
    root.destroy()


def transfertext(e):
    global root, label1
    global count
    count = count+1
    label1.configure(text=count)


def runGUI():
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
    root.mainloop()


runGUI()
