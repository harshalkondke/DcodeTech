import tkinter as tk
import requests
import json

# window = tk.Tk()
# window.title("Send SMS")
from urllib3.connectionpool import xrange

mobile = int(input("Enter phone no: "))
n = int(input("sms: "))
URL = 'https://www.way2sms.com/api/v1/sendCampaign'

# import random
# import string
#
# digits = "".join( [random.choice(string.digits) for i in xrange(8)] )
# chars = "".join( [random.choice(string.letters) for i in xrange(15)] )
# message = digits + chars

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


# get response
for i in range(0,n):
    response = sendPostRequest(URL, '5WD19U2JZXHCGTDEMUQFH6RQPOEBX0OD', 'LK61XB84BWRNDGPJ', 'stage', mobile,
                               'harshalkondke2014@gmail.com', i)
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)
