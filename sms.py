from tkinter import *

import requests

window = Tk()
window.title("Form")
window.geometry("300x300")
window.configure(background="light grey")

a = Label(window, text="Mobile no.")
a.grid(row=0, column=0, pady=10)
a1 = Entry(window)
a1.grid(row=0, column=1, pady=10)
b = Label(window, text="Message")
b.grid(row=1, column=0, pady=10)
b1 = Text(window, width=15, height=5)
b1.grid(row=1, column=1, pady=10)

btn = Button(window, text="Send", command=lambda: func(str(a1.get()), str(b1.get("1.0", "end-1c"))))

btn.grid(row=3, column=1, pady=10)

URL = 'https://www.way2sms.com/api/v1/sendCampaign'


# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    req_params = {
        'apikey': apiKey,
        'secret': secretKey,
        'usetype': useType,
        'phone': phoneNo,
        'message': textMessage,
        'senderid': senderId
    }
    return requests.post(reqUrl, req_params)


def func(mob, msg):
    # get response
    response = sendPostRequest(URL, 'E1WQHN7NMH089W3LZO77WAVH8ZPHBVAJ', 'XX8LLWFKK1GP9NYK', 'stage', mob,
                               'rutujapowar2015@gmail.com', msg)
    """
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
  """
    # print response if you want
    print(response.text)


window.mainloop()
