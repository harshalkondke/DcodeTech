import tkinter as tk

root = tk.Tk()


def raise_frame(frame):
    frame.tkraise()


frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)

for used_frame in (frame1, frame2, frame3, frame4):
    used_frame.grid(row=0, column=0)

btn1 = tk.Button(frame1, text="Frame 1 ", command=lambda: raise_frame(frame2))
btn1.grid(row=1, column=0)

btn2 = tk.Button(frame2, text="Frame 2 ", command=lambda: raise_frame(frame3))
btn2.grid(row=2, column=0)

btn3 = tk.Button(frame3, text="Frame 3 ", command=lambda: raise_frame(frame4))
btn3.grid(row=3, column=0)

btn4 = tk.Button(frame4, text="Frame 4 ", command=lambda: raise_frame(frame1))
btn4.grid(row=4, column=0)

raise_frame(frame2)
root.mainloop()