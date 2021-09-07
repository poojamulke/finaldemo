from selenium import webdriver
from getpass import getpass

username = input("Enter in youe username: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome(executable_path=r'C:\Users\Pooja\PycharmProjects\pythonProject\harekrishanabehaveproject\features\driver\chromedriver.exe')
driver.get("https://platformrc.wyscout.com/app/")
driver.implicitly_wait(10)

username_textbox = driver.find_element_by_id("login_username")
username_textbox.send_keys("poojamulke77@gmail.com")

password_textbox = driver.find_element_by_id("login_password")
password_textbox.send_keys("pw_IndiaTest!")

login_button = driver.find_element_by_id("login_button")
login_button.click()
