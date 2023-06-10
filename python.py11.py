from tkinter import *

window=Tk()
canvas = Canvas(window,width=840,height=680)
canvas.grid(row=1,column=1,columnspan=4,sticky=EW)
var = DoubleVar()
scale = Scale(window,from_=1, to=15, variable=var, orient=VERTICAL)
scale.set(5)
scale.grid(row=1,column=7,sticky=NS)
lastx, lasty, mycolor = None,None,"black"

def clear():
    global canvas
    canvas.delete("all")

def reset(event):
    global lastx, lasty
    lastx,lasty=None,None

def paint(event):
    global lastx, lasty, mycolor
    if lastx and lasty:
        canvas.create_oval(lastx, lasty, event.x, event.y, width=var.get(), outline=mycolor)
    lastx=event.x
    lasty=event.y

def red():
    global mycolor
    mycolor="red"

def green():
    global mycolor
    mycolor="green"

def yellow():
    global mycolor
    mycolor="yellow"

def black():
    global mycolor
    mycolor="black"

button = Button(window, text="빨간색", command=red)
button2 = Button(window, text="초록색", comman=green)
button3 = Button(window, text="노랑색", comman=yellow)
button4 = Button(window, text="검은색", comman=black)
button5 = Button(window, text="전체지우기", comman=clear)


button.grid(row=2,column=1,sticky=EW)
button2.grid(row=2,column=2,sticky=EW)
button3.grid(row=2,column=3,sticky=EW)
button4.grid(row=2,column=4,sticky=EW)
button5.grid(row=2,column=5,sticky=EW)

canvas.bind("<B1-Motion>,",paint)
canvas.bind("ButtonRelease-1",reset)

window.mainloop()
