import tkinter as tk

root = tk.Tk()

text = tk.Text(root, width=10, height=2)
text.pack()


def data_format():
    from tkcalendar import Calendar
    top = tk.Toplevel(root)

    def print_set():
        var = Cal.selection_get()
        text.insert(0.0, var)
        top.destroy()

    Cal = Calendar(top, font="Arial 14", selectmode='day', cursor='hand1')
    Cal.pack()
    btn = tk.Button(top, text="OK", command=print_set)
    btn.pack()


data_format()

root.mainloop()
