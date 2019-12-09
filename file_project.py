import tkinter as tk
from tkinter import ttk
from csv import DictWriter

window = tk.Tk()
window.title("Form fill")


def check_mobile():
    temp = Mobile_no.get()
    if len(temp) == 10:
        return True
    else:
        popup_mobile()


def check():
    file = open("data.txt", 'r')
    data = file.read()
    T.insert(0.0, data)
    file.close()

    # csv read ###############
    # file = open('filename.csv', 'r')
    # read_file = DictReader(file)
    # for row in read_file:
    #   print(read_file)


def check_email():
    temp = email.get()
    if temp.endswith("@gmail.com"):
        return True
    else:
        popup_email()


def success():
    win2 = tk.Toplevel()
    win2.wm_title("Wow..")

    l = tk.Label(win2, text="Data added successfully. :) ")
    l.grid(row=0, column=0)

    b = tk.Button(win2, text="Exit", command=win2.destroy)
    b.grid(row=1, column=0)


def success_csv():
    win3 = tk.Toplevel()
    win3.wm_title("Wow..")

    l = tk.Label(win3, text="CSV file generated successfully :) ")
    l.grid(row=0, column=0)

    b = tk.Button(win3, text="Exit", command=win3.destroy)
    b.grid(row=1, column=0)


def success_pdf():
    win4 = tk.Toplevel()
    win4.wm_title("Wow..")

    l = tk.Label(win2, text="PDF file generated successfully :) ")
    l.grid(row=0, column=0)

    b = tk.Button(win4, text="Exit", command=win4.destroy)
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


def write_text_file():
    if check_mobile() and check_email():
        Name = name.get()
        mobile = Mobile_no.get()
        Email = email.get()
        Age = age.get()
        Gender = comboGender.get()
        Eli = v.get()
        file = open("data.txt", 'a')
        file.write("Name : ")
        file.write(Name)
        file.write("\n")
        file.write("Mobile No : ")
        file.write(mobile)
        file.write("\n")
        file.write("Email : ")
        file.write(Email)
        file.write("\n")
        file.write("Age : ")
        file.write(Age)
        file.write("\n")
        file.write("Gender : ")
        file.write(Gender)
        file.write("\n")
        file.write("Eligibility : ")
        file.write(Eli)
        file.write("\n\n\n")
        file.close()
        success()



def write_csv_file():
    file = open("data.csv", 'a')
    dict_writer = DictWriter(file, fieldnames=['Name', 'Mobile_no', 'Email', 'Age', 'Gender', 'Eligibility'])

    if :
        dict_writer.writeheader()
    if check_mobile() and check_email():
        dict_writer.writerow({
            'Name': name.get(),
            'Mobile_no': Mobile_no.get(),
            'Email': email.get(),
            'Age': age.get(),
            'Gender': comboGender.get(),
            'Eligibility': v.get()
        })
        success_csv()


from fpdf import FPDF


def write_pdf_file():
    file = open("data.txt", 'r')
    data = file.read()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 100, txt=data, align="L")
    pdf.output("pdf_" + name.get() + ".pdf")
    file.close()
    success_pdf()


# Name
tk.Label(window,
         text="Name :", ).grid(row=0)
name = tk.Entry(window)
name.grid(row=0, column=5)

# Mobile no
tk.Label(window,
         text="Mobile no :", ).grid(row=1)
Mobile_no = tk.Entry(window)
Mobile_no.grid(row=1, column=5)

# Email
tk.Label(window,
         text="Email :", ).grid(row=2)
email = tk.Entry(window)
email.grid(row=2, column=5)

# age
tk.Label(window,
         text="Age :", ).grid(row=3)
age = tk.Spinbox(window, from_=1, to=100)
age.grid(row=3, column=5)

# gender

gender = tk.Label(window,
                  text="Gender")
gender.grid(row=4)

comboGender = ttk.Combobox(window,
                           values=[
                               "Male",
                               "Female",
                               "Rather not to say"
                           ])
comboGender.grid(row=4, column=5)
# eligible
v = tk.StringVar()

tk.Radiobutton(window,
               text="Eligible",
               padx=20,
               variable=v,
               value=1).grid(row=5, column=0)
tk.Radiobutton(window,
               text="Not Eligible",
               padx=20,
               variable=v,
               value=2).grid(row=5, column=5)

# terms & conditions

terms = tk.IntVar()
Terms_Condition = ttk.Checkbutton(window, text="Agree to terms and Conditions", variable=terms,
                                  onvalue=1, offvalue=0)
Terms_Condition.grid(row=6, column=5)
# get txt
tk.Button(window, text="Get TXT", activebackground="green", command=write_text_file).grid(row=7, column=0)
# get scv
tk.Button(window, text="Get CSV", activebackground="green", command=write_csv_file).grid(row=7, column=5)
# get pdf
tk.Button(window, text="Get PDF", activebackground="green", command=write_pdf_file).grid(row=7, column=10)
# text box
T = tk.Text(window, height=10, width=30)
T.grid(row=8, column=5)
quote = """"""
T.insert(tk.END, quote)
# check (when clicked check button the text stored in file will be displayed in upper text box )
tk.Button(window, text="Check", activebackground="green", command=check).grid(row=8, column=10)
# clear
tk.Button(window, text="Clear", activebackground="green", command=lambda: T.delete(1.0, tk.END)).grid(row=9, column=10)
# end here

window.mainloop()
