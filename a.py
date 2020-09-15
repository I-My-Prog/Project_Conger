from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Entry Test')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

label1 = ttk.Label(frame1, text='Username', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

label2 = ttk.Label(frame1, text='Password', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

# Username Entry
username = StringVar()
username_entry = ttk.Entry(
    frame1,
    textvariable=username,
    width=20)
username_entry.grid(row=0, column=1)

# Password Entry
password = StringVar()
password_entry = ttk.Entry(
    frame1,
    textvariable=password,
    width=20,
    show='*')
password_entry.grid(row=1, column=1)

frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=2, column=1, sticky=W)

button1 = ttk.Button(
    frame2, text='OK',
    command=lambda: print("%s,%s" % (username.get(), password.get())))
button1.pack(side=LEFT)

button2 = ttk.Button(frame2, text='Cancel', command=quit)
button2.pack(side=LEFT)

root.mainloop()