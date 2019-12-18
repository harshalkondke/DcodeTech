import string
from random import *
from tkinter import ttk
import pymysql
import tkinter as tk
import base64
import io

database = pymysql.connect(host="localhost", user="root", passwd="Pass@123")

cursor = database.cursor()

try:
    cursor.execute("create database login1")
    database.select_db("login1")
    cursor.execute(
        "Create table user(user_id int auto_increment primary key , u_name varchar(200), u_email varchar(30), u_password varchar(250), age int, DOB DATE, about MEDIUMTEXT, image LONGBLOB)")
    print("Database created successfully :)")
except pymysql.err.ProgrammingError:
    print("Boom... Already created.")

finally:
    database.select_db("login1")

# gui starts here..

window = tk.Tk()
window.title("Welcome :)")


def raise_frame(frame):
    frame.tkraise()


login_frame = tk.Frame(window)
signup_frame = tk.Frame(window)
start = tk.Frame(window)
after_login = tk.Frame(window)

for used_frame in (start, login_frame, signup_frame, after_login):
    used_frame.grid(row=0, column=0, sticky='news')

login = tk.Button(start, text="Login", activebackground="green", command=lambda: raise_frame(login_frame))
login.grid(row=0, column=0)

signup = tk.Button(start, text="Signup", activebackground="green", command=lambda: raise_frame(signup_frame))
signup.grid(row=0, column=1)

# login form here..
################################################################################################################

tk.Label(login_frame, text="LOGIN", bd=6, fg="red").grid(row=0, column=2)

tk.Label(login_frame, text="Email: ", fg="black").grid(row=1, column=2)
email = tk.Entry(login_frame)
email.grid(row=1, column=3)
tk.Label(login_frame, text="Password", bd=6, fg="black").grid(row=2, column=2)
password = tk.Entry(login_frame)
password.grid(row=2, column=3)


def fun_login():
    enter_email = email.get()
    enter_password = password.get()
    cursor.execute("Select u_email, u_password from user where u_email=%s", enter_email)
    var = cursor.fetchall()
    if enter_email == var[0][0]:
        if enter_password == var[0][1]:
            raise_frame(after_login)
            user_email = email.get()
            cursor.execute("Select u_name from user where u_email=%s", user_email)
            user_name = cursor.fetchall()
            tk.Label(after_login, text=user_name, bd=6, fg="red").grid(row=0, column=0)
        else:
            print("wrong password...")
    else:
        print("please check email")


login1 = tk.Button(login_frame, text="Login", activebackground="green", command=fun_login)
login1.grid(row=3, column=4)

back = tk.Button(login_frame, text="Back", activebackground="green", command=lambda: raise_frame(start))
back.grid(row=3, column=5)
# after login here...
################################################################################################################


logout = tk.Button(after_login, text="Log Out", activebackground="green", command=lambda: raise_frame(start))
logout.grid(row=0, column=1)

tk.Label(after_login, text="Age", fg="black").grid(row=1, column=0)
age = tk.Entry(after_login)
age.grid(row=1, column=1)

tk.Label(after_login, text="DOB", fg="black").grid(row=2, column=0)
text12 = tk.Text(after_login, width=12, height=1)
text12.grid(row=2, column=1)


def data_format():
    from tkcalendar import Calendar
    top = tk.Toplevel(after_login)

    def print_set():
        var = Cal.selection_get()
        text12.insert(0.0, var)
        top.destroy()

    Cal = Calendar(top, font="Arial 14", selectmode='day', cursor='hand1')
    Cal.pack()
    btn = tk.Button(top, text="OK", command=print_set)
    btn.pack()


cal = tk.Button(after_login, text="^", activebackground="green", command=data_format)
cal.grid(row=2, column=2)

filepath = tk.Text(after_login, width=20, height=1)
filepath.grid(row=3, column=1)


def file_select():
    # file select code here...
    from tkinter import filedialog
    upload_image = filedialog.askopenfilename(initialdir='',
                                              title='Select img file',
                                              filetypes=(("png files", "*.png"),
                                                         ("all files", "*")))

    filepath.insert(0.0, upload_image)


selfile = tk.Button(after_login, text="upload", activebackground="green", command=file_select)
selfile.grid(row=3, column=2)

tk.Label(after_login, text="About", fg="black").grid(row=4, column=0)
about = tk.Text(after_login, width=20, height=6)
about.grid(row=4, column=1)


from PIL import Image
import PIL.Image


def add_data():
    my_age = age.get()
    Dob = text12.get("1.0", tk.END)
    imgfile = filepath.get("1.0", tk.END)
    img_path = imgfile.strip()
    with open(img_path, 'rb') as f:
        photo = f.read()
    encodestring = base64.b64encode(photo)
    my_about = about.get("1.0", tk.END)
    cursor.execute("update user set age=%s, DOB=%s, image=%s, about=%s where u_email=%s",
                   (my_age, Dob, encodestring, my_about, email.get()))
    database.commit()
    print("successfully added data...")
    cursor.execute("select image from user where u_email=%s", email.get())
    data = cursor.fetchall()
    data1 = base64.b64decode(data[0][0])
    file_like = io.BytesIO(data1)
    img = PIL.Image.open(file_like)
    img.show()
    raise_frame(start)


add_details = tk.Button(after_login, text="submit", activebackground="green", command=add_data)
add_details.grid(row=5, column=1)

# signup form here....
##################################################################################################################

tk.Label(signup_frame, text="SIGN UP", bd=6, fg="red").grid(row=0, column=2)

tk.Label(signup_frame, text="Name: ", fg="black").grid(row=1, column=1)
name = tk.Entry(signup_frame)
name.grid(row=1, column=2)

tk.Label(signup_frame, text="Email: ", fg="black").grid(row=2, column=1)
new_email = tk.Entry(signup_frame)
new_email.grid(row=2, column=2)

tk.Label(signup_frame, text="Password", bd=6, fg="black").grid(row=3, column=1)
new_password = tk.Entry(signup_frame)
new_password.grid(row=3, column=2)

tk.Label(signup_frame, text="Confirm Password", bd=6, fg="black").grid(row=4, column=1)
confirm_password = tk.Entry(signup_frame)
confirm_password.grid(row=4, column=2)

tk.Label(signup_frame, text="Captcha: ", bd=6, fg="black").grid(row=5, column=1)
captcha = tk.Entry(signup_frame)
captcha.grid(row=5, column=2)

text = tk.Text(signup_frame, height=1, width=6)
text.grid(row=5, column=3)


def add_captcha():
    str_char = string.ascii_letters + string.digits
    empty_list = []
    for x in range(randint(5, 5)):
        empty_list.append(choice(str_char))

    add_captcha.data = "".join(empty_list)
    text.insert(tk.END, add_captcha.data)


add_captcha()


def delete_capt():
    text.delete(1.0, tk.END)
    add_captcha()


refresh = tk.Button(signup_frame, text="refresh", activebackground="green", command=delete_capt)
refresh.grid(row=5, column=4)


def fun_signup():
    database.select_db("login1")
    add_name = name.get()
    add_email = new_email.get()
    add_pass = new_password.get()
    add_cpass = confirm_password.get()
    capt = captcha.get()
    if add_cpass == add_pass:
        if capt == add_captcha.data:
            cursor.execute("insert into user(u_name , u_email, u_password) values (%s,%s,%s)",
                           (add_name, add_email, add_pass))
            database.commit()
            print("successfully signup")
            raise_frame(login_frame)
        else:
            print("oops... captcha not matched.. ")
    else:
        print("oops... passwords not matched..")


signup1 = tk.Button(signup_frame, text="SignUp", activebackground="green", command=fun_signup)
signup1.grid(row=6, column=2)

back1 = tk.Button(signup_frame, text="Back", activebackground="green", command=lambda: raise_frame(start))
back1.grid(row=6, column=3)

#################################################################################################################

raise_frame(start)
window.mainloop()
