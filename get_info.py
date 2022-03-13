from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from datetime import date
import pytextnow as pytn
from decouple import config

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

    semester = season + ' 20' + year
    return semester


def bot(netID, Password, Commands, UserNum): 
    #netID = config('USERNAME')
    #Password = config('PASSWORD')
    s=Service('/Users/dannychung/StudentReminder/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    #options.add_argument("--headless")
    Bot_Chrome = webdriver.Chrome(service=s, options=options )  

    print("running script..")
    client = pytn.Client("luis29798", sid_cookie="s%3A8fhrkEnwxcHwt51RtxbgBYIOeH_bhxAS.OmVatrUGxqWWZ80coYN0VhJ2G0K15MXH5ggQUQwY%2FnM", csrf_cookie="s%3A0wmGXLUFhATOQU875LeVbnal.m7qZODeJLASfzBqdalYjMIiAccFGlZSPkLyCelL88kA")
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
        client.send_sms(UserNum, "Success Login")
        title = Bot_Chrome.title
        if title == "Information Release":
            #clicks accept button for information release
            Bot_Chrome.find_element(By.XPATH, '/html/body/form/div/div[2]/p[2]/input[2]').click()
            time.sleep(2)
            WebDriverWait(Bot_Chrome,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
            #click courses navigation button
            Bot_Chrome.find_element(By.LINK_TEXT, 'Courses').click()
            #click grid toggle
            time.sleep(2)
            Bot_Chrome.find_element(By.CSS_SELECTOR, 'label.toggle-label.input.label-two.js-label-toggle-grid').click()
            time.sleep(2)
            #WebDriverWait(Bot_Chrome, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content-inner"]/div/div[1]/div[1]/div/div/div[2]/div/header/bb-search-box'))).click()
            Bot_Chrome.find_element_by_css_selector('bb-search-box>div>input').send_keys('Fall 2021')    

            time.sleep(2)
            parentCourseDiv = Bot_Chrome.find_element_by_class_name('course-org-list')
            childElements = parentCourseDiv.get_attribute("childElementCount")
            childElementsNum = int(childElements) - 1

            todos = []
            i = 1
            
            all_course_cards = Bot_Chrome.find_elements_by_tag_name('bb-base-course-card')
            all_course_cards.pop()
            for course in all_course_cards:
                course.click()
                time.sleep(3)

                iframe = Bot_Chrome.find_element_by_xpath("//iframe[@name='classic-learn-iframe']")
                print(iframe)
                Bot_Chrome.switch_to.frame(iframe)
              
                div = Bot_Chrome.find_elements(By.CSS_SELECTOR, '#blocklist\:\:3-dueView\:\:\:\:\:3-dueView_3')
                
                for todo in div:
                    print(todo.text)
                
                time.sleep(3)
                Bot_Chrome.find_element_by_class_name('bb-close').click()
            
            print(childElementsNum)
            if(childElementsNum == -1):
                client.send_sms(UserNum,'no classes for current semester')
            #print(todos)
            time.sleep(45)

    else:
        client.send_sms(UserNum, "Fail login")
    Bot_Chrome.close()

    

