#   MYCLASS BOT BY PRANAV KHAIRNAR

from selenium import webdriver
import datetime
import time
driver = webdriver.Chrome("D:\Webdriver\chromedriver.exe")
driver.maximize_window()  
driver.get('https://myclass.lpu.in/')

day = datetime.datetime.today().weekday();

username = "12001452"    #Enter Your Username For myclass
password = "password"

u = driver.find_element_by_name("i");
p = driver.find_element_by_name("p");
u.send_keys(username)
p.send_keys(password)
driver.find_element_by_xpath("/html/body/div[2]/div/form/div[7]/button").click()

def monday():
    #classLinkPath = Enter path of your class
    #driver.find_element_by_xpath("").click()
    #time.sleep(3600)
    time.sleep(5)
    driver.quit()
    print("Today is Monday")
def tuesday():
    #classLinkPath = Enter path of your class
    #driver.find_element_by_xpath("").click()
    #time.sleep(3600)
    time.sleep(5)
    driver.quit()
    print("Today is Tuesday")
def wednesday():
    #classLinkPath = Enter path of your class
    #driver.find_element_by_xpath("").click()
    #time.sleep(3600)
    time.sleep(5)
    driver.quit()
    print("Today is Wednesday")
def thursday():  
    #classLinkPath = Enter path of your class
    #driver.find_element_by_xpath("").click()
    #time.sleep(3600)
    time.sleep(5)
    driver.quit()
    print("Today is Thursday")
    
try:
    driver.find_element_by_xpath("/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a").click()
    if(day == 0):
        monday()
    elif(day == 1):
        tuesday()
    elif(day == 2):
        wednesday()
    elif(day == 4):
        thursday()
    else:
        driver.quit()
        print("Today is Holiday")
except:
    time.sleep(1)
    driver.quit()
    print("Wrong username or password")