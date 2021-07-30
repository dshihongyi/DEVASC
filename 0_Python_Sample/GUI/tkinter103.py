from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title="Reply", message='Hello %s' % name)

top=Tk()
top.title('Echo')
# top.iconbitmap('google.ico.png')

Label(top, text='Enter your name: ').pack(side=TOP)
ent=Entry(top)
ent.pack(side=TOP)
button=Button(top, text="Submit", command=(lambda: reply(ent.get())))
button.pack(side=LEFT)
top.mainloop()