
#this is my text box
from tkinter import *
master = Tk()

scrollbar = Scrollbar (master)
var = scrollbar.pack

Label(master, text='First Name').pack()
Label(master, text='Last Name').pack()
e1 = Entry(master)
e2 = Entry(master)
e1.pack()
e2.pack()


var1 = IntVar()
Checkbutton(master, text='male', variable=var1).pack()
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).pack()
var3 = IntVar()
Checkbutton(master, text='5', variable=var3).pack()
var4 = IntVar()
Checkbutton(master, text='8e', variable=var4).pack()


frame = Frame(master)
frame.pack()
bottomframe = Frame(master)
bottomframe.pack(side=BOTTOM)
redbutton = Button(frame, text='Red', fg='red')
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text='Brown', fg='brown')
greenbutton.pack(side=LEFT)
bluebutton = Button(frame, text='Blue', fg='blue')
bluebutton.pack(side=LEFT)
blackbutton = Button(bottomframe, text='Black', fg='black')
blackbutton.pack(side=BOTTOM)
frame.pack()



mb = Menubutton(master, text="Button")
mb.pack()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton(label='Contact', variable=cVar)
mb.menu.add_checkbutton(label='About', variable=aVar)
mb.pack()



menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=master.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


w = Label(master, text='GeeksForGeeks.org!')
w = Label(master, text='ComputerScience')
w = Label(master, text='PostOakSchool')
w = Label(master, text='Tkinter')
w.pack()


ourMessage ='This is our Message'
messageVar = Message(master, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack()


v = IntVar()
Radiobutton(master, text='Science', variable=v, value=1).pack(anchor=W)
Radiobutton(master, text='Math', variable=v, value=2).pack(anchor=W)
Radiobutton(master, text='English', variable=v, value=1).pack(anchor=W)
Radiobutton(master, text='History', variable=v, value=2).pack(anchor=W)
Radiobutton(master, text='Art', variable=v, value=1).pack(anchor=W)



w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()

w = Spinbox(master, from_ = 0, to = 10)
w.pack()
mainloop()

