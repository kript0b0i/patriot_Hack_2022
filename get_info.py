from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from datetime import date
import pytextnow as pytn

def getSemester():

    season = 'Holiday'

    today = date.today()

    # mm/dd/y
    d3 = today.strftime("%m/%d/%y")

    dateList = d3.split('/')
    month = dateList[0]
    day = dateList[1]
    year = dateList[2]

    if(month == '01' or month == '02' or month == '03' or month == '04' or (month == '05' and day <= 15)):
        season = 'Spring'
    elif((month == '05' and day > 15) or month == '06' or month == '07' or (month == '08' and day <= 15)):
        season = 'Summer'
    elif((month == '08' and day > 15) or month == '09' or month == '10' or month == '11' or month == '12'):
        season = 'Fall'

    semester = season + ' ' + year
    print(semester)

    return semester


def bot(netID, Password, Commands): 
    s=Service('/usr/bin/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    Bot_Chrome = webdriver.Chrome(service=s, options=options )  
    print("running script..")
    client = pytn.Client("dannychung333", sid_cookie="s%3AUzbX3dzpU2DDWhXrpnOayIeKncK0JjhN.R20zdRsZWF2tCDIS5VzjTtIDL4UqDG15qomj8%2FARM1Q", csrf_cookie="s%3A1-RmzV2mdnfXy-MFNLMpnQaT.7hPEJC5lU67MAcewwrlET%2BHSpx33uUMB4GqRIW7vNIU")
    print("opening website")
    Bot_Chrome.get("https://mymasonportal.gmu.edu/")
    time.sleep(1)
    Bot_Chrome.find_element(By.XPATH, '//*[@id="login-form"]/a/button').click()
    time.sleep(2)
    Bot_Chrome.find_element(By.XPATH, '//*[@id="username"]').send_keys(netID)
    print("typing username")
    time.sleep(1)
    Bot_Chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys(Password)
    print("typing password")
    time.sleep(1)
    Bot_Chrome.find_element(By.XPATH, '/html/body/div/div/div/div[2]/form/div[5]/button').click()
    title = Bot_Chrome.title
    if title != "George Mason Federated Login Service":
        client.send_sms("5714842469", "Success Login")
        title = Bot_Chrome.title
        if title == "Information Release":
            Bot_Chrome.find_element(By.XPATH, '/html/body/form/div/div[2]/p[2]/input[2]').click()
            time.sleep(1)
            Bot_Chrome.find_element(By.XPATH, '//*[@id="base_tools"]/bb-base-navigation-button[4]/div/li/a').click()
            time.sleep(1)
            Bot_Chrome.find_element(By.XPATH,'//*[@id="courses-filter"]/li[3]/a/span').click()
            time.sleep(1)
            Bot_Chrome.find_element(By.XPATH, '//*[@id="main-content-inner"]/div/div[1]/div[1]/div/div/div[3]/div/header/bb-search-box/div/input').send_keys("")


    else:
        client.send_sms("5714842469", "Fail login")
    Bot_Chrome.close()

