# Open url in a new window of the default browser, if possible
#
# # Open url in a new page (“tab”) of the default browser, if possible
# webbrowser.open_new_tab(a_website)
#
# webbrowser.open(a_website, 1) # Equivalent to: webbrowser.open_new(a_website)
# webbrowser.open(a_website, 2) # Equivalent to: webbrowser.open_new_tab(a_website)

import webbrowser
import tkinter as tk

window = tk.Tk()
window.title("Search here")

query = tk.Text(window, width=50, height=1)
query.grid(row=0, column=0)

var = tk.IntVar()

google = tk.Radiobutton(window, text="Google", variable=var, value=1)
google.grid(row=2, column=0)

ddg = tk.Radiobutton(window, text="Duck Duck Go", variable=var, value=2)
ddg.grid(row=2, column=1)


def search():
    if str(var.get()) == '1':
        a_website = "https://www.google.com/search?client=firefox-b-d&q=" + query.get(1.0, tk.END)
    else:
        a_website = "https://duckduckgo.com/?q=" + query.get(1.0, tk.END)

    webbrowser.open_new(a_website)


def func(event):
    search()


window.bind('<Return>', func)
tk.Button(window, text="Search", command=search).grid(row=0, column=1)

window.mainloop()
