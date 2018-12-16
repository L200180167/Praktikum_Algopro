from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className='data diri')
L1 = Label(my_app, text="DATA DIRI", font=('Arial', 24))
L1.grid(row=0, column=0)
L2 = Label(my_app, text="Nama Mahasiswa", font=('Arial', 24))
L2.grid(row=1, column=0)
str1 = StringVar()
E2 = Entry (my_app, textvariable=str1)
E2.grid(row=1, column=1)
L3 = Label(my_app, text="NIM", font=('Arial', 24))
L3.grid(row=2, column=0)
str2 = StringVar(value=0)
E3 = Entry (my_app, textvariable=str2)
E3.grid(row=2, column=1)
L4 = Label(my_app, text="Buku Favorit", font=('Arial', 24))
L4.grid(row=3, column=0)
str3 = StringVar()
E4 = Entry (my_app, textvariable=str3)
E4.grid(row=3, column=1)
L5 = Label(my_app, text="Idola", font=('Arial', 24))
L5.grid(row=4, column=0)
str4 = StringVar()
E5 = Entry (my_app, textvariable=str4)
E5.grid(row=4, column=1)
L6 = Label(my_app, text="Motto", font=('Arial', 24))
L6.grid(row=5, column=0)
str5 = StringVar()
E6 = Entry (my_app, textvariable=str5)
E6.grid(row=5, column=1)

def tutup():
    my_app.destroy()

B1 = Button (my_app, text="Tutup", command=tutup)
B1.grid(row=6, column=1)

my_app.mainloop()

