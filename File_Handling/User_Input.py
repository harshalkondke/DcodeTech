import tkinter as tk

# created window
window = tk.Tk()
window.title("6/12")

# name label and inout filed for first name
tk.Label(window,
         text="First Name").grid(row=0)
fname = tk.Entry(window)
fname.grid(row=0, column=10)

# name label and inout filed for last name
tk.Label(window,
         text="Last Name").grid(row=2)
lname = tk.Entry(window)
lname.grid(row=2, column=10)


# pop up when data added to file successfully
def success():
    win = tk.Toplevel()
    win.wm_title("Wow")

    l = tk.Label(win, text="Data added successfully. :) ")
    l.grid(row=0, column=0)

    b = tk.Button(win, text="Exit", command=window.destroy)
    b.grid(row=1, column=0)


# write user inputs into the file
def write_file():
    first_name = fname.get()
    last_name = lname.get()
    file = open('user_data.txt', 'a')
    file.write(first_name)
    file.write(" ")
    file.write(last_name)
    file.write("\n")
    file.close()
    success()


# submit button # this will initiate the function write_file
tk.Button(window, text="Submit", bg="green", fg="white", command=write_file).grid(row=6, column=10)

window.mainloop()
