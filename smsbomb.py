from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

mobile_no = int(input("Enter Mobile no: "))
n = int(input("sms: "))

driver = webdriver.Firefox(executable_path=r'C:\Users\harsh\Desktop\geckodriver.exe')

driver.get("https://www.fast2sms.com/free-sms-without-registration.php")

mobile = driver.find_element_by_id("username")
mobile.send_keys(mobile_no)

message = driver.find_element_by_id("user_message")
message.send_keys("i spam you")

submit = driver.find_element_by_id("loginBTN")

for i in range(0,n):
    submit.click()

driver.close()