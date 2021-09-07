from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'C:\Users\Pooja\PycharmProjects\pythonProject\harekrishanabehaveproject\features\driver\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.google.com/")
