# def main():
import tkinter as tk

window = tk.Tk()
window.title("5/12 - 1")
# name label
tk.Label(window,
         text="Name :", ).grid(row=0)
name1 = tk.Entry(window)
name1.grid(row=0, column=10)
name = name1.get()

# Mobile no lable
tk.Label(window,
         text="Mobile No :", ).grid(row=2)
Mobile_no1 = tk.Entry(window)
Mobile_no1.grid(row=2, column=10)

# Address lable
tk.Label(window,
         text="Address :", ).grid(row=4)
address1 = tk.Entry(window)
address1.grid(row=4, column=10)
address = address1.get()

# email lable
tk.Label(window,
         text="Email :", ).grid(row=6)
email1 = tk.Entry(window)
email1.grid(row=6, column=10)


def check_mobile():
    temp = Mobile_no1.get()
    if len(temp) == 10:
        return True
    else:
        popup_mobile()


def check_email():
    temp = email1.get()
    if temp.endswith("@gmail.com"):
        return True
    else:
        popup_email()


def success():
    win2 = tk.Toplevel()
    win2.wm_title("Error")

    l = tk.Label(win2, text="Data added successfully. :) ")
    l.grid(row=0, column=0)

    b = tk.Button(win2, text="Exit", command=win2.destroy)
    b.grid(row=1, column=0)


def check_all():
    if check_mobile() and check_email():
        success()


def popup_mobile():
    win = tk.Toplevel()
    win.wm_title("Error")

    l = tk.Label(win, text="Mobile no must be 10 digit only")
    l.grid(row=0, column=0)

    b = tk.Button(win, text="Exit", command=win.destroy)
    b.grid(row=1, column=0)


def popup_email():
    win1 = tk.Toplevel()
    win1.wm_title("Error")

    l = tk.Label(win1, text="Email must end with @gmail.com")
    l.grid(row=0, column=0)

    b = tk.Button(win1, text="Exit", command=win1.destroy)
    b.grid(row=1, column=0)


tk.Button(window, text="Submit", activebackground="green", command=check_all).grid(row=8, column="5")

window.mainloop()