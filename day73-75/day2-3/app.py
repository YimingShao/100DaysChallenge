from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime
import time





if __name__ == '__main__':
    browser = webdriver.Chrome()

    User = os.environ.get('MY_MAIL')
    Password = os.environ.get('MY_MAIL_PASSOWRD')

    browser.get("http://www.gmail.com")

    elem = browser.find_element_by_id("identifierId")
    elem.send_keys(User)

    browser.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
    time.sleep(2)

    elem = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    elem.send_keys(Password)

    time.sleep(2)

    browser.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
    time.sleep(2)

    browser.find_element_by_xpath("//*[@id=':hd']/div/div").click()
    time.sleep(2)

    elem = browser.find_element_by_xpath("//*[@id=':mx']")
    elem.send_keys("shaoyiminglobo@gmail.com")
    time.sleep(2)


    browser.quit()



