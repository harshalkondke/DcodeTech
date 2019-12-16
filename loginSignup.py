import string
from random import *
from tkinter import ttk
import pymysql
import tkinter as tk
from werkzeug.security import check_password_hash, generate_password_hash

database = pymysql.connect(host="localhost", user="root", passwd="Pass@123")

cursor = database.cursor()

try:
    cursor.execute("create database login1")
    database.select_db("login1")
    cursor.execute(
        "Create table user(user_id int auto_increment primary key , u_name varchar(200), u_email varchar(30), u_password varchar(250))")
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

for used_frame in (start, login_frame, signup_frame):
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
    cursor.execute("Select u_password from user where u_email=%s", enter_email)
    original_pass = cursor.fetchall()
    if check_password_hash(original_pass, enter_password):
        print("welcome you're loged in....")
    else:
        print("please check email and password")


login1 = tk.Button(login_frame, text="Login", activebackground="green", command=fun_login)
login1.grid(row=3, column=4)

back = tk.Button(login_frame, text="Back", activebackground="green", command=lambda: raise_frame(start))
back.grid(row=3, column=5)

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
    add_pass = generate_password_hash(new_password.get())
    add_cpass = generate_password_hash(confirm_password.get())
    capt = captcha.get()
    if check_password_hash(add_cpass, add_pass):
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
