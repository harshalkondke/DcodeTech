import smtplib
import tkinter as tk

window = tk.Tk()
window.title("Send Email")

tk.Label(window, text="Receiver Email").grid(row=0, column=0)
email = tk.Entry(window)
email.grid(row=0, column=1)

tk.Label(window, text="message").grid(row=1, column=0)
message = tk.Entry(window)
message.grid(row=1, column=1)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rutujapowar2015@gmail.com', 'Rutuja@1999')
    server.sendmail('rutujapowar2015@gmail.com', email.get(), message.get())
    server.quit()
    print("email send successfully")


tk.Button(window, text="send email", command=send_email).grid(row=2, column=0)

window.mainloop()