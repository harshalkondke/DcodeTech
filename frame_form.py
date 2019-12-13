import tkinter as tk

window = tk.Tk()
window.geometry("200x100")


def raise_frame(frame):
    frame.tkraise()


frame1 = tk.Frame(window)
frame2 = tk.Frame(window)

for used_frame in (frame1, frame2):
    used_frame.grid(row=0, column=0)

raise_frame(frame1)

tk.Label(frame1,
         text="First Name: ").grid(row=1, column=2)
F_name = tk.Entry(frame1)
F_name.grid(row=1, column=3)

tk.Label(frame1,
         text="Last Name: ").grid(row=2, column=2)
L_name = tk.Entry(frame1)
L_name.grid(row=2, column=3)

btn2 = tk.Button(window, text="Submit ", command=lambda: raise_frame(frame2))
btn2.grid(row=3, column=0)
tk.Label(frame2, text="Hello ").grid(row=0, column=0)
name = str(F_name.get())
tk.Label(frame2, text=name).grid(row=1, column=0)

window.mainloop()
