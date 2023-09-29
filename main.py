
#this is my text box
from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=5, column=2)
Label(master, text='Last Name').grid(row=6, column=2)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=5, column=0)
e2.grid(row=6, column=0)
from tkinter import *

var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(master, text='5', variable=var3).grid(row=2, sticky=W)
var4 = IntVar()
Checkbutton(master, text='8e', variable=var4).grid(row=3, sticky=W)

from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text='Brown', fg='brown')
greenbutton.pack(side=LEFT)
bluebutton = Button(frame, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)
blackbutton = Button(bottomframe, text='Black', fg='black')
blackbutton.pack(side=BOTTOM)

from tkinter import *

top = Tk()
mb = Menubutton(top, text="GfG")
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton(label='Contact', variable=cVar)
mb.menu.add_checkbutton(label='About', variable=aVar)
mb.pack()

from tkinter import *

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

from tkinter import *
master = Tk()
w = Label(master, text='GeeksForGeeks.org!')
w = Label(master, text='ComputerScience')
w = Label(master, text='PostOakSchool')
w = Label(master, text='Tkinter')
w.pack()

from tkinter import *
main = Tk()
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )

from tkinter import *
master = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)

from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()

from tkinter import *
master = Tk()
w = Spinbox(master, from_ = 0, to = 10)
w.pack()
mainloop()

