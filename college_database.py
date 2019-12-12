from tkinter import ttk

import pymysql
import tkinter as tk

from soupsieve.util import string

database = pymysql.connect(host="localhost", user="root", passwd="Pass@123")

cursor = database.cursor()

try:
    cursor.execute("create database college_database")
    database.select_db("college_database")
    cursor.execute(
        "Create table student(S_id int auto_increment primary key , S_name varchar(200), S_gender varchar(30), address varchar(250), DOB varchar(20))")
    cursor.execute(
        "Create table department(D_id int auto_increment primary key, D_name varchar(100))")
    cursor.execute(
        "Create table course(C_id int auto_increment primary key , C_name varchar(200), C_code varchar(10))")
    cursor.execute(
        "Create table faculty(F_id int auto_increment primary key , F_name varchar(200), F_gender varchar(30), exp varchar(250), AGE varchar(2), salary varchar(20))")
    cursor.execute(
        "Create table research_project(P_id int auto_increment primary key , P_name varchar(200), duration varchar(20))")
    print("Database created successfully :)")
except pymysql.err.ProgrammingError:
    print("Boom... Already created.")

finally:
    pass


def gui():
    window = tk.Tk()
    window.title("College Database")

    # student data here...

    tk.Label(window,
             text="Student Info :", bd=6, fg="red").grid(row=0, column=0)

    tk.Label(window,
             text="Name: ").grid(row=1, column=0)
    S_name = tk.Entry(window)
    S_name.grid(row=1, column=1)

    tk.Label(window,
             text="Gender").grid(row=2, column=0)

    S_gender = ttk.Combobox(window,
                            values=[
                                "Male",
                                "Female",
                                "Rather not to say"
                            ])
    S_gender.grid(row=2, column=1)

    tk.Label(window,
             text="Address: ").grid(row=3, column=0)
    address = tk.Entry(window)
    address.grid(row=3, column=1)

    tk.Label(window,
             text="DOB: ").grid(row=4, column=0)
    DOB = tk.Entry(window)
    DOB.grid(row=4, column=1)

    # department data here...

    tk.Label(window,
             text="Department Info :", bd=6, fg="red").grid(row=0, column=2)

    tk.Label(window,
             text="Dept Name: ").grid(row=1, column=2)
    D_name = tk.Entry(window)
    D_name.grid(row=1, column=3)

    # Course Info...

    tk.Label(window,
             text="Course Info :", bd=6, fg="red").grid(row=0, column=4)

    tk.Label(window,
             text="Course Name: ").grid(row=1, column=4)
    C_name = tk.Entry(window)
    C_name.grid(row=1, column=5)

    tk.Label(window,
             text="Code: ").grid(row=2, column=4)
    C_code = tk.Entry(window)
    C_code.grid(row=2, column=5)

    # Faculty Info...

    tk.Label(window,
             text="Faculty Info :", bd=6, fg="red").grid(row=0, column=6)

    tk.Label(window,
             text="Dept Name: ").grid(row=1, column=6)
    F_name = tk.Entry(window)
    F_name.grid(row=1, column=7)

    tk.Label(window,
             text="Gender").grid(row=2, column=6)
    F_gender = ttk.Combobox(window,
                            values=[
                                "Male",
                                "Female",
                                "Rather not to say"
                            ])
    F_gender.grid(row=2, column=7)

    tk.Label(window,
             text="Exp: ").grid(row=3, column=6)
    exp = tk.Entry(window)
    exp.grid(row=3, column=7)

    tk.Label(window,
             text="Salary: ").grid(row=7, column=6)
    salary = tk.Entry(window)
    salary.grid(row=7, column=7)

    # research_project info...

    tk.Label(window,
             text="Research project: ", bd=6, fg="red").grid(row=0, column=8)

    tk.Label(window,
             text="Project Name: ").grid(row=1, column=8)
    P_name = tk.Entry(window)
    P_name.grid(row=1, column=9)

    tk.Label(window,
             text="duration: ").grid(row=2, column=8)
    duration = tk.Entry(window)
    duration.grid(row=2, column=9)

    def insert_data():
        database.select_db("college_database")

        name1 = S_name.get()
        gender1 = S_gender.get()
        address1 = address.get()
        dob1 = DOB.get()
        cursor.execute(
            "insert into student(S_name, S_gender, address, DOB) values(%s, %s, %s, %s)", (name1, gender1, address1, dob1))
        name2 = D_name.get()
        cursor.execute(
            "insert into department(D_name) values(%s)", name2)
        name3 = C_name.get()
        code = C_code.get()
        cursor.execute(
            "insert into course(C_name, C_code) values(%s, %s)", (name3, code))
        name4 = F_name.get()
        gender4 = F_gender.get()
        exp4 = exp.get()
        salary4 = salary.get()
        cursor.execute(
            "insert into faculty(F_name, F_gender, exp, salary) values(%s, %s, %s, %s)", (name4, gender4, exp4, salary4))
        name5 = P_name.get()
        duration5 = duration.get()
        cursor.execute(
            "insert into research_project(P_name, duration) values(%s, %s)", (name5, duration5))

        database.commit()

        print("Data Added successfully...")

    # submit button

    submit = tk.Button(window, text="Submit", activebackground="green", command=insert_data)
    submit.grid(row=8, column=9)

    window.mainloop()


gui()
