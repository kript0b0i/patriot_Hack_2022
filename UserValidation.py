from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from decouple import config

def CheckPassword(netID, netPassoword):
    s=Service('/usr/bin/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    Bot = webdriver.Chrome(service=s, options=options ) 
    print("Waiting for validation!")
    Bot.get("https://mymasonportal.gmu.edu/")
    loginButton = Bot.find_element(By.XPATH, '//*[@id="login-form"]/a/button').click()
    usernameBox = Bot.find_element(By.XPATH, '//*[@id="username"]').send_keys(netID)
    passwordBox = Bot.find_element(By.XPATH, '//*[@id="password"]').send_keys(netPassoword)
    title = Bot.title
    if title != "George Mason Federated Login Service":
        print("Correct Username and Password")
    else:
        print("Error, please check your username or password")
    Bot.close()
if __name__ == "__main__":
    username = config('USERNAME')
    password = config('PASSWORD')
    print(username)
    CheckPassword(username, password)
